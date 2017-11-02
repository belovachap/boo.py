"A spooooky Python program about Halloween."

import argparse
import boo2017

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Boo!')
    parser.add_argument(
        'year',
        type=int,
        choices=[2017,],
        help='Which Halloween are you being spooked upon?'
    )
    args = parser.parse_args()

    if args.year == 2017:
        boo2017.boo()
    else:
        raise Exception("A very spooooky year.")
