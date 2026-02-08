# 🏁 Kaggle Competition: Predicting Road Accident Risk

- **Timeframe:** October 2025 (≈1 month)  
- **Goal:** Predict a *road accident risk score* bounded between 0–1 (**Regression problem**)  
- **Competition:** [Playground Series S5E10](https://www.kaggle.com/competitions/playground-series-s5e10/overview)

---

## 🧮 Final Results

| Metric | My Score | Best Score | Relative |
|--------|-----------|-------------|-----------|
| **RMSE** | 0.05579 | 0.05563 | ✅ **99.7% of top performance** |
| **Leaderboard position** | **839 / 4,083** | — | **Top 20%** |
| **Difference from best** | +0.00016 RMSE | +0.2876% worse | — |

➡️ *My model’s predictions were only 0.00016 RMSE points away from the best model in the entire competition.*

---

## 🧠 Summary of My Approach

### 1. Exploratory Data Analysis (EDA)
Notebook: [`00_ead.ipynb`](./00_ead.ipynb)

- Inspected dataset with `.info()` and `.describe()`  
- Visualized **target distribution** and checked for skewness  
- Compared **categorical variables vs. target** via boxplots  
- Computed:
  - **Mutual Information** for categorical variables  
  - **Pearson correlation** for numeric features  
- Created **pairplots** for numeric interactions  
- Performed **train/test split before visualization** to avoid data leakage  

**Learnings:**  
EDA revealed several non-linear relationships and categorical clusters, motivating feature binning and interaction features later on.

---

### 2. Data Cleaning
- Checked for **null values** → none found  
- Verified data types and ranges for all features  
- Prepared consistent column naming for later feature engineering  

---

### 3. Experiment Tracking
- Set up **MLflow** locally to log experiments, parameters, and metrics  
- Logged every model run with:
  - Algorithm name
  - Hyperparameters
  - RMSE on validation set
  - Feature list and preprocessing pipeline

---

### 4. Baseline Models
Established performance benchmarks:
- **Linear Regression**
- **Random Forest Regressor**

These baselines helped evaluate whether further complexity actually improved RMSE.

---

### 5. Model Tuning with Hyperopt
Used **Hyperopt** for hyperparameter optimization of:
- `RandomForestRegressor`
- `Ridge`, `Lasso`, `ElasticNet`
- `GradientBoostingRegressor`
- Later extended to **CatBoost**, **LightGBM**, and **XGBoost**

Each run was logged in MLflow, allowing direct visual comparison.

---

### 6. Feature Engineering
Experimented with a wide range of transformations:
- ✅ **Aggregated accident risk features** (e.g., general risk score per condition)  
- ✅ **Binary indicators** (e.g., `is_speed_limit_over_45`)  
- ✅ **Polynomial and non-linear transformations**  
- ✅ **Ratios and interactions** (e.g., `weather × lighting`)  
- ✅ **Binned speed limits** (`very_low`, `low`, `medium`, `high`, `very_high`)

**Learnings:**  
Feature engineering had one of the biggest impacts on performance. Non-linear and interaction features helped gradient boosting models capture subtle dependencies.

---

### 7. Model Evaluation
- Used **RMSE** as main metric  
- Analyzed **residuals** and **predicted vs. true** plots  
- Checked model boundaries (predictions clipped between 0–1)  
- Compared training vs. validation RMSE for overfitting detection  

---

### 8. Preprocessing Pipeline
- Used **TargetEncoder** for categorical features  
- Applied **StandardScaler** to numerical columns  
- Combined with `ColumnTransformer` for reproducibility  

---

### 9. Ensemble Learning
Final performance came from **stacking and blending**:
- Base models: **CatBoost**, **LightGBM**, **Gradient Boosting**, **Ridge**, **KNN**  
- Final meta-model: **Ridge regression** on out-of-fold predictions  

This approach improved stability and slightly boosted RMSE.

---

## 🧰 Libraries & Tools
- **Scikit-learn**
- **Hyperopt**
- **XGBoost**
- **LightGBM**
- **CatBoost**
- **MLflow**
- **Pandas**, **NumPy**, **Matplotlib**, **Seaborn**

---

## 🌟 What Worked Well
- Strong improvement through **ensembling and stacking**
- Exploring **CatBoost and LightGBM** for the first time
- Tracking everything in **MLflow** simplified iteration
- **Feature engineering** made the biggest performance difference

---

## ⚠️ What Could Be Improved
- Didn’t use **cross-validation folds** → limited model stability
- Late start on **documentation and experiment logging**
- Some feature ideas were added too late to test extensively

---

## 🧭 Learnings for Future Competitions
- Start with a **baseline notebook template** (EDA → baseline → tracking)
- Document ideas continuously (simple Markdown notes are enough)
- Always use **folds or OOF validation** before ensembling
- Integrate MLflow or W&B tracking from day one
- Keep an “experimentation ideas” file at project root

---

## 🔍 For Future Exploration
- **TabM** regressors ([great notebook example](https://www.kaggle.com/code/masayakawamata/s5e10-single-tabm-tuned))  
- **Genetic programming for feature generation** – explore frameworks like [TPOT](https://epistasislab.github.io/tpot/)  
- **Hill-climbing / greedy feature selection** – meta-heuristic search for improved features  

---
