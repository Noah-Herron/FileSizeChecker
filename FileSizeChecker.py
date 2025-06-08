# put this file in root of directory you want this file sizes of.

# This File looks at all the files in a Directory (and subdirectories) and lists them in 
# Descending order listing the file_size, file_name, and rank

import os

def main():
    file_sizes = []
    # Walk the directory tree
    for root, _, files in os.walk('.'):
        for name in files:
            path = os.path.join(root, name)
            try:
                size_bytes = os.path.getsize(path)
                file_sizes.append((size_bytes, path))
            except OSError:
                continue  # skip files we can’t stat

    # Sort descending by size
    file_sizes.sort(reverse=True, key=lambda x: x[0])

    # Write out rank, size (MB), and path
    with open('files_by_size.txt', 'w') as out:
        out.write("Rank\tSize (MB)\tPath\n")
        for rank, (size_bytes, path) in enumerate(file_sizes, start=1):
            size_mb = size_bytes / (1024 * 1024)
            out.write(f"{rank}\t{size_mb:.2f}\t{path}\n")

    print("Wrote sorted file list to files_by_size.txt")

if __name__ == "__main__":
    main()