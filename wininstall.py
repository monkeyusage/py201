from os import system

def main():
    system(f"python -m venv venv")
    system(f"venv/Scripts/activate && python -m pip install -r requirements.txt")

if __name__ == "__main__":
    main()
