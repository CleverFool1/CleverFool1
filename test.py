# test.py
from py_utils import py_logsum
from cy_utils import cy_logsum, np_logsum, c_logsum
import time


# a rough estimation of running time of certain function.
def run_time(x, y, rep, func, func_name):
    total_time = 0.0
    for i in range(5):
        start_time = time.time()
        for _ in range(rep):
            res = func(x, y)
        total_time += time.time() - start_time
    stime = total_time / 5.0
    print("%s: res = %.6f, time = %.2f" % (func_name, res, stime))


def main(x, y, rep):
    run_time(x, y, rep, py_logsum, "py_logsum")
    run_time(x, y, rep, cy_logsum, "cy_logsum")
    run_time(x, y, rep, np_logsum, "np_logsum")
    run_time(x, y, rep, c_logsum, "c_logsum")


if __name__ == "__main__":
    main(3.1, 5.2, 1000000)
