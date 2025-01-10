# Drone delivery and the value of customer privacy: A discrete choice experiment with U.S. consumers

This repository includes data and code used in our analysis: "Drone delivery and the value of customer privacy: A discrete choice experiment with U.S. consumers".

A survey was designed for a discrete choice experiment with hundreds of choice questions. The collected data collected is used to calibrate model choice models.

The data also contains useful information about use of delivery services by different demographics and for different product types. See below.

You are welcome to use our data, code and methodology. Please cite as: 

> Alex Berke, Geoffrey Ding, Christopher Chin, Karthik Gopalakrishnan, Kent Larson, Hamsa Balakrishnan, Max Z. Li, Drone delivery and the value of customer privacy: A discrete choice experiment with U.S. consumers, Transportation Research Part C: Emerging Technologies, Volume 157, 2023, 104391, ISSN 0968-090X, https://doi.org/10.1016/j.trc.2023.104391.

### Abstract

_Drone delivery services are becoming increasingly available, but they introduce new consumer privacy risks. As a result of safety regulations that require drones to broadcast their locations, third-party observers may link customers to their purchases by following a delivery from vendor to customer. These privacy risks can be reduced with routing strategies that aggregate customer orders, at the potential cost of additional delivery wait times or fees. This study measures the importance of these privacy risks to delivery service customers, their willingness to pay for privacy, and how this differs across consumer groups and product types. We developed a discrete choice experiment and mode choice logit models using data from over 3700 U.S. consumers who chose between ground vehicle versus drone delivery across a range of privacy, delivery fee, and wait time options. Preferences were tested for various product types: take-out food, liquor store items, groceries, and prescription medications. Results show offering privacy enhancements significantly increased consumers’ likelihood of choosing drone delivery. Without privacy enhancements, when fees and wait times were the same, consumers chose ground vehicle 4 times more often than drone. Offering privacy for the drone option closed this gap. Yet preferences differ by demographic group. Males and frequent e-commerce users were more likely to prefer drone regardless of privacy, while privacy improvements had a significantly larger impact on females and younger consumers. We measured consumers’ value of privacy in both money and time. The value of privacy for medications delivery was about twice that for other product types. The value of privacy was then highest for liquor store items, then groceries, then take-out food. Our results can inform delivery service planning as well as contribute to a broader understanding of how consumers value privacy and methods to measure that valuation._


Data collection and (de-identified) publication was approved by the MIT IRB (E-3924).

## Data collection

Our survey instrument was designed to conduct a discrete mode choice experiment.

Data was collected via a Qualtrics survey.
Link to survey preview: https://mit.co1.qualtrics.com/jfe/preview/previewId/f3158b16-5eeb-4088-925e-ecfa997bd4a4/SV_6mmF0a0AcjAgoqq?Q_CHL=preview&Q_SurveyVersionID=current

See the [flowchart](survey-flowchart.jpg) and [survey PDF](survey.pdf) for a summary of the survey design and questions.


### Choice question generation

Choice questions were generated programmatically and then imported into Qualtrics.

See survey-questions/


## Data

The raw data directly exported from Qualtrics is not made publicly accessible.
This raw data is preprocessed and the cleaned resulting data is made publicly accessible.
Note the data is available as wide data, with one row per respondent.

- Data: `/data/sample-preprocessed.csv`
- Data fields and question text: `/data/fields.csv`
- The codebook can be used to map data to readable questions and answers: `/data-analysis/codebook.py`


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
