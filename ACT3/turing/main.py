from dicc import Diccionario
import sys


def main() -> None:
    if len(sys.argv) != 2:
        raise Exception(f'Invalid arg number ({len(sys.argv)-1}), one argument should be supplied (.tm file path)')
    else:
        Diccionario(sys.argv[1])


if __name__ == "__main__":
    main()