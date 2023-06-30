# drones-consumer-privacy

This repository includes data and code used to conduct a discrete mode choice experiment.

A survey was designed with hundreds of choice questions. The data collected is then used to design and calibrate model choice models.


## Data collection

Data was collected via a Qualtrics survey.
Link to survey preview: https://mit.co1.qualtrics.com/jfe/preview/previewId/f3158b16-5eeb-4088-925e-ecfa997bd4a4/SV_6mmF0a0AcjAgoqq?Q_CHL=preview&Q_SurveyVersionID=current


### Choice question generation

Choice questions were generated programmatically and then imported into Qualtrics.

See survey-questions/


## Data

The raw data directly exported from Qualtrics is not made publicly accessible.
This raw data is preprocessed and the cleaned resulting data is made publicly accessible.

The data collection and (de-identified) publication was approved by the MIT IRB (E-3924).

### Preprocessing

The preprocessing step removes Prolific IDs (potentially identifying info) and drops responses from participants whose data should be excluded (e.g. failed attention checks, tests from us, did not complete survey).

Preprocessing: data-analysis/preprocess-survey-data.ipynb

Preprocessed data (public): data/sample-preprocessed.csv

#### Fields
Metadata containing fields used in analysis are saved (excluding all choice questions) in data/fields.csv

Note that only the fields/columns prefixed by `Q` or `CHOICE` are questions. 
The following fields are for embedded data set by us in the survey logic:
```
'PROLIFIC_PID',
'STUDY_ID',
'online_shopping',
'takeout_food_delivery',
'online_groceries',
'prescription_medications_delivery',
'last_minute_groceries_delivery',
'liquor_store_delivery',
'questions_asked'
```
Others are automatically created by Qualtrics.

### Further data transformation for analysis

The preprocessed data is 'wide' data. It contains a row for each participant, with every question. Note many questions were not shown to participants (shown <=12 of 800 choice questions) and are therefore empty.

We transform the 'wide' data to 'long' data to be used in the choice models.

See data-analysis/transform-survey-data-for-choice-modeling.ipynb

## Choice models

We develop a choice model for each vendor type in a separate notebook. 

See data-analysis/mode-choice-models-v[0,1,2,3].ipynb

where vendors are:
- v0: Take-out food
- v1: prescription medications
- v2: liquor store
- v3: last-minute groceries

For more information on attribute levels, see: survey-questions/attributes.py
