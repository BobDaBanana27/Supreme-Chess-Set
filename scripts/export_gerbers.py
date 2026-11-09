"""
Supreme Chess Set — Automated Gerber & Drill Export Script
Uses KiCad 10 CLI to export production Gerbers and drill files,
then zips them into ready-to-upload packages for JLCPCB / PCBWay.
"""

import os
import subprocess
import zipfile

KICAD_CLI = r"C:\Program Files\KiCad\10.0\bin\kicad-cli.exe"
HARDWARE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "hardware"))
GERBERS_DIR = os.path.join(HARDWARE_DIR, "gerbers")

BOARDS = [
    {
        "name": "supreme_chess_motherboard",
        "pcb": os.path.join(HARDWARE_DIR, "supreme_chess.kicad_pcb"),
        "out_dir": os.path.join(GERBERS_DIR, "motherboard"),
        "zip": os.path.join(GERBERS_DIR, "supreme_chess_motherboard_gerber.zip")
    },
    {
        "name": "sensor_strip",
        "pcb": os.path.join(HARDWARE_DIR, "sensor_strip.kicad_pcb"),
        "out_dir": os.path.join(GERBERS_DIR, "sensor_strip"),
        "zip": os.path.join(GERBERS_DIR, "sensor_strip_gerber.zip")
    }
]

def export_board(board):
    os.makedirs(board["out_dir"], exist_ok=True)
    
    # 1. Export Gerber layers
    print(f"Exporting Gerbers for {board['name']}...")
    subprocess.run([
        KICAD_CLI, "pcb", "export", "gerbers",
        "-o", board["out_dir"],
        board["pcb"]
    ], check=True)
    
    # 2. Export Drill files
    print(f"Exporting Drill file for {board['name']}...")
    subprocess.run([
        KICAD_CLI, "pcb", "export", "drill",
        "-o", board["out_dir"],
        board["pcb"]
    ], check=True)
    
    # 3. Zip for JLCPCB
    print(f"Zipping {board['zip']}...")
    with zipfile.ZipFile(board["zip"], "w", zipfile.ZIP_DEFLATED) as z:
        for f in os.listdir(board["out_dir"]):
            full_path = os.path.join(board["out_dir"], f)
            if os.path.isfile(full_path) and not f.endswith(".zip"):
                z.write(full_path, arcname=f)
    print(f"Done: {os.path.basename(board['zip'])} ({os.path.getsize(board['zip'])} bytes)")

def main():
    for b in BOARDS:
        export_board(b)
    print("\nAll Gerber ZIP archives generated successfully in hardware/gerbers/")

if __name__ == "__main__":
    main()
