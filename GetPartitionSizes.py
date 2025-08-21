
import os # walk throught parttions 
import psutil # detect the partitions ((python system and process utilities))

def get_folder_size(path):
    """Return total size of all files inside a folder (recursively)."""
    total_size = 0
    for dirpath, _, filenames in os.walk(path, onerror=lambda e: None):
        for f in filenames:
            try:
                fp = os.path.join(dirpath, f)
                if os.path.isfile(fp):
                    total_size += os.path.getsize(fp)
            except (PermissionError, FileNotFoundError):
                continue
    return total_size

def get_biggest_folder(root_path):
    """Return the biggest top-level folder in a given partition."""
    biggest_folder = None
    biggest_size = 0
    for entry in os.scandir(root_path):
        if entry.is_dir(follow_symlinks=False):
            try:
                size = get_folder_size(entry.path)
                if size > biggest_size:
                    biggest_size = size
                    biggest_folder = entry.path
            except (PermissionError, FileNotFoundError):
                continue
    return biggest_folder, biggest_size

def bytes_to_gb(size_in_bytes):
    return round(size_in_bytes / (1024 ** 3), 2)

def main():
    partitions = psutil.disk_partitions()
    for p in partitions:# E,D,F,C
        print(f"\n🔹 Partition: {p.device} ({p.mountpoint})")
        try:
            # total partition file size
            total_size = get_folder_size(p.mountpoint)
            print(f"   Total file size: {bytes_to_gb(total_size)} GB")

            # biggest top-level folder
            biggest_folder, biggest_size = get_biggest_folder(p.mountpoint)
            if biggest_folder:
                print(f"   Biggest folder: {biggest_folder} — {bytes_to_gb(biggest_size)} GB")
            else:
                print("   No accessible folders found.")
        except PermissionError:
            print("   Skipped (Permission Denied)")
        except Exception as e:
            print(f"   Error: {e}")

if __name__ == "__main__":
    main()

# output

#🔹 Partition: C:\ (C:\)
   # Total file size: 140.49 GB
   # Biggest folder: C:\Users — 46.02 GB

#🔹 Partition: D:\ (D:\)
   # Total file size: 176.82 GB
   # Biggest folder: D:\تعليم — 80.07 GB

#🔹 Partition: E:\ (E:\)
   # Total file size: 49.65 GB
   # Biggest folder: E:\installatinos — 32.74 GB

#🔹 Partition: F:\ (F:\)
   # Total file size: 120.75 GB
   # Biggest folder: F:\mine — 114.67 GB
