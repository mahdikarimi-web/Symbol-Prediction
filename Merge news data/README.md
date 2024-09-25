This script merges multiple CSV files from a source directory into a single CSV per topic and removes duplicate rows. The merged files are saved in a target directory, with each file representing a unique topic based on the filename.

Usage

1. Place the script in your working directory.

2. Modify the source_dir and target_dir paths in the script to match your directories:

source_dir: Directory containing the CSV files to be merged.

target_dir: Directory where the merged CSV files will be saved.

3. The script assumes that the topic is a part of the CSV filename before any delimiter such as an underscore (\_).

4. Run the script. It will:

Read all the CSV files from the source_dir.

Group and merge the CSV files by topic.

Remove duplicate rows from each merged CSV.

Save the merged files in the target_dir.
