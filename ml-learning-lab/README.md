# Machine Learning Learning Lab 🐝

A personal learning repository for building **strong Machine Learning foundations** before applying them to **HiveWhisper** (a smart beehive monitoring project).

> **Status:** Learning notes and small exercises. This is **not** a finished or validated ML application.

## Learning progress

| Day | Topic | Theory | Practice | Notes |
| --- | --- | --- | --- | --- |
| 01 | How Models Work / Decision Trees | Started | Not completed | Thresholds and validation need review |

## Repository structure

```text
ml-learning-lab/
├── README.md
├── .gitignore
├── requirements.txt
├── notes/
│   └── day_01_how_models_work.py
└── practice/
    └── day_01_decision_tree.py
```

- `notes/`: Notes written as Python comments to read inside VS Code.
- `practice/`: Small, separate Python exercises. Files marked as a **starter** are not completed assignments.

## Day 1 — How Models Work

Topics discussed:
- Learning patterns from historical data
- Features (`X`) and targets (`y`)
- Regression decision trees, splits, and leaves
- Why a split is chosen based on training error
- Difference between **sum of squared errors (SSE)** and **mean squared error (MSE)**

**To revisit next session:** Why a threshold can be `3.5` even for integer bedroom counts; training error vs. validation error; then complete and explain the Python exercise.

### Source
[Kaggle — Introduction to Machine Learning: How Models Work](https://www.kaggle.com/learn/intro-to-machine-learning/how-models-work)

## Optional: Run the starter exercise

Install Python, then in the project folder:

```bash
python -m pip install -r requirements.txt
python practice/day_01_decision_tree.py
```

The code in `practice/` is **prepared for the next study session**, not claimed as work already completed.

## Study rule

Learn the concept, try it yourself, then explain the result in your own words. Do not mark practice as complete until you have actually run and understood it.
