#!/usr/bin/python

# Importing necessary modules
import os
import os.path
import hashlib
import sys  # Need to import sys for accessing command-line arguments

# Function to walk through directory and its subdirectories
def walk(dir):
    hashes = []  # List to store hashes of files
    for path in os.listdir(dir):  # Iterating through files and directories in given directory
        
        fullpath = os.path.join(dir, path)  # Full path of the current file or directory

        if os.path.isdir(fullpath):  # If the current item is a directory
            if path[0:1] == ".":  # Skip hidden directories
                continue
            walk(fullpath)  # Recursively call walk function for subdirectory
            continue

        md5 = hash(fullpath)  # Calculate hash of the file
        if md5 in hashes:  # If hash already exists in the list
            print("Duplicate: " + fullpath)  # Print duplicate file path
            os.remove(fullpath)  # Remove duplicate file
        
        hashes.append(md5)  # Add hash to the list

# Function to calculate hash of a file
def hash(file):
    BLOCK_SIZE = 65536  # The size of each read from the file

    file_hash = hashlib.sha256()  # Create SHA-256 hash object
    with open(file, 'rb') as f:  # Open the file to read its bytes in binary mode
        fb = f.read(BLOCK_SIZE)  # Read a block of bytes from the file
        while len(fb) > 0:  # Loop until no more bytes are read
            file_hash.update(fb)  # Update the hash object with the bytes read
            fb = f.read(BLOCK_SIZE)  # Read the next block of bytes
    return file_hash.hexdigest()  # Return the hexadecimal digest of the hash

if __name__ == "__main__":
    path = sys.argv[0]  # Get the path of the script
    print("Prüfe " + path)  # Print the path being checked
    walk()  # Start walking through the directory structure
