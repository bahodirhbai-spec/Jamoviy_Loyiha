
from pathlib import Path

from team_project import (
    path_File,
    analyzer_File,
    display_plan
)

from analyzer import (
    create_folders,
    confirm,
    move_files,
    print_summary
)


def main():

    # 1. Papka manzilini olish
    files = path_File()

    if files is None:
        return

    planned_moves = analyzer_File(files)

    folder = Path(input("Enter the same folder path again: ").strip())

    plan = []

    for filename, category in planned_moves.items():

        src = folder / filename

        # Faqat oddiy fayllarni qabul qil
        # amiz
        if not src.is_file():
            continue

        plan.append((src, category))

        # 4. Rejani ko'rsatish
        display_plan(planned_moves)

    if not plan:
        print("No files found.")
        return

    # 5. Foydalanuvchidan tasdiq olish
    if confirm():

        # 6. Papkalarni yaratish
        create_folders(folder, plan)

        # 7. Fayllarni ko'chirish
        moved, skipped = move_files(folder, plan)

        # 8. Yakuniy natija
        print_summary(moved, skipped)

    else:
        print("Cancelled. Nothing was changed.")


if __name__ == "__main__":
    main()
