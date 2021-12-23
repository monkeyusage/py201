from os import system

def main():
    system(r"python -m venv venv")
    system(r".\venv\Scripts\activate && python -m pip install --upgrade pip && python -m pip install -r requirements.txt")

if __name__ == "__main__":
    main()
