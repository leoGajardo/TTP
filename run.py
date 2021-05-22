#!/usr/bin/python

# ====================================================================================
#  Experiment 3 from the paper
#  "Population-based vs. Single-solution heuristics for the Travelling Thief Problem"
# ====================================================================================

import os
import time


instances = [
  "eil76_n75_bounded-strongly-corr_01.ttp",
  "kroA100_n99_bounded-strongly-corr_01.ttp",
  "ch130_n129_bounded-strongly-corr_01.ttp",
  "u159_n158_bounded-strongly-corr_01.ttp",
  "a280_n279_bounded-strongly-corr_01.ttp",
  "u574_n573_bounded-strongly-corr_01.ttp",
  "u724_n723_bounded-strongly-corr_01.ttp",

  "eil76_n375_uncorr-similar-weights_05.ttp",
  "kroA100_n495_uncorr-similar-weights_05.ttp",
  "ch130_n645_uncorr-similar-weights_05.ttp",
  "u159_n790_uncorr-similar-weights_05.ttp",
  "a280_n1395_uncorr-similar-weights_05.ttp",
  "u574_n2865_uncorr-similar-weights_05.ttp",
  "u724_n3615_uncorr-similar-weights_05.ttp",

  "eil76_n750_uncorr_10.ttp",
  "kroA100_n990_uncorr_10.ttp",
  "ch130_n1290_uncorr_10.ttp",
  "u159_n1580_uncorr_10.ttp",
  "a280_n2790_uncorr_10.ttp",
  "u574_n5730_uncorr_10.ttp",
  "u724_n7230_uncorr_10.ttp",
]

# nb of iterations
n = 10

# test all instances
for instance in instances:
    for i in range(0,n):
      os.system("java -jar ./build/libs/ttplab-1.1.jar "+instance+" cs2sa " + instance + ".csv")
      time.sleep(2)