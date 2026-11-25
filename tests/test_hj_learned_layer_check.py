"""The learned-HJ dynamics evaluator supports exactly two hidden layers."""
from __future__ import annotations

import numpy as np
import pytest

from lcert.hj_learned import LearnedDoubleIntegratorDynamics


def _weights(n_linear_layers: int):
    members = tuple(
        tuple(np.zeros((2, 3), dtype=np.float32) for _ in range(n_linear_layers))
        for _ in range(2)
    )
    return members


def _biases(n_linear_layers: int):
    members = tuple(
        tuple(np.zeros(2, dtype=np.float32) for _ in range(n_linear_layers))
        for _ in range(2)
    )
    return members


def test_rejects_single_hidden_layer():
    with pytest.raises(ValueError, match="exactly 2 hidden layers"):
        LearnedDoubleIntegratorDynamics(
            ensemble_weights=_weights(2),
            ensemble_biases=_biases(2),
            input_mean=np.zeros(3, dtype=np.float32),
            input_scale=np.ones(3, dtype=np.float32),
        )


def test_rejects_three_hidden_layers():
    with pytest.raises(ValueError, match="exactly 2 hidden layers"):
        LearnedDoubleIntegratorDynamics(
            ensemble_weights=_weights(4),
            ensemble_biases=_biases(4),
            input_mean=np.zeros(3, dtype=np.float32),
            input_scale=np.ones(3, dtype=np.float32),
        )


def test_accepts_two_hidden_layers():
    dynamics = LearnedDoubleIntegratorDynamics(
        ensemble_weights=_weights(3),
        ensemble_biases=_biases(3),
        input_mean=np.zeros(3, dtype=np.float32),
        input_scale=np.ones(3, dtype=np.float32),
    )
    assert len(dynamics.weights) == 2
