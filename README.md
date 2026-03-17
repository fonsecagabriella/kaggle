# 🏁 Kaggle Competitions

This repository is my central place to organize Kaggle competition work.

Each competition lives in its own folder and usually contains:
- exploratory data analysis
- experiments and model comparisons
- final training / submission notebooks
- a competition-specific `README`
- notes about what worked, what failed, and what I learned

The goal of this repository is not only to keep final scores, but also to document how my thinking evolves across competitions.

---

## 📂 Repository Structure

```text
.
├── README.md
├── 2025_10_predicting_road_accident_risk/
│   ├── README.md
│   ├── 00_ead.ipynb
│   ├── 01_experiments.ipynb
│   └── ...
└── 2026_02_prediciting_heart_disease/
    ├── README.md
    ├── 00_ead.ipynb
    ├── 01_experiments.ipynb
    ├── 02_final_experiments.ipynb
    └── ...
```

---

## 📘 Competition Log

| Date | Competition | Type | Metric | Result | Rank | Folder |
|------|-------------|------|--------|--------|------|--------|
| **2026-02** | **Predicting Heart Disease** | Binary classification | **ROC-AUC** | **0.95522 private / 0.95374 public** | **690 / 4,371** *(Top 16%)* | [`2026_02_prediciting_heart_disease/`](./2026_02_predicting_heart_disease/) |
| **2025-10** | **Predicting Road Accident Risk** | Regression | **RMSE** | **0.05579** | **839 / 4,083** *(Top 20%)* | [`2025_10_predicting_road_accident_risk/`](./2025_10_predicting_road_accident_risk/) |

---

## 🔎 Competition Summaries

### 2026-02 — Predicting Heart Disease
- Main lesson: **small local gains do not always translate to leaderboard gains**
- Strongest models: **CatBoost** and **XGBoost**
- Useful techniques: **OOF validation**, **seed ensembling**, **adding compatible external/original data**, **simple weighted blends**
- Final takeaway: trusting CV became more important than chasing tiny leaderboard differences

### 2025-10 — Predicting Road Accident Risk
- Main lesson: **feature engineering and ensembling can move the needle meaningfully in tabular regression**
- Strong areas explored: **stacking**, **blending**, **boosting models**, and **MLflow experiment tracking**
- Final takeaway: structured experimentation mattered as much as model choice

---

## 🧠 Cross-Competition Learnings

Across these projects, a few themes are becoming clear:
- **OOF / cross-validation is essential** for making reliable decisions
- **More data can matter more than more tuning**
- **Feature engineering is useful, but not automatically helpful**
- **Seed ensembling reduces variance** and can improve stability
- **Hyperparameter search helps refine a model, but does not replace reasoning**
- **Experiment tracking matters**; without naming discipline and logging, good ideas get lost

---

## 🛠 Current Workflow

My current competition workflow is converging toward:
1. **EDA**
2. **Simple baselines**
3. **OOF / CV validation**
4. **Model comparison**
5. **Feature engineering and extra data tests**
6. **Careful ensembling**
7. **Submission logging and retrospective notes**

Tools used most often so far:
- **Python**
- **Pandas / NumPy**
- **Scikit-learn**
- **CatBoost / XGBoost / LightGBM**
- **PyTorch** (when testing neural approaches)
- **MLflow**
- **Matplotlib / Seaborn**

---

## 🎯 Repository Goals

This repo is intended to help me:
- keep a clear history of competitions and results
- compare approaches across projects
- build reusable templates for future competitions
- improve the discipline of experimentation, tracking, and documentation

As more competitions are added, this page will serve as the top-level index.
