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

