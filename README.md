# Predicting Employee Attrition Using Machine Learning

Master’s thesis project · Business Informatics · Double Degree FH Technikum Wien / ITBA
Author: Edison Polackal

This repository contains the data, documentation and (later) the code for an interactive, explainable HR risk dashboard that predicts employee attrition at segment and individual level. This first version documents **data availability and suitability** as required before the thesis starts.

## Research questions

**Main research question:** How must an interactive, ML-supported HR dashboard be designed so that HR managers can identify employee segments at risk of attrition early and comprehensibly and derive retention measures from them?

| Sub-question | Data needed | Covered by the dataset |
| --- | --- | --- |
| **SQ1** (empirical): How does a cost-based classification threshold, derived from an explicit cost matrix for false negatives and false positives, change the practical utility of the selected model compared with the default threshold of 0.5, and how robust is it to the cost assumptions? | Labelled target, predictive features, salary information for the cost of a false negative | Yes: `Attrition` (binary), 30 usable features, `MonthlyIncome` |
| **SQ2** (design-oriented): Which requirements do HR users place on an attrition dashboard? | Realistic HR attributes to discuss with practitioners; segment variables | Yes: `Department`, `JobRole`, `OverTime`, satisfaction scales, tenure |
| **SQ3** (evaluative): How do HR users assess the usability and perceived value of the prototype? | Data for realistic task scenarios in the prototype | Yes: complete, anonymous records for all four dashboard views |

SQ2 and SQ3 additionally use primary data from 3–5 interviews with HR practitioners; these are collected during the thesis with informed consent and are not published here.

## Dataset

| Item | Details |
| --- | --- |
| Name | IBM HR Analytics Employee Attrition & Performance (IBM, 2015) |
| Source | [Kaggle](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset); copy from IBM’s repository [IBM/employee-attrition-aif360](https://github.com/IBM/employee-attrition-aif360) |
| Mirrors | OpenML (ID 43696); R package `modeldata` (`attrition`) |
| Licence | Database: ODbL v1.0 · Contents: DbCL v1.0 (see [`data/README.md`](data/README.md)) |
| Access | **Secured.** Public, no registration or approval needed. The file is stored in this repository (`data/raw/`) and verified by SHA-256 checksum. |
| Size | 1,470 records × 35 attributes |
| Target | `Attrition`: 237 Yes / 1,233 No (16.1 %) |
| Completeness | 0 missing values, 0 duplicate rows, unique employee IDs |
| Documentation | [`data/DATA_DICTIONARY.md`](data/DATA_DICTIONARY.md), [`reports/data_quality_report.md`](reports/data_quality_report.md) |

### Quality checks performed

- Structure, completeness and duplicates: no issues found.
- Three constant columns (`EmployeeCount`, `Over18`, `StandardHours`) and the identifier (`EmployeeNumber`) carry no information and are removed → 30 usable features.
- Class imbalance: 16.1 % attrition. A naive model that always predicts “No” reaches 83.9 % accuracy, so F1, precision, recall, AUC-ROC and PR-AUC are used instead.
- A stratified 20 % holdout set would contain only ≈ 47 leavers, so model selection uses repeated stratified 5 × 5 cross-validation.
- `PerformanceRating` only takes the values 3 and 4.

### Limitations

- **Fictional data** created by IBM data scientists: results show feasibility and design knowledge, not real-world attrition rates. External validity is limited.
- **Cross-sectional:** no time stamps, so no time-to-leave prediction.
- **Small minority class** (237 leavers): metrics are reported as mean ± standard deviation across folds.
- **Sensitive attributes** (`Age`, `Gender`, `MaritalStatus`): their effect and the option to exclude them are discussed (fairness, GDPR Art. 22, EU AI Act). No causal statements about reasons for leaving are made.

## Reproduce the data checks

Requires Python 3.11 or newer.

```bash
pip install -r requirements.txt
python scripts/download_data.py        # verifies (or restores) the raw file
python scripts/data_quality_report.py  # regenerates reports/data_quality_report.md
```

## Repository structure

```
data/
  raw/                 original dataset (unchanged)
  processed/           empty: preprocessing runs inside the CV folds
  DATA_DICTIONARY.md   all 35 attributes with roles and codings
scripts/               data download and quality report
src/pipeline/          ML pipeline (planned)
src/app/               Streamlit dashboard (planned)
notebooks/             exploratory analysis (planned)
models/                trained models (planned)
reports/               generated reports
```

## Planned methods

Design Science Research (Hevner et al., 2004; Peffers et al., 2007) as framework, CRISP-DM for the data analysis, FEDS for the evaluation (Venable et al., 2016). Models: logistic regression, random forest and XGBoost, each without correction, with SMOTE and with class weighting, followed by a cost-based threshold analysis. Explanations with SHAP; prototype in Streamlit.
