"""The data split must be reproducible from split_seed alone.

Legacy behaviour fixes split_seed=42 across replicates (so only noise and model
init vary). ``--vary-split-seed`` derives split_seed from the run seed instead.
These tests pin both directions with tiny, fast data sizes.
"""
from __future__ import annotations

import numpy as np

from lcert.data import generate_trajectory_splits


def _config(*, split_seed: int, seed: int = 0) -> dict:
    return {
        "system": "double_integrator",
        "state_lo": [-1.0, -2.0],
        "state_hi": [3.0, 2.0],
        "umax": 1.0,
        "dt": 0.05,
        "trajectory_steps": 3,
        "trajectory_counts": {"train": 2, "validation": 1, "test": 1},
        "derivative_observation_noise_std": 0.0,
        "split_seed": split_seed,
        "seed": seed,
        "max_sampling_attempts": 5000,
        "coverage_gap": {"enabled": False},
    }


def test_same_split_seed_gives_identical_training_arrays():
    a, _ = generate_trajectory_splits(_config(split_seed=7))
    b, _ = generate_trajectory_splits(_config(split_seed=7))
    np.testing.assert_array_equal(a["train"]["states"], b["train"]["states"])
    np.testing.assert_array_equal(a["train"]["features"], b["train"]["features"])
    np.testing.assert_array_equal(a["train"]["targets"], b["train"]["targets"])


def test_different_split_seed_gives_different_training_arrays():
    a, _ = generate_trajectory_splits(_config(split_seed=7))
    b, _ = generate_trajectory_splits(_config(split_seed=8))
    assert a["train"]["states"].shape == b["train"]["states"].shape
    assert not np.array_equal(a["train"]["states"], b["train"]["states"])
