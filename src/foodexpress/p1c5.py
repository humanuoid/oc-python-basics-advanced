from pathlib import Path

RESOURCE_CSV_MENU = Path(__file__).parent / "resources/menu.csv"

def main():
    try:
        with open(RESOURCE_CSV_MENU, encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")
                name = parts[0]
                price = parts[1]
                print(f"{name} — {price} €")
    except FileNotFoundError:
        print("Menu introuvable")

if __name__ == "__main__":
    main()
