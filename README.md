# CloudWare

CloudWare is a simple Python tool designed to simplify the zipping and unzipping of files using native Windows capabilities, allowing efficient management of compressed files. This utility leverages Python's built-in libraries to manage file compression and extraction.

## Features

- **Zip Files:** Compresses a specified directory into a zip file.
- **Unzip Files:** Extracts the contents of a zip file to a specified directory.

## Requirements

- Python 3.6 or later

## Installation

Clone the repository and navigate into the project directory:

```bash
git clone https://github.com/yourusername/cloudware.git
cd cloudware
```

## Usage

CloudWare provides command-line interface (CLI) to zip and unzip files.

### Zip Files

To compress a directory, use the `zip` command followed by the source directory and the desired output zip file:

```bash
python cloudware.py zip <source_directory> <output_zip_file>
```

Example:

```bash
python cloudware.py zip ./my_folder ./my_archive.zip
```

### Unzip Files

To extract a zip file, use the `unzip` command followed by the zip file and the target extraction directory:

```bash
python cloudware.py unzip <zip_file> <extract_directory>
```

Example:

```bash
python cloudware.py unzip ./my_archive.zip ./extracted_files
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.