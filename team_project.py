import os


def path_File():
    path = input("Enter path: ")

    if not os.path.exists(path):
        print("Xato! Bunday papka mavjud emas")

        return

    else:
        files = os.listdir(path)

        return files



    


def analyzer_File(path_File):

    planned_moves = {}

    for file in path_File:
        filename, extantion = os.path.splitext(file)

        extantion = extantion.lower()

        if extantion in [".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp"]:
            category = "Image"

        elif extantion in [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".xls", ".pptx", ".csv"]:
            category = "Document"

        elif extantion in [".zip", ".rar", ".7z", ".tar", ".gz"]:
            category = "Archive"

        elif extantion in [".mp3", ".wav", ".flac", ".mp4", ".mkv", ".avi", ".mov"]:
            category = "Media"

        elif extantion in [".py", ".js", ".html", ".css", ".json", ".sql", ".cpp", ".java"]:
            category = "Code"

        elif extantion in [".exe", ".msi", ".dmg"]:
            category = "Executables"

        else:
            category = "Other"

        planned_moves[file] = category

    return planned_moves






def display_plan(planned_moves):
    print("\nPlanned file organization:")

    for file, category in planned_moves.items():
        print(f"{file} → {category}/")






def main():
    files = path_File()

    if files is None:
        return

    planned_moves = analyzer_File(files)

    display_plan(planned_moves)


if __name__ == "__main__":
    main()

