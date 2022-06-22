import torch

import contextlib
import logging
import time
from collections import Counter
from functools import partial, reduce
from operator import mul
from math import sqrt

log = logging.getLogger(__name__)

class Once(set):
    def __call__(self, *x):
        return x not in self and (self.add(x) or True)

timers = Counter()

@contextlib.contextmanager
def timer(name):
    t0 = time.perf_counter()
    yield
    t1 = time.perf_counter()
    timers[name] += t1 - t0

def divisors(n):
    ret = []
    for i in range(1, int(sqrt(n))+2):
        if n % i == 0:
            ret.append(i)
            ret.append(n//i)

    return ret

