# You may modify this file without removing what's already present.
import sys
import math
from datetime import date
from currency_converter import CurrencyConverter

def f(x):
    a = int(x * 10000)
    return (a - 1597) >> 2

if __name__ == "__main__":
    c = CurrencyConverter(fallback_on_missing_rate=True)
    
    if len(sys.argv[1:]) != 4:
        print("You did not input enough information")
        sys.exit()

    curr1, curr2, dd, mm = sys.argv[1:]

    if not curr1 in c.currencies:
        print("One of your inputs is not correct")
        sys.exit()
    if not curr2 in c.currencies:
        print("One of your inputs is not correct")
        sys.exit()

    conv = c.convert(1, curr1, curr2, date=date(2025, int(mm), int(dd)))
    print(f'The capital of your destionation was founded in: {f(conv)}')
