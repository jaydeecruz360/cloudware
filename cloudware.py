import os
import shutil
import zipfile
import argparse
from pathlib import Path

def zip_files(source_dir, output_zip):
    """Compresses the specified directory into a zip file."""
    source_dir = Path(source_dir)
    output_zip = Path(output_zip)

    if not source_dir.exists():
        print(f"Error: The directory {source_dir} does not exist.")
        return

    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                file_path = Path(root) / file
                zipf.write(file_path, file_path.relative_to(source_dir))

    print(f"Files from {source_dir} have been zipped into {output_zip}")

def unzip_files(zip_file, extract_dir):
    """Extracts the contents of a zip file to the specified directory."""
    zip_file = Path(zip_file)
    extract_dir = Path(extract_dir)

    if not zip_file.exists():
        print(f"Error: The file {zip_file} does not exist.")
        return

    with zipfile.ZipFile(zip_file, 'r') as zipf:
        zipf.extractall(extract_dir)

    print(f"Files from {zip_file} have been extracted to {extract_dir}")

def main():
    parser = argparse.ArgumentParser(description="Simplifies the zipping and unzipping of files.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    zip_parser = subparsers.add_parser('zip', help="Zip the files in the given directory")
    zip_parser.add_argument('source_dir', help="The directory to zip")
    zip_parser.add_argument('output_zip', help="The output zip file")

    unzip_parser = subparsers.add_parser('unzip', help="Unzip the given zip file")
    unzip_parser.add_argument('zip_file', help="The zip file to unzip")
    unzip_parser.add_argument('extract_dir', help="The directory to extract files to")

    args = parser.parse_args()

    if args.command == 'zip':
        zip_files(args.source_dir, args.output_zip)
    elif args.command == 'unzip':
        unzip_files(args.zip_file, args.extract_dir)

if __name__ == "__main__":
    main()