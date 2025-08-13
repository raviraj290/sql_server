import subprocess

# Google Drive direct download link
url = "https://drive.google.com/uc?export=download&id=1Gnu57nm6VjaXlgwbw68xeCwO0XQIYtUb"

# Output file name
output_file = r"c:\PRACTISE\data\downloaded_file.csv"

# PowerShell command
ps_command = f"Invoke-WebRequest -Uri '{url}' -OutFile '{output_file}'"

# Run PowerShell from Python
subprocess.run(["powershell", "-Command", ps_command], check=True)

print(f"Downloaded file saved as: {output_file}")
