# Radian Tool Lint Scope Walkthrough

I use this file as a small checklist before changing the Python implementation.

| Case | Focus | Score | Lane |
| --- | --- | ---: | --- |
| baseline | file span | 153 | ship |
| stress | terminal width | 217 | ship |
| edge | argument risk | 174 | ship |
| recovery | report density | 163 | ship |
| stale | file span | 203 | ship |

Start with `stress` and `baseline`. They create the widest contrast in this repository's fixture set, which makes them better review anchors than the middle cases.

The useful comparison is `terminal width` against `file span`, not the raw score alone.
