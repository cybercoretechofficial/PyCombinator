
import argparse

def main():
    parser = argparse.ArgumentParser(description='CLI Tool Example')
    parser.add_argument('name', type=str, help='Your name')
    args = parser.parse_args()
    print(f"Hello, {args.name}! Welcome to the Python CLI Tool.")

if __name__ == "__main__":
    main()
