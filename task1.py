from pathlib import Path
import argparse
import shutil


def parse_args():
    parser = argparse.ArgumentParser(
        description="Копіювання файлів з сортуванням за розширеннями."
    )
    parser.add_argument(
        "--source", type=Path, required=True, help="Шлях до вихідної директорії"
    )
    parser.add_argument(
        "--dest", type=Path, default=Path("dist"), help="Шлях до директорії призначення"
    )
    return parser.parse_args()


def copy_files(src, dst):
    try:
        for item in src.iterdir():
            if item.is_dir():
                copy_files(item, dst)
            else:
                folder = dst / item.name[:1]  # output/f
                folder.mkdir(exist_ok=True, parents=True)
                shutil.copy2(item, folder)
            print(f"Копіювання файлів з {src} завершено.")
    except Exception as e:
        print(f"Помилка під час копіювання: {e}")


def main():
    args = parse_args()
    source = args.source
    dest = args.dest
    copy_files(source, dest)


if __name__ == "__main__":
    main()
