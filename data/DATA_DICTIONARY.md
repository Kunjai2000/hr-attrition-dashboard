# Data dictionary

IBM HR Analytics Employee Attrition & Performance – 1,470 records, 35 attributes.
Value ranges are observed in `data/raw/WA_Fn-UseC_-HR-Employee-Attrition.csv`.
Codings of the ordinal scales follow the dataset description on Kaggle.

**Role:** `target` = variable to predict · `feature` = model input · `drop` = removed before modelling (constant or identifier) · `sensitive` = feature that requires a fairness discussion.

| Column | Type | Observed values | Role | Description |
| --- | --- | --- | --- | --- |
| Age | integer | 18–60 | feature, sensitive | Age in years |
| Attrition | categorical | No, Yes | **target** | Employee left the company |
| BusinessTravel | categorical | Non-Travel, Travel_Rarely, Travel_Frequently | feature | Frequency of business travel |
| DailyRate | integer | 102–1499 | feature | Daily rate (unit not documented) |
| Department | categorical | Human Resources, Research & Development, Sales | feature | Department; used for segment views |
| DistanceFromHome | integer | 1–29 | feature | Distance between home and workplace (unit not documented) |
| Education | ordinal | 1–5 | feature | 1 Below College, 2 College, 3 Bachelor, 4 Master, 5 Doctor |
| EducationField | categorical | 6 fields | feature | Field of education |
| EmployeeCount | integer | 1 | drop | Constant |
| EmployeeNumber | integer | 1–2068 (unique) | drop | Employee identifier |
| EnvironmentSatisfaction | ordinal | 1–4 | feature | 1 Low, 2 Medium, 3 High, 4 Very High |
| Gender | categorical | Female, Male | feature, sensitive | Gender |
| HourlyRate | integer | 30–100 | feature | Hourly rate (unit not documented) |
| JobInvolvement | ordinal | 1–4 | feature | 1 Low, 2 Medium, 3 High, 4 Very High |
| JobLevel | ordinal | 1–5 | feature | Job level |
| JobRole | categorical | 9 roles | feature | Job role; used for segment views |
| JobSatisfaction | ordinal | 1–4 | feature | 1 Low, 2 Medium, 3 High, 4 Very High |
| MaritalStatus | categorical | Single, Married, Divorced | feature, sensitive | Marital status |
| MonthlyIncome | integer | 1009–19999 | feature | Monthly income; basis for the cost of a false negative in the cost matrix |
| MonthlyRate | integer | 2094–26999 | feature | Monthly rate (unit not documented) |
| NumCompaniesWorked | integer | 0–9 | feature | Number of previous employers |
| Over18 | categorical | Y | drop | Constant |
| OverTime | categorical | No, Yes | feature | Works overtime |
| PercentSalaryHike | integer | 11–25 | feature | Last salary increase in percent |
| PerformanceRating | ordinal | 3–4 | feature | 1 Low, 2 Good, 3 Excellent, 4 Outstanding; only 3 and 4 occur |
| RelationshipSatisfaction | ordinal | 1–4 | feature | 1 Low, 2 Medium, 3 High, 4 Very High |
| StandardHours | integer | 80 | drop | Constant |
| StockOptionLevel | ordinal | 0–3 | feature | Stock option level |
| TotalWorkingYears | integer | 0–40 | feature | Total years of work experience |
| TrainingTimesLastYear | integer | 0–6 | feature | Number of trainings last year |
| WorkLifeBalance | ordinal | 1–4 | feature | 1 Bad, 2 Good, 3 Better, 4 Best |
| YearsAtCompany | integer | 0–40 | feature | Years at the company |
| YearsInCurrentRole | integer | 0–18 | feature | Years in the current role |
| YearsSinceLastPromotion | integer | 0–15 | feature | Years since the last promotion |
| YearsWithCurrManager | integer | 0–17 | feature | Years with the current manager |
