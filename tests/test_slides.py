#########################
# Load the main package #
#########################
from .context import pyslides

##################
# Testing module #
##################
import pytest

@pytest.mark.parametrize("attr", [('add'), ('save')])
def test_slides_has_needed_attrs(attr):
    assert hasattr(pyslides.Slides, attr)

    
