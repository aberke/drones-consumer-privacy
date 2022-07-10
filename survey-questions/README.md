# Making Qualtrics survey questions

We programatically create the choice sets and Qualtrics Questions.

Steps:

## 1. Define attributes

Define attributes for the choice sets.

## 2. Generate choice sets.

Use the defined attributes to generate choice sets in a CSV from which well formatted Questions will be generated.

Each row represents a choice between a ground vehicle delivery option and a drone delivery option.

A full factorial experiment is generated and then reduced to a fractional experiment design.

Note: Reducing to small subset of choices (likely smaller than otherwise "efficient design") is necessary in order to work within Qualtrics.

Input: Attributes

Output: CSV defining choice sets

## 3. Generate Qualtrics Questions

Qualtrics has a way to generate Questions/Blocks/Entire surveys for import via their 'AdvancedFormat' .txt files.

See 
https://www.qualtrics.com/support/survey-platform/survey-module/survey-tools/import-and-export-surveys/#ImportTXTDoc

Each of the choice sets (rows) defined in the CSV from step 2 are used to create a question.

A script then does 2 main things when:

1. Generates nicely formatted Qualtrics Questions.



2. Encodes attributes / data for each choice set into Questions.

This is to better enable data analysis when data is exported with Question IDs and corresponding (numeric) response codes.


### Script to make qualtrics questions

`generate-questions.py`

example usage:
```
$ python survey-questions/generate-questions.py survey-questions/choice-sets/v0-sampled-100.csv
```

### Encoding choice attributes/data into questions

The script encodes attributes into Question IDs.
 - e.g. Question ID: Q_v1_gc1_gt1_dc1_dt1_dp1 correspond to parameters:
    - vendor type: 1
    - ground vehicle fee: 1
    - ground vehicle time: 1
    - drone fee: 1
    - drone time: 1
    - drone privacy: 1

Answers are 'recoded'
- 0: ground vehicle
- 1: drone
- Note: Use "numeric" data export from Qualtrics to get answer codes.


#### Formatting notes:
Can do the following
- put tables into any part of the questions or answers
- put CSS anywhere into a question that modifies our added HTML as well as Qualtrics styles
    - careful: CSS will globally apply to the questions shown on current page (not necessarily for other questions in the block if there is a page break.)
- insert images from our qualtrics library into questions


## 4. Import Survey questions

Import the AdvancedFormat .txt from (3) into Qualtrics and go from there, applying additional survey logic.

## Qualtrics gotcha's:

- The "Preview" view does not always look like the "Publish" view. This is particularly the case on mobile.
- A good debug / testing technique: Have a scratch/test copy of the survey that you do all tests in. Publish all changes and view.


## Survey versions


### version: ICRAT 
There was a separate "ICRAT" version of the survey where we tested ideas at ICRAT (conference).

[preview](https://mit.co1.qualtrics.com/jfe/preview/SV_5hcBQuYS69mUgVo?Q_CHL=preview&Q_SurveyVersionID=current)




