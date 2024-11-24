import sys


def main():
    if len(sys.argv) < 3:
        sys.exit(1)

    font_name = sys.argv[2].lower()

    font_files = {
        'shadow': 'shadow.txt',
        'standard': 'standard.txt',
        'thinkertoy': 'thinkertoy.txt'
    }

    if font_name not in font_files:
        print("Использовать только 'shadow', 'standard' или 'thinkertoy'.")
        sys.exit(1)

    ascii_file = font_files[font_name]

    try:
        with open(ascii_file, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Файл '{ascii_file}' не найден")
        sys.exit(1)

    ascii_dict = {}

    symbols = [' '] + [chr(i) for i in range(33, 127)]

    for i in range(0, len(lines), 9):
        block = lines[i:i + 8]
        ascii_representation = ''.join(block)

        if i // 9 < len(symbols):
            ascii_dict[symbols[i // 9]] = ascii_representation

    def print_ascii_string(input_string):
        output_lines = ['' for _ in range(8)]
        for char in input_string:
            if char in ascii_dict:
                ascii_char_lines = ascii_dict[char].split('\n')
                for i in range(8):
                    output_lines[i] += ascii_char_lines[i]

        for line in output_lines:
            print(line)

    user_input = sys.argv[1]
    print_ascii_string(user_input)


if __name__ == "__main__":
    main()
