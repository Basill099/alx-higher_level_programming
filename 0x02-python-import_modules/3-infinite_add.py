#!/usr/bin/python3
if __name__ == "__main__":
    import math
    result = 0
    for i in sys.argv:
        result += int(i)
        print("{}".format(result))
