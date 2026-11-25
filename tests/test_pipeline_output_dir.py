"""run_pipeline honours an explicit output directory instead of results/sweeps."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_output_dir_flag_is_accepted():
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "run_pipeline.py"), "--help"],
        capture_output=True,
        text=True,
        timeout=120,
    )
    assert result.returncode == 0
    assert "--output-dir" in result.stdout


def test_run_pipeline_writes_to_given_output_dir(tmp_path):
    from scripts.run_pipeline import run_pipeline

    config = tmp_path / "tiny.yaml"
    config.write_text(
        "\n".join(
            [
                "experiment: E1",
                "system: double_integrator",
                "state_lo: [-1.0, -2.0]",
                "state_hi: [3.0, 2.0]",
                "umax: 1.0",
                "dt: 0.05",
                "trajectory_steps: 2",
                "horizon: 0.2",
                "grid_size: 11",
                'accuracy: "low"',
                "seed: 0",
                "seeds: [0, 1]",
                "split_seed: 42",
                "data_sizes_trajectories: [1]",
                "val_trajectories: 1",
                "test_trajectories: 1",
                "derivative_observation_noise_std: 0.0",
                "coverage_gap: {enabled: false, lo: [0.4, -2.0], hi: [1.0, 2.0]}",
                "gap_conditions: [true]",
                "model: {type: ensemble_mlp, members: 2, hidden_sizes: [8, 8], epochs: 1, learning_rate: 0.002}",
                "inflation_k_values: [0.0]",
            ]
        ),
        encoding="utf-8",
    )
    out = tmp_path / "out"
    run_pipeline(config, output_dir=out)
    assert (out / "sweep_summary.json").exists()
