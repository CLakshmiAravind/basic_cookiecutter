# post_gen_project.py

import os
import shutil
import sys

def run_post_gen_hook(install_path="{{cookiecutter.install_path}}", folder_name="{{cookiecutter.folder_name}}", file_name="{{cookiecutter.file_name}}"):
    # Create directory if it doesn't exist
    if not os.path.exists(install_path):
        os.makedirs(install_path)
    
    # Copy files to the installation path
    # Modify this part according to your setup requirements
    shutil.copytree('./', os.path.join(install_path, folder_name))
    print(f"Setup completed in {install_path}")

# Run the post generation hook

if __name__ == '__main__':
    sys.exit(run_post_gen_hook())
