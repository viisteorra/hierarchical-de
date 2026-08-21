"""Locked 1:11 mix on a 12-fold period. Not a fit parameter.

One Euclidean square seed (q=4) + eleven hyperbolic square steps (q=5)
per octave-length period. Residual tail T = 49/71. Do not retune 1:11
from a better χ²; that needs a new geometric derivation.
"""

# 1 part q=4  (r = 2/4 = 0.5)  +  11 parts q=5  (r = 2/5 = 0.4)
Q4_WEIGHT = 1
Q5_WEIGHT = 11
TOTAL = Q4_WEIGHT + Q5_WEIGHT          # 12

r = (Q4_WEIGHT * (2 / 4) + Q5_WEIGHT * (2 / 5)) / TOTAL   # 4.9/12
OMEGA_DE_TODAY = r / (1 - r)           # 4.9/7.1 ≈ 0.69014
OMEGA_M = 1.0 - OMEGA_DE_TODAY
