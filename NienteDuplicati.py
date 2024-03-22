#!/usr/bin/python

import os
import os.path
import hashlib

def walk(dir):
    hashes = []
    for path in os.listdir(dir):
        
        fullpath = os.path.join(dir, path)

        if os.path.isdir(fullpath): 
            if path[0:1] == ".": continue
            walk(fullpath)
            continue

        md5 = hash(fullpath)
        if md5 in hashes:
            print("Duplicate: " + fullpath)
            os.remove(fullpath)
        
        hashes.append(md5)

def hash(file):
    BLOCK_SIZE = 65536 # The size of each read from the file

    file_hash = hashlib.sha256() # Create the hash object, can use something other than `.sha256()` if you wish
    with open(file, 'rb') as f: # Open the file to read it's bytes
        fb = f.read(BLOCK_SIZE) # Read from the file. Take in the amount declared above
        while len(fb) > 0: # While there is still data being read from the file
            file_hash.update(fb) # Update the hash
            fb = f.read(BLOCK_SIZE) # Read the next block from the file
    return file_hash.hexdigest()

if __name__ == "__main__":
    path = sys.argv[0]
    print("Prüfe " + path)
    walk()
