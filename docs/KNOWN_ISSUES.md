# Known issues

Only verified issues are listed here. Each entry states what was checked and
where the evidence lives.

## 1. C0 and C2 are bit-identical in the stored S2 output

In `results/certifier_comparison/s2_full6_grid101_n10.json`, the C0 and C2
entries have exactly equal summary statistics and exactly equal per-seed
records (checked across all 10 per-seed records, not just the means). Their
`fuv_star_curve` is constant in both, which makes the AUPC reduce to the
penalty value in each case. Because the values are identical to the bit, the
stored output cannot distinguish the two certifiers; treat the C0/C2 comparison
as unresolved rather than as evidence that they agree by design.

## 2. FSV is a grid-cell count, so small disturbances can be invisible

FSV is computed as a fraction of grid cells (`src/lcert/metrics.py`), so a
small change in the learned disturbance bound can leave every cell on one side
of the safety threshold untouched and produce an identical FSV. The stored C0
vs C2 rows are an example: their `fuv_star_curve` is constant across the whole
control-ratio grid. Report FSV differences with this granularity in mind, and do
not read a zero change as proof that the underlying safety set did not move.

