Python File Organizer

A Python-based file organization tool that automatically analyzes files, categorizes them by their extensions, creates corresponding folders, and moves files into their appropriate categories.

📌 About the Project

Managing files manually can be time-consuming, especially when a directory contains many different file types.

Python File Organizer solves this problem by automating the file organization process.

The program scans a selected directory, identifies file extensions, assigns each file to a category, displays a preview of the planned organization, and asks the user for confirmation before moving files.

✨ Features

Automatic File Detection: Scans the selected directory and identifies files.

File Categorization: Groups files based on their extensions.

Folder Creation: Automatically creates folders for each category.

Organization Preview: Displays the planned file organization before making changes.

User Confirmation: Requests permission before moving files.

File Movement: Moves files into their corresponding folders.

Duplicate Handling: Skips files if a file with the same name already exists in the destination.

Summary Report: Displays the number of successfully moved and skipped files.

📂 File Categories

The program organizes files into the following categories:

Category

File Extensions

Images

.jpg, .jpeg, .png, .gif, .svg, .webp

Documents

.pdf, .docx, .doc, .txt, .xlsx, .xls, .pptx, .csv

Archives

.zip, .rar, .7z, .tar, .gz

Media

.mp3, .wav, .flac, .mp4, .mkv, .avi, .mov

Code

.py, .js, .html, .css, .json, .sql, .cpp, .java

Executables

.exe, .msi, .dmg

Other

All other file types

🛠️ Technologies Used

Python 3

    .os — Directory and file handling.

    .pathlib — Working with file paths.

    .shutil — Moving files between directories.


📁 Project Structure

Python-File-Organizer/
│
├── main.py
├── team_project.py
├── analyzer.py
└── README.md

🚀 How to Run

1. Clone the repository

git clone YOUR_REPOSITORY_URL

2. Navigate to the project directory

cd Python-File-Organizer

3. Run the program

python main.py

4. Enter the directory path

When prompted, enter the path of the directory you want to organize.

5. Confirm the operation

The program displays a preview of the planned organization.

Enter y to confirm and move the files, or n to cancel.

💻 Example

Before organization:

Test_Files/
├── photo.jpg
├── document.pdf
├── music.mp3
├── script.py
└── archive.zip

After organization:

Test_Files/
├── Images/
│   └── photo.jpg
│
├── Documents/
│   └── document.pdf
│
├── Media/
│   └── music.mp3
│
├── Code/
│   └── script.py
│
└── Archives/
    └── archive.zip

🎯 Project Goals

This project was developed to practice and improve Python programming skills, including:

Functions and modular programming.

Lists, dictionaries, and tuples.

File and directory handling.

Working with Python modules and imports.

Exception handling.

Automating repetitive tasks.

Building a multi-file Python application.

👨‍💻 Author

Developed as a Python programming practice project.

Language: Python