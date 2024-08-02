# Group Matcher
This is a repository dedicated to hosting all code and files associated with our group-matching system. For a brief overview of our system, please view this [document](https://docs.google.com/document/d/1fwjhMQp1gaulxNNvgjQUJKQdKne5pkpXNf0U4q5hxVY/edit?usp=sharing) or alternatively, overview.pdf.

PDF versions of our template surveys including the intake survey, reassignment survey, and final feedback survey can be found in this repo. If you have a Berkeley Google Drive account, you can access these surveys directly to make a copy at this [link](https://drive.google.com/drive/folders/1-IyhfElu9w_el7llScAWCOFn8QXDEmuH?usp=drive_link). Previous versions of our surveys and a detailed overview of the changes made to them over time can be found in the Surveys folder.

If you would like to learn more about our group-matching algorithm and its impact on students' educational experiences, see [1] and [2].

## Example usage:
With Python 3.x installed, run:

`python run.py example_config.py /path/to/matching_form_responses.csv`

## Steps for Running the Algorithm

### Outline of the group match process
* Data cleaning and preprocessing
* Running the algorithm
* Post Processing

### Cleaning & Preprocess:
* Make sure that the column names in your input CSV match or contain the strings in the corresponding Column objects in the ROW_CONFIG within your config file. If needed, we recommend changing the column names in the CSV directly.

### Running the algorithm
#### Algorithm settings / Modifying the Config File: 
The following modifications should be made in your configuration file. The config file needs to reflect any changes made to your survey. An example config file can be found in this repo (example_config.py). Below are some suggested config file modifications:

* Modify the CONSTRAINTS settings to match what you want to prioritize: Update the "Partition" entry in the CONSTRAINTS dictionary to reflect the ordering of criteria that you would like to prioritize matching students on. This is the order that the algorithm will partition the students on. For example, given the example config, the algorithm will first partition on year, then location, then homework start time, etc., as we wanted to prioritize matching students of the same graduation year first.

* Modify group size parameters: Adjust the MIN_GROUP_SIZE and MAX_GROUP_SIZE parameters until you are satisfied with the final group sizes in the output CSV file.

* If the form is modified from the example config, modify the config: If you added new questions to the survey, make sure to include them as a new entry in the ROW_CONFIG, and optionally create a new transformer method that will bucket that question's options.

Run script: `python run.py example_config.py data/responses_clean.csv`
* example_config.py is the config file that is tailored to your desired grouping output.
* data/responses_clean.csv is your cleaned google form dataset. 

### Post Processing
Make some manual spot checks. The algorithm should do what it is supposed to do. We recommend making sure that the following doesn’t happen: 
1. A student is a singleton (i.e. the only student of their race/gender in a given group)
2. Solo students (1 person in a group)-- add this student to an existing group
Manually modify the groups in the output CSV file if necessary.

TODO: add yamm script and file

## Our Publications

[1] Sumer Kohli, Neelesh Ramachandran, Ana Tudor, Gloria Tumushabe, Olivia Hsu, and Gireeja Ranade. 2023. Inclusive study group formation at scale. In Proceedings of the 54th ACM Technical Symposium on Computer Science Education V. 1, 11–17.

[2] Bridget Agyare, Alicia Matsumoto, Manooshree Patel, and Gireeja Ranade. 2023. Student Feedback on Opt-in, Inclusive, Course-Integrated Study Groups. In 2023 IEEE Frontiers in Education Conference (FIE). IEEE, 1–10.

## Contact Info
Please email ucb-group-matching@berkeley.edu if you have any questions!