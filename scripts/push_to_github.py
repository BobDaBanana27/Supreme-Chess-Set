"""
GitHub REST API Fast Push Script — Supreme Chess Set
Efficiently pushes only modified and new files to BobDaBanana27/Supreme-Chess-Set.
Uses GitHub Git Trees API to fetch all remote SHAs in 1 call, avoiding redundant commits.
"""

import os
import sys
import base64
import json
import urllib.request
import urllib.error
import hashlib
import time

OWNER = "BobDaBanana27"
REPO  = "Supreme-Chess-Set"
BRANCH = "main"

WORKSPACE = r"c:\Users\grpie\Documents\ChatGPT\Hack Club Half Life 2\Magnetic Portable Chess set"

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

def calc_blob_sha(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()

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

def get_remote_tree(token):
    res, status = github_api("GET", f"/repos/{OWNER}/{REPO}/git/trees/{BRANCH}?recursive=1", token)
    if status == 200 and "tree" in res:
        return {item["path"]: item["sha"] for item in res["tree"] if item["type"] == "blob"}
    return {}

def push_file(token, local_path, repo_path, remote_sha=None):
    with open(local_path, "rb") as f:
        raw = f.read()
    
    local_sha = calc_blob_sha(raw)
    if remote_sha == local_sha:
        return "UNCHANGED"
    
    content_b64 = base64.b64encode(raw).decode("ascii")
    
    commit_msg = f"Update {repo_path} - Symmetrical capture tray alignment & clean CAD"
    body = {
        "message": commit_msg,
        "content": content_b64,
        "branch": BRANCH,
    }
    if remote_sha:
        body["sha"] = remote_sha
    
    result, status = github_api("PUT", f"/repos/{OWNER}/{REPO}/contents/{repo_path}", token, body)
    
    if status in (200, 201):
        return "UPDATED" if remote_sha else "CREATED"
    else:
        msg = result.get("message", str(result))
        print(f"  FAIL ({status}): {repo_path} - {msg}")
        return "FAILED"

def collect_files():
    files = []
    for root, dirs, filenames in os.walk(WORKSPACE):
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
    
    print(f"Fetching current remote tree for {OWNER}/{REPO} ({BRANCH})...")
    remote_tree = get_remote_tree(token)
    print(f"Found {len(remote_tree)} files on remote branch.\n")
    
    files = collect_files()
    print(f"Scanning {len(files)} local workspace files...\n")
    
    updated = 0
    created = 0
    unchanged = 0
    failed = 0
    
    for i, (local_path, repo_path) in enumerate(files):
        size = os.path.getsize(local_path)
        if size > 50 * 1024 * 1024:
            print(f"  SKIP: {repo_path} too large (>50MB)")
            continue
        
        remote_sha = remote_tree.get(repo_path)
        status = push_file(token, local_path, repo_path, remote_sha)
        
        if status == "UNCHANGED":
            unchanged += 1
        elif status == "UPDATED":
            print(f"  OK Updated: {repo_path} ({size:,} bytes)")
            updated += 1
            time.sleep(0.5)
        elif status == "CREATED":
            print(f"  OK Created: {repo_path} ({size:,} bytes)")
            created += 1
            time.sleep(0.5)
        else:
            failed += 1
    
    print(f"\n{'='*60}")
    print(f"Push Summary:")
    print(f"  Unchanged : {unchanged}")
    print(f"  Updated   : {updated}")
    print(f"  Created   : {created}")
    print(f"  Failed    : {failed}")
    print(f"View repo: https://github.com/{OWNER}/{REPO}")

if __name__ == "__main__":
    main()
