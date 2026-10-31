import os

files = ["sales.csv", "sales.json", "sales.parquet"]

print("File size comparison:\n")

for file in files:
    size = os.path.getsize(file)

    print(f"{file}: {size:,} bytes")



### os.path.getsize() retrieves a file's size in bytes.
### A loop allows us to check multiple files.
### This is a simple example of how data engineers inspect storage usage.