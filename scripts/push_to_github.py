"""
GitHub REST API Push Script — Supreme Chess Set
Pushes all project files from the local workspace to BobDaBanana27/Supreme-Chess-Set
Requires a GitHub Personal Access Token with repo scope (Contents: read & write).

Usage:
  python scripts/push_to_github.py <GITHUB_TOKEN>
"""

import os
import sys
import base64
import json
import urllib.request
import urllib.error
import time

OWNER = "BobDaBanana27"
REPO  = "Supreme-Chess-Set"
BRANCH = "main"

WORKSPACE = r"c:\Users\grpie\Documents\ChatGPT\Hack Club Half Life 2\Magnetic Portable Chess set"

# Files/directories to skip
SKIP_PATTERNS = [
    "__pycache__",
    ".FCBak",
    ".pyc",
    ".system_generated",
]

def should_skip(path):
    for pat in SKIP_PATTERNS:
        if pat in path:
            return True
    return False

def github_api(method, path, token, body=None):
    url = f"https://api.github.com{path}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "SupremeChessSet-Pusher/1.0",
        "Content-Type": "application/json",
    }
    data = json.dumps(body).encode("utf-8") if body else None
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode("utf-8")), resp.status
    except urllib.error.HTTPError as e:
        body_text = e.read().decode("utf-8")
        return json.loads(body_text) if body_text else {}, e.code

def get_existing_sha(token, repo_path):
    result, status = github_api("GET", f"/repos/{OWNER}/{REPO}/contents/{repo_path}?ref={BRANCH}", token)
    if status == 200 and "sha" in result:
        return result["sha"]
    return None

def push_file(token, local_path, repo_path):
    with open(local_path, "rb") as f:
        raw = f.read()
    
    # Try to decode as UTF-8 text; use binary base64 for binary files
    content_b64 = base64.b64encode(raw).decode("ascii")
    
    sha = get_existing_sha(token, repo_path)
    
    commit_msg = f"Upload {repo_path}"
    body = {
        "message": commit_msg,
        "content": content_b64,
        "branch": BRANCH,
    }
    if sha:
        body["sha"] = sha
    
    result, status = github_api("PUT", f"/repos/{OWNER}/{REPO}/contents/{repo_path}", token, body)
    
    if status in (200, 201):
        action = "Updated" if sha else "Created"
        print(f"  OK {action}: {repo_path}")
        return True
    else:
        msg = result.get("message", str(result))
        print(f"  FAIL ({status}): {repo_path} - {msg}")
        return False

def collect_files():
    files = []
    for root, dirs, filenames in os.walk(WORKSPACE):
        # Skip hidden/system dirs
        dirs[:] = [d for d in dirs if not d.startswith(".") and d != "__pycache__"]
        for fname in filenames:
            full = os.path.join(root, fname)
            rel = os.path.relpath(full, WORKSPACE).replace("\\", "/")
            if not should_skip(rel):
                files.append((full, rel))
    return sorted(files, key=lambda x: x[1])

def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/push_to_github.py <GITHUB_TOKEN>")
        sys.exit(1)
    
    token = sys.argv[1].strip()
    
    files = collect_files()
    print(f"Found {len(files)} files to push to {OWNER}/{REPO}/{BRANCH}\n")
    
    success = 0
    fail = 0
    
    for i, (local_path, repo_path) in enumerate(files):
        size = os.path.getsize(local_path)
        print(f"[{i+1:3d}/{len(files)}] {repo_path} ({size:,} bytes)")
        
        if size > 50 * 1024 * 1024:  # 50MB GitHub limit
            print(f"  SKIP: File too large (>50MB)")
            continue
        
        ok = push_file(token, local_path, repo_path)
        if ok:
            success += 1
        else:
            fail += 1
        
        # Polite rate limiting: 1 request per second to avoid 403
        time.sleep(0.8)
    
    print(f"\n{'='*60}")
    print(f"Push complete: {success} uploaded, {fail} failed")
    print(f"View repo: https://github.com/{OWNER}/{REPO}")

if __name__ == "__main__":
    main()
