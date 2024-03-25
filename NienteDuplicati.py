import os
import hashlib

def file_checksum(file_path):
    """Generate MD5 checksum for a file."""
    with open(file_path, 'rb') as f:
        checksum = hashlib.md5()
        while chunk := f.read(8192):
            checksum.update(chunk)
    return checksum.hexdigest()

def find_duplicate_files(root_dir):
    """Find duplicate files within directories and subdirectories."""
    file_hash_map = {}
    duplicate_files = []

    for dirpath, _, filenames in os.walk(root_dir):
        file_hash_map.clear()  # Clear the map for each directory
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if os.path.isfile(file_path):
                file_hash = file_checksum(file_path)
                if file_hash in file_hash_map:
                    duplicate_files.append(file_path)
                else:
                    file_hash_map[file_hash] = file_path

    return duplicate_files

def delete_duplicate_files(duplicate_files):
    """Delete duplicate files."""
    for file_path in duplicate_files:
        os.remove(file_path)
        print(f"Deleted: {file_path}")

def main():
    root_directory ="/Volumes/FotosSSD/Fotos"
    duplicate_files = find_duplicate_files(root_directory)

    if duplicate_files:
        print("Duplicate files found:")
        for file_path in duplicate_files:
            print(file_path)
        delete_confirmation = input("Do you want to delete the duplicates? (yes/no): ")
        if delete_confirmation.lower() == "yes":
            delete_duplicate_files(duplicate_files)
            print("Duplicate files have been deleted.")
        else:
            print("Duplicate files were not deleted.")
    else:
        print("No duplicate files found.")

if __name__ == "__main__":
    main()
