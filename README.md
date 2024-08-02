# Study Group Matcher 📚
This is a repository dedicated to hosting all code and files associated with our group-matching system. For a detailed overview of our system and how you can integrate it into your classroom, please view this [document](https://docs.google.com/document/d/1fwjhMQp1gaulxNNvgjQUJKQdKne5pkpXNf0U4q5hxVY/edit?usp=sharing) or alternatively, `Materials/overview.pdf`.

PDF versions of our template surveys including the intake survey, reassignment survey, and final feedback survey can be found in the "Materials" folder. If you have a UC Berkeley Google Drive account, you can access these surveys directly to make a copy at this [link](https://drive.google.com/drive/folders/1-IyhfElu9w_el7llScAWCOFn8QXDEmuH?usp=drive_link). Previous versions of our surveys and a detailed overview of the changes made to them over time can be found in the "Past Surveys" folder.

If you would like to learn more about our group-matching algorithm and its impact on students' educational experiences, see [1] and [2].

## Example usage:
With Python 3.x installed, run:

`python run.py example_config.py /path/to/intake_survey_responses.csv`

## Steps for Running the Algorithm

### Outline of the Group-Matching Process
1. Data Cleaning and Preprocessing
2. Running the Algorithm
3. Post Processing

### 1. Data Cleaning and Preprocessing:
Make sure that the column names in your input CSV (intake_survey_responses.csv) match or contain the strings in the corresponding Column objects in your config file. If needed, we recommend changing the column names in the CSV directly.

### 2. Running the Algorithm
#### Algorithm settings / Modifying the Config File: 
The following modifications should be made in your config file. The config file needs to reflect any changes made to your survey. An example config file can be found in this repo (`example_config.py`). Below are some suggested config file modifications:

* Modify the CONSTRAINTS settings to match your grouping preferences: Update the "Partition" entry in the CONSTRAINTS dictionary to reflect the ordering of criteria that you would like to prioritize matching students on. This is the order that the algorithm will partition the students on. For example, given example_config.py, the algorithm will first partition on year, then location, then homework start time, etc., as we wanted to prioritize matching students of the same graduation year first.

* Modify group size parameters: Adjust the MIN_GROUP_SIZE and MAX_GROUP_SIZE parameters until you are satisfied with the final group sizes in the output CSV file.

* If you make modifications to the example intake survey, modify the config: If you added new questions to the survey, make sure to include them as a new entry in the ROW_CONFIG, and optionally create a new transformer method that will bucket that question's options.

#### Usage and Output
Run script: `python run.py example_config.py /path/to/intake_survey_responses.csv`
* `example_config.py` -- the config file that is tailored to your desired grouping output
* `/path/to/intake_survey_responses.csv` -- your cleaned dataset

The algorithm should output a file called "out-private.csv" which contains the group assignments. Students with the same group_num in out-private.csv were matched to the same group. You can sanity check that students are being matched based on the correct configurations by checking the values in each column.

### 3. Post Processing
Make some manual spot checks to your out-private.csv file. This includes manually modifying the groups in the output CSV file if necessary. We recommend making sure that the following doesn’t happen: 
* A student is a singleton (i.e. the only student of their race/gender in a given group) -- add this student to a group where they are not a singleton
* Solo students (1 person in a group) -- add this student to an existing group

To email students information about their study group partners we use [YAMM](https://yamm.com/). Our script to create a YAMM compatible CSV file given your out-private.csv is at `Materials/into_yamm.ipynb`. The corresponding example YAMM email script can also be found in that file.

## Our Publications

[1] Sumer Kohli, Neelesh Ramachandran, Ana Tudor, Gloria Tumushabe, Olivia Hsu, and Gireeja Ranade. 2023. Inclusive Study Group Formation at Scale. In Proceedings of the 54th ACM Technical Symposium on Computer Science Education V. 1, 11–17.

[2] Bridget Agyare, Alicia Matsumoto, Manooshree Patel, and Gireeja Ranade. 2023. Student Feedback on Opt-in, Inclusive, Course-Integrated Study Groups. In 2023 IEEE Frontiers in Education Conference (FIE). IEEE, 1–10.

## Contact Info
Please email ucb-group-matching@berkeley.edu if you have any questions!
