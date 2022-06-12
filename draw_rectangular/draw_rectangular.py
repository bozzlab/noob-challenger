import argparse
from typing import Optional


def draw_rectangular(
    width: int = 0,
    high: int = 0,
    vertical_symbol: Optional[str] = "|",
    horizontal_symbol: Optional[str] = "─",
    conner_symbol: Optional[str] = "+",
    empty_symbol: Optional[str] = " "
):
    w_boundary = width - 1
    h_boundary = high - 1
    conner = ["0,0", f"0,{w_boundary}", f"{h_boundary},0", f"{h_boundary},{w_boundary}"]
    symbol = None

    for x in range(high):
        for y in range(width):
            if x in (0, h_boundary):
                symbol = horizontal_symbol
            elif y in (0, w_boundary):
                symbol = vertical_symbol
            else:
                symbol = empty_symbol

            if f"{x},{y}" in conner:  # bored tuple
                symbol = conner_symbol

            print(symbol, end="  ")
        print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--width', type=int)
    parser.add_argument('--high', type=int)

    args = parser.parse_args()

    draw_rectangular(width=args.width, high=args.high)