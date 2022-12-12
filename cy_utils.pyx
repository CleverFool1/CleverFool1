 #cy_utils.pyx
from math import log as mt_log
from numpy import log as np_log
from libc.math cimport log as c_log

def cy_logsum(x, y):
  return mt_log(x + y)

def np_logsum(x, y):
  return np_log(x + y)

def c_logsum(x, y):
  return c_log(x + y)