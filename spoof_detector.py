import os

# Magic number database
MAGIC_NUMBERS = {
    b"\xFF\xD8\xFF": "jpeg",
    b"\x89PNG\r\n\x1a\n": "png",
    b"GIF87a": "gif",
    b"GIF89a": "gif",
    b"%PDF": "pdf",
    b"PK\x03\x04": "zip/docx/xlsx/pptx/apk",
    b"Rar!\x1A\x07\x00": "rar",
    b"\x1F\x8B": "gz",
    b"ID3": "mp3",
    b"\xFF\xFB": "mp3",
    b"\x00\x00\x00\x18ftyp": "mp4",
    b"\x00\x00\x00\x14ftyp": "mp4",
    b"MZ": "exe",
    b"\x7FELF": "elf (linux executable)",
    b"BM": "bmp",
    b"II*\x00": "tiff",
    b"MM\x00*": "tiff",
    b"SQLite format 3\x00": "sqlite db",
}

def get_file_header(file_path, size=16):
    with open(file_path, "rb") as f:
        return f.read(size)

def detect_file_type(header):
    for magic, filetype in MAGIC_NUMBERS.items():
        if header.startswith(magic):
            return filetype
    return "unknown"

def check_file(file_path):
    if not os.path.isfile(file_path):
        print("Invalid file path")
        return

    header = get_file_header(file_path)
    real_type = detect_file_type(header)

    extension = file_path.split('.')[-1].lower()

    print("\n--- File Analysis ---")
    print(f"File: {file_path}")
    print(f"Extension: .{extension}")
    print(f"Detected Type: {real_type}")

    if real_type == "unknown":
        print("⚠️ Unknown file type (not in database)")
    elif extension not in real_type:
        print("🚨 MISMATCH DETECTED: Possible spoofed file!")
    else:
        print("✅ File type matches")

def scan_folder(folder_path):
    for file in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file)
        if os.path.isfile(full_path):
            check_file(full_path)

# -------- RUN --------
choice = input("1. Scan single file\n2. Scan folder\nChoose option: ")

if choice == "1":
    path = input("Enter file path: ")
    check_file(path)

elif choice == "2":
    folder = input("Enter folder path: ")
    scan_folder(folder)

else:
    print("Invalid option")