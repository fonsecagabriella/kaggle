# 🏁 Kaggle Competition: Predicting Heart Disease

- **Competition:** [Playground Series - Season 6, Episode 2: Predicting Heart Disease](https://www.kaggle.com/competitions/playground-series-s6e2)
- **Goal:** Predict whether a patient has heart disease (**binary classification**)
- **Metric:** **ROC-AUC**
- **Main notebooks:** [`00_ead.ipynb`](./00_ead.ipynb), [`01_experiments.ipynb`](./01_experiments.ipynb), [`02_final_experiments.ipynb`](./02_final_experiments.ipynb)

---

## 🧮 Final Results

| Item | Result |
|------|--------|
| **Best public leaderboard score** | **0.95374** |
| **Best private leaderboard score** | **0.95522** |
| **Best local score (OOF / CV AUC)** | **0.955577** |
| **Final selected submission 1** | `submission_ca_xgb_blend_w_50_full_data.csv` |
| **Final selected submission 1 scores** | Public **0.95374** \| Private **0.95522** |
| **Final selected submission 2** | `submission_stack_feature_aware_without_TE.csv` |
| **Final selected submission 2 scores** | Public **0.95371** \| Private **0.95517** |
| **Gap to the top final private score** | **0.00013**, about 0.0136% lower |
|**Relative standing**| Top 16% (690/4371)|


➡️ One of the main lessons from this competition was that the **highest local score did not automatically give the best final result**. Some more advanced stacks and hill-climbing runs improved OOF very slightly, but the best final selected submission came from a relatively simple CatBoost + XGBoost blend trained on the merged dataset.

---

## 🧠 Summary of My Approach

### 1. Exploratory Data Analysis (EDA)
Notebook: [`00_ead.ipynb`](./00_ead.ipynb)

I started by understanding the structure of the synthetic heart disease dataset and separating features into:
- **Numerical:** `age`, `bp`, `cholesterol`, `max_hr`, `st_depression`, `number_of_vessels_fluro`
- **Categorical:** `sex`, `fbs_over_120`, `exercise_angina`, `chest_pain_type`, `ekg_results`, `slope_of_st`, `thallium`

Main EDA steps:
- Checked data types, distributions, and possible outliers
- Looked at the target distribution
- Compared numerical features against the target
- Compared categorical features against the target
- Computed correlations and feature relevance
- Listed domain-inspired risk patterns for later feature engineering

**Main EDA insight:** the strongest signals seemed to come from variables such as **chest pain type**, **ST depression**, and **number of vessels fluoroscopy**, while variables such as **blood pressure** and **cholesterol** were less informative than expected in this synthetic setting.

---

### 2. Baselines and First Strong Models
Still in the first notebook, I tested simpler models before moving to tuning.

Some early local results:
- **Random Forest:** CV ROC-AUC ≈ **0.9472**
- **Gradient Boosting Classifier V1:** CV ROC-AUC ≈ **0.9542**
- **Logistic Regression:** CV ROC-AUC ≈ **0.9529**
- **CatBoost:** CV AUC ≈ **0.95540**
- **LightGBM:** CV AUC ≈ **0.95511**
- **XGBoost:** CV AUC ≈ **0.95523**

This established very early that **tree boosting** was the right direction.

---

### 3. Feature Engineering
Across the notebooks, I experimented with both manual and model-driven feature ideas, including:
- Interaction terms such as `age_x_maxhr`, `chol_x_age`, `bp_x_age`
- Domain-inspired combinations such as `vessels_x_thallium` and `stdep_x_angina`
- Low-risk subgroup logic
- Target encoding experiments for selected categorical patterns

This was useful, but it also showed a limit: in a **synthetic medical dataset**, feature engineering can help, but ideas that look medically reasonable do **not** necessarily improve leaderboard performance.

---

### 4. Model Tuning and Experimentation
Notebook: [`01_experiments.ipynb`](./01_experiments.ipynb)

The experimentation phase focused mostly on **CatBoost** and **XGBoost**.

What I explored:
- CatBoost parameter searches and variants
- XGBoost shallow configurations
- Seed ensembling
- Weighted blends
- Slice analysis for errors and subgroup performance
- SHAP-based inspection for CatBoost
- Logistic-regression and ridge-style meta-models
- A small neural-network baseline through **RealMLP**

At this stage, the project became less about finding a completely different algorithm and more about **stability, validation, and blend quality**.

---

### 5. Adding More Data
Notebook: [`02_final_experiments.ipynb`](./02_final_experiments.ipynb)

One of the most important decisions in the competition was to **merge the synthetic Kaggle training set with the original heart disease dataset**.

- Kaggle training rows: **630,000**
- Combined training rows: **630,270**

This gave a small but useful lift and reinforced a good Kaggle principle: **when extra data is compatible, it is worth testing**.

---

### 6. Final Models
The main final candidates were:
- **CatBoost V4** with seed ensemble
- **XGBoost shallow** with seed ensemble
- **CatBoost with target encoding**
- **XGBoost with target encoding**
- **RealMLP**
- **Simple weighted blends**
- **Hill-climbing ensemble**
- **Ridge / logistic stacking**
- **Feature-aware meta-models**

What stood out most was how close the best models were. CatBoost and XGBoost were both strong, and their predictions were highly correlated. That meant many later improvements were very small and often close to leaderboard noise.

---

## 📊 Local vs Leaderboard Scores

This table combines the **local notebook scores** I tracked during experimentation with the **public/private leaderboard scores** visible in [my Kaggle submission history screenshots](./imgs/).

| Model / submission | Local score | Public LB | Private LB | Notes |
|------|-------------|----------|-----------|-------|
| CatBoost V4 (4 seeds, original data) | 0.955478 | 0.95369 | 0.95520 | Strong single-model baseline |
| CatBoost V4 (4 seeds, merged data) | 0.955533 | 0.95369 | 0.95520 | Slight local gain after adding original data |
| CatBoost TE (`submission_catboost_te.csv`) | 0.955468 | 0.95363 | 0.95516 | Competitive, but not better than plain CatBoost |
| XGBoost shallow (4 seeds, original data) | 0.955381 | 0.95368 | 0.95515 | Very close to CatBoost |
| XGBoost shallow (4 seeds, merged data) | 0.955519 | 0.95369 / 0.95367 | 0.95516 / 0.95517 | Small lift from added data |
| XGBoost TE (`submission_xgb_shallow_te_full_data.csv`) | 0.955483 | 0.95226 | 0.95345 | Good local score, weak leaderboard transfer |
| RealMLP (`submission_realmlp_full_data_auc_opt.csv`) | 0.953321 | 0.95164 | 0.95322 | Useful learning experiment, not competitive |
| Hill-climb ensemble (`submission_hillclimb_blend_full_data.csv`) | 0.955577 | 0.95365 | 0.95505 | Local gain did not generalize |
| Ridge stack (`submission_ridge_stack_full_data.csv`) | 0.955577 | 0.95359 | 0.95498 | Best local-type result, weaker leaderboard |
| Ridge stack Cat + XGB (`submission_ridge_stack_cat_xgb_full_data.csv`) | — | 0.95374 | 0.95522 | Tied best public and private among visible submissions |
| Stacked logistic regression (`submission_stacked_logreg.csv`) | — | 0.95373 | 0.95522 | Very close to best blend |
| Feature-aware stack (`submission_stack_feature_aware.csv`) | — | 0.95374 | 0.95519 | Strong public score |
| Feature-aware stack without TE (`submission_stack_feature_aware_without_TE.csv`) | — | 0.95371 | 0.95517 | One of the two final selected submissions |
| **CatBoost + XGBoost blend 50/50 (`submission_ca_xgb_blend_w_50_full_data.csv`)** | **0.955572** | **0.95374** | **0.95522** | **Best final selected submission** |
| Cat + XGB + RealMLP blend (`submission_blend_cat0.60_xgb0.40_rmlp0.02.csv`) | — | 0.95372 | 0.95522 | Tiny improvement locally did not clearly separate |
| Logit / weighted blends (multiple versions) | — | 0.95372–0.95373 | 0.95520–0.95522 | Many variants converged to nearly the same region |

---

## 📈 Progression During the Project

- Started with standard baselines to understand the competition before tuning.
- Reached about **0.9542** with Gradient Boosting and **0.9529** with Logistic Regression.
- Confirmed quickly that **CatBoost / XGBoost** were the strongest direction, both around **0.9552–0.9554** locally.
- Learned to rely much more on **OOF / CV** instead of isolated holdout impressions.
- Added **manual feature engineering**, but saw that some ideas helped little or even hurt on this synthetic dataset.
- Tested **seed ensembles**, which improved stability and reduced variance.
- Merged the Kaggle dataset with the original data, pushing the strongest single-model local scores to around **0.9555**.
- Explored **RealMLP** for diversity; useful educationally, but not competitive enough here.
- Tried stacking, hill climbing, logit blends, and feature-aware meta-models; these often improved local AUC by tiny amounts but did **not** produce a clearly better private score.
- Finished with two selected submissions, with the best one scoring **0.95374 public / 0.95522 private**.

---

## ✅ What Worked Well

- Comparing models directly instead of overcommitting too early
- Using **OOF predictions** to compare models more reliably
- Trusting CV more as the project progressed
- Adding more compatible data instead of only tuning parameters
- Using **seed ensembles** to reduce variance
- Starting to use **MLflow**
- Using **MLflow** to inspect and study specific models more closely
- Going deeper on a few promising model families instead of testing everything superficially

---

## ⚠️ What Could Be Better

- **Naming conventions** for runs and submissions should have been stricter
- More code should have been turned into **functions** instead of running notebook cells out of order
- MLflow logging started well, but consistency dropped later in the competition
- Documentation in the middle of the project could have been cleaner
- Too many late-stage blends were probably too correlated to add real value

---

## 🧭 Main Lessons Learned

- **OOF matters.** This was one of the most important ideas I improved in this competition.
- **Trust CV**, but treat very small gains with caution.
- **Adding data can matter more than clever tuning.**
- **Feature engineering is not automatically good.** In synthetic datasets, it can drift away from the hidden generating process.
- **Seed ensembling reduces variance** and can be a practical improvement when strong models are close.
- **Trying a new architecture was worthwhile.** RealMLP did not win here, but it expanded my understanding of tabular modelling.
- **Hyperparameter optimisation helps, but it is not magic.** It refines a strong setup; it does not replace reasoning.
- It is often better to **look closely at one promising model family** than to rely only on broad automated search.
- A useful rule from experienced Kagglers is to tune parameters **early** to find a good region and **again near the end** when the pipeline is stable.

---

## 🔧 What I Would Improve Next Time

- Keep a cleaner experiment tracker from day one
- Use a stricter run and submission naming system
- Log all important runs consistently in **MLflow**
- Separate exploration, validated experiments, and final submissions more clearly
- Record every submission with notebook version, feature set, and blend recipe
- Turn repeated notebook logic into reusable functions earlier
- Spend less time chasing tiny gains between highly correlated models
- Push harder on **model diversity** if I want ensembles to matter

---

## 🧰 Libraries & Tools

- **Python**
- **Pandas**, **NumPy**
- **Scikit-learn**
- **CatBoost**
- **XGBoost**
- **LightGBM**
- **PyTorch / RealMLP**
- **Matplotlib**, **Seaborn**
- **MLflow**

---

## 🔍 Next Things Worth Exploring

- Better diversity in ensembles instead of stacking highly similar models
- More disciplined use of **logit-space blending**
- Better experiment tracking from the first day
- More deliberate testing of feature families instead of one-off ideas
- A reusable competition template with: **EDA → baseline → OOF → model comparison → submission log**
