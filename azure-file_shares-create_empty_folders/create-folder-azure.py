from azure.storage.fileshare import ShareClient

# Azure File Share account information
connect_str = ""
share_name = ""

# Path to text file containing folder names
txt_file_path = "folders.txt"

# Path to parent folder where you want to create subfolders
parent_folder_path = "templates/customer/"

# Create a ShareClient object
share_client = ShareClient.from_connection_string(connect_str, share_name=share_name)

# Read folder names from text file
with open(txt_file_path, "r") as file:
    folder_names = [line.strip() for line in file]

if not share_client.get_directory_client(parent_folder_path).exists():
    print(f"Incorect parent folder: {parent_folder_path}")

# Create folders in Azure File Share
for folder_name in folder_names:
    # Modify folder name to include parent folder path
    folder_name = parent_folder_path + folder_name.replace(" ", "-").lower()
    
    # Create the folder
    if not share_client.get_directory_client(folder_name).exists():
        share_client.get_directory_client(folder_name).create_directory()
        print(f"+ Created folder: {folder_name}")
    else:
        print(f"- Folder exist: {folder_name}")


