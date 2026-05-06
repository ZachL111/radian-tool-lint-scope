# radian-tool-lint-scope

`radian-tool-lint-scope` keeps a focused Python implementation around cli tools. The project goal is to package a Python local lab for lint analysis with round-trip fixtures, lossless normalization checks, and documented operating limits.

## Purpose

The project exists to keep a narrow engineering decision visible and testable. For this repo, that decision is how file span and argument risk should influence a review result.

## Radian Tool Lint Scope Review Notes

For a quick review, compare `terminal width` with `file span` before reading the middle cases.

## What Is Covered

- `fixtures/domain_review.csv` adds cases for file span and terminal width.
- `metadata/domain-review.json` records the same cases in structured form.
- `config/review-profile.json` captures the read order and the two review questions.
- `examples/radian-tool-lint-walkthrough.md` walks through the case spread.
- The Python code includes a review path for `terminal width` and `file span`.
- `docs/field-notes.md` explains the strongest and weakest cases.

## Implementation Notes

The fixture data drives the tests. The code stays thin, while `metadata/domain-review.json` and `config/review-profile.json` explain what each case is meant to protect.

The Python implementation avoids hidden state so fixture changes are easy to reason about.

## Command

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/verify.ps1
```

## Audit Path

The same command runs the local verification path. The highest-scoring domain case is `stress` at 217, which lands in `ship`. The most cautious case is `baseline` at 153, which lands in `ship`.

## Limits

The repository is intentionally scoped to local checks. I would expand it by adding adversarial fixtures before adding features.
