import argparse
import json
from os.path import expanduser
from typing import Dict


def get_count_total(the_dict: Dict[str, Dict[str, str]]) -> int:
    return sum(len(the_dict[key]) for key in the_dict)


def print_info(path: str):
    # Get json data
    numbers_dict = read_json(path)

    # Print total count
    count_total = get_count_total(numbers_dict)
    print(f"\nTotal numbers: {count_total}")

    # Print device counts
    for device in numbers_dict:
        print(f"Numbers on {device}: {len(numbers_dict[device])}")

    print()

    # Print numbers by device
    for device in numbers_dict:
        for i in range(the_count := len(the_list := list(numbers_dict[device]))):
            answer = ""
            while answer != "y":
                print(f"Device:\t{device} ({i + 1:0>2}/{the_count:0>2})")
                print(f"Email:\t{the_list[i]}")
                print(f"Number:\t{numbers_dict[device][the_list[i]]}")
                answer = input("Did you send a keep-alive message? [y/n] ")
                print()

    print("Well done!\n")


def read_json(path: str) -> Dict[str, Dict[str, str]]:
    result = {}

    try:
        with open(expanduser(path), "r") as file:
            result = json.load(file)
    except Exception as e:
        print(f"Read json error: {e}")

    return result


def search_info(path: str, query: str) -> bool:
    # Init flag
    match = False

    # Get json data
    numbers_dict = read_json(path)
    print()

    # Search emails and numbers
    for device in numbers_dict:
        for email in numbers_dict[device]:
            if query in email or query in numbers_dict[device][email]:
                match = True
                print(f"Device:\t{device}")
                print(f"Email:\t{email}")
                print(f"Number:\t{numbers_dict[device][email]}\n")

    if match:
        return True

    print("No results found!\n")
    return False


def main(params: argparse.Namespace):
    if not params.f:
        return False

    if params.s:
        return search_info(params.f, params.s)

    print_info(params.f)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f",
        type=str,
        nargs="?",
        default="example.json",
        help="file path"
    )
    parser.add_argument(
        "-s",
        type=str,
        nargs="?",
        help="search information"
    )
    args = parser.parse_args()
    main(args)
