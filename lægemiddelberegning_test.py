# lægemiddelberegning_test.py
# Kør tests med:  pytest lægemiddelberegning_test.py

import pytest
from lægemiddelberegning import (
    volume_for_dose,
    convert_mg_to_g,
    infusion_rate_mL_per_h,
    dilution_stock_volume,
)

def test_volume_for_dose():
    assert volume_for_dose(250, 500, 10) == 5.0


def test_convert_mg_to_g():
    assert convert_mg_to_g(1000) == 1.0
    assert convert_mg_to_g(500) == 0.5


def test_infusion_rate_mL_per_h():
    assert infusion_rate_mL_per_h(20, 1) == 20.0
    assert infusion_rate_mL_per_h(50, 2) == 25.0


def test_dilution_stock_volume():
    assert dilution_stock_volume(10, 2, 50) == 10.0


def test_invalid_inputs():
    # volume_for_dose
    with pytest.raises(ValueError):
        volume_for_dose(-1, 500, 10)
    with pytest.raises(ValueError):
        volume_for_dose(250, 0, 10)
    with pytest.raises(ValueError):
        volume_for_dose(250, 500, 0)

    # convert_mg_to_g
    with pytest.raises(ValueError):
        convert_mg_to_g(0)

    # infusion_rate_mL_per_h
    with pytest.raises(ValueError):
        infusion_rate_mL_per_h(20, 0)
    with pytest.raises(ValueError):
        infusion_rate_mL_per_h(0, 1)

    # dilution_stock_volume
    with pytest.raises(ValueError):
        dilution_stock_volume(0, 2, 50)
    with pytest.raises(ValueError):
        dilution_stock_volume(10, 10, 50)  # C2 må ikke være >= C1
