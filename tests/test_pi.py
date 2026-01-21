import pytest
import numpy as np
from picalc_ip8725.pi.pi import estimate_pi

def test_estimate_pi():
    assert np.isclose(estimate_pi(10_000_000, 4), 3.1412, rtol=0.01)
