# mygame/__main__.py

from .app import App

def main() -> int:
    App.Init_app()
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
