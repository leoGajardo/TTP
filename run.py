#!/usr/bin/python

# ====================================================================================
#  Experiment 3 from the paper
#  "Population-based vs. Single-solution heuristics for the Travelling Thief Problem"
# ====================================================================================

import os
import time


instances = [
#   "eil76_n75_bounded-strongly-corr_04.ttp",
#   "kroA100_n99_bounded-strongly-corr_04.ttp",
#   "ch130_n129_bounded-strongly-corr_04.ttp",
#   "u159_n158_bounded-strongly-corr_04.ttp",
#   "a280_n279_bounded-strongly-corr_04.ttp",
#   "u574_n573_bounded-strongly-corr_04.ttp",
#   "u724_n723_bounded-strongly-corr_04.ttp",
#
#   "eil76_n375_uncorr-similar-weights_03.ttp",
#   "kroA100_n495_uncorr-similar-weights_03.ttp",
#   "ch130_n645_uncorr-similar-weights_03.ttp",
#   "u159_n790_uncorr-similar-weights_03.ttp",
#   "a280_n1395_uncorr-similar-weights_03.ttp",
#   "u574_n2865_uncorr-similar-weights_03.ttp",
#   "u724_n3615_uncorr-similar-weights_03.ttp",
#
#   "eil76_n750_uncorr_07.ttp",
#   "kroA100_n990_uncorr_07.ttp",
#   "ch130_n1290_uncorr_07.ttp",
#   "u159_n1580_uncorr_07.ttp",
#   "a280_n2790_uncorr_07.ttp",
#   "u574_n5730_uncorr_07.ttp",
#   "u724_n7230_uncorr_07.ttp",
#
#     "eil76_n75_bounded-strongly-corr_05.ttp",
#     "kroA100_n99_bounded-strongly-corr_05.ttp",
#     "ch130_n129_bounded-strongly-corr_05.ttp",
    "u159_n158_bounded-strongly-corr_05.ttp",
    "a280_n279_bounded-strongly-corr_05.ttp",
    "u574_n573_bounded-strongly-corr_05.ttp",
    "u724_n723_bounded-strongly-corr_05.ttp",

    "eil76_n375_uncorr-similar-weights_07.ttp",
    "kroA100_n495_uncorr-similar-weights_07.ttp",
    "ch130_n645_uncorr-similar-weights_07.ttp",
    "u159_n790_uncorr-similar-weights_07.ttp",
    "a280_n1395_uncorr-similar-weights_07.ttp",
    "u574_n2865_uncorr-similar-weights_07.ttp",
    "u724_n3615_uncorr-similar-weights_07.ttp",

    "eil76_n750_uncorr_06.ttp",
    "kroA100_n990_uncorr_06.ttp",
    "ch130_n1290_uncorr_06.ttp",
    "u159_n1580_uncorr_06.ttp",
    "a280_n2790_uncorr_06.ttp",
    "u574_n5730_uncorr_06.ttp",
    "u724_n7230_uncorr_06.ttp",
]

# nb of iterations
n = 10
algo = "cs2sa"
# test all instances
for instance in instances:
    for i in range(0,n):
      output = instance + "_" + algo + ".csv"
      os.system("java -jar ./build/libs/ttplab-1.1.jar "+instance+" " + algo + " " + output)
      time.sleep(2)