# Group Matcher
Repo dedicated to hosting all code and files associated with grouping students into groups based on configurable constraints and CSV format.

## Example usage:
With Python 3.x installed, run:

`python run.py configs/group_matching_template.py /path/to/matching_form_responses.csv`

## Steps for Running the Algorithm

### Outline of the group match process
* Data cleaning and preprocessing
* Running the algorithm
* Post Processing

### Cleaning & Preprocess:
* Make sure that the column names in your input CSV match or contain the strings in the corresponding Column objects in the ROW_CONFIG. If needed, we recommend changing the column names in the CSV directly.
* Make sure students who fill out that they have existing partners (“yes”) actually have written partners in the form, or else the matched results will have them as singletons.

### Running the algorithm
#### Algorithm settings / Modifying the Config File: 
The following modifications should be made in your configuration file. The config file needs to reflect any changes made to your survey. An example config file can be found in the Github repo.

First, modify the CONSTRAINTS settings to what we want to prioritize: 
Update the "Partition" entry (around line 290 of the config) in the CONSTRAINTS dictionary to reflect the ordering of criteria that you would like to prioritize matching students on. This is the order that the algorithm will partition the students on. For example, given the current Fall 2023 config, the algorithm will first partition on year, then location, then homework start time, etc., as we wanted to prioritize matching students of the same graduation year first.

Modify group size parameters: 
Adjust the MIN_GROUP_SIZE and MAX_GROUP_SIZE parameters until you are satisfied with the final group sizes in the output CSV file.

If the form is modified from fa23 template, modify the config:
If you added new questions to the survey, make sure to include them as a new entry in the ROW_CONFIG, and optionally create a new transformer method that will bucket that question's options.

Run script: `python run.py example-config.py data/responses_clean.csv`
* We use example-config.py config file, which is the main thing that we make changes. 
* data/responses_clean.csv is your cleaned google form dataset. 

### Post Processing
Make some manual spot checks. The algorithm should do what it is supposed to do. Make sure the following doesn’t happen: 
1. A student is the only race/gender in a given group
2. Check for singletons (1 person in a group), add them to existing groups
3. Manually modify groups if necessary
