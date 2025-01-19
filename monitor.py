import os
import time
import subprocess
import shutil  # For moving files

# Configuration
FOLDER_PATH = "./images"  # Replace with your folder path
UPLOADED_FOLDER = "./uploaded"  # Folder for successfully uploaded files
UPLOAD_URL = "https://projects.benax.rw/f/o/r/e/a/c/h/p/r/o/j/e/c/t/s/4e8d42b606f70fa9d39741a93ed0356c/iot_testing_202501/upload.php"  # Upload endpoint
UPLOAD_INTERVAL = 30  # Time interval in seconds

# Ensure the "uploaded" folder exists
os.makedirs(UPLOADED_FOLDER, exist_ok=True)

def upload_file_with_curl(file_path):
    """Upload a file using the curl command."""
    try:
        # Construct the curl command
        command = [
            "curl",
            "-X", "POST",
            "-F", f"imageFile=@{file_path}",
            UPLOAD_URL
        ]
        # Run the curl command and capture the output
        result = subprocess.run(command, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"Uploaded successfully: {file_path}")
            return True
        else:
            print(f"Failed to upload {file_path}: {result.stderr}")
            return False
    except Exception as e:
        print(f"Error uploading {file_path}: {e}")
        return False

def process_folder():
    """Monitor folder, upload files, and move them after successful upload."""
    for file_name in os.listdir(FOLDER_PATH):
        file_path = os.path.join(FOLDER_PATH, file_name)
        if os.path.isfile(file_path):  # Ensure it's a file
            if upload_file_with_curl(file_path):  # If upload succeeds
                # Move the file to the uploaded folder
                uploaded_path = os.path.join(UPLOADED_FOLDER, file_name)
                shutil.move(file_path, uploaded_path)
                print(f"Moved to uploaded folder: {uploaded_path}")

if __name__ == "__main__":
    while True:
        process_folder()
        time.sleep(UPLOAD_INTERVAL)
