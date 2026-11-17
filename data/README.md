# Data

## Raw data

`raw/WA_Fn-UseC_-HR-Employee-Attrition.csv` – IBM HR Analytics Employee Attrition & Performance.

- **Creator:** IBM data scientists (fictional dataset)
- **Original publication:** Kaggle, <https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset>
- **Copy used here:** IBM’s public repository <https://github.com/IBM/employee-attrition-aif360> (`data/emp_attrition.csv`)
- **SHA-256:** `a5c31e38bd7fafc9bc333884eb181b06b41b8e5e488e8f7ccb27199fb3be7659`

## Licence

As stated in IBM’s repository:

- Database: [Open Database License (ODbL) v1.0](https://opendatacommons.org/licenses/odbl/1-0/)
- Contents: [Database Contents License (DbCL) v1.0](https://opendatacommons.org/licenses/dbcl/1-0/)

The file is redistributed unchanged with this attribution. Derived databases published from it fall under the ODbL as well.

## Processed data

`processed/` stays empty in the repository. All preprocessing (encoding, scaling, resampling) runs inside the training folds of the ML pipeline to avoid data leakage; no pre-processed files are stored.
