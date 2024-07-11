# Report for Assignment 1 resit

## Project chosen

Name: Junhyeok Lee

URL: https://github.com/data-8/datascience

Number of lines of code and the tool used to count it: 5.8KLOC counted by Lizard.py

Programming language: Python

## Coverage measurement with existing tool

<"Inform the name of the existing tool that was executed and how it was executed">

I have used Coverage.py, which is an existing tool to measure coverage for python projects. 

Step 1: clone git project to the local repository
Step 2: make sure to install all neccessary modules for projects to run flawlessly
** pip install coverage **
** pip install pytest **
** pip install datascience **
** pip install -r requirements.txt **
** pip install -r requirements-tests.txt **
Step 3: Once all modules are installed, change current directory to the root directory of the project and run coverage by Coverage.py
** coverage run --branch -m pytest **
** coverage report **
** coverage html **

<"Show the coverage results provided by the existing tool with a screenshot">

<img src="sep_image/old_overall_coverage.png" style="width:600px; height:auto;">

## Coverage improvement

### Individual tests

<The following is supposed to be repeated for each function (2 in total)>

<Function 1: _varargs_labels_as_list>

<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced tests for function 1>

<"Provide a screenshot of the old coverage results for such function">

<img src="sep_image/f1_old_bCoverage_html.png" style="width:600px; height:auto;">

<"Provide a screenshot of the new coverage results for such function">

Instrumented result:

<img src="sep_image/f1_branch_coverage.png" style="width:600px; height:auto;">

existing tool coverage result:

<img src="sep_image/f1_new_bCoverage_html.png" style="width:600px; height:auto;">

<"State the coverage improvement with a number and elaborate on why the coverage is improved">


<Function 2: circle.draw_on>

<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced tests for function 2>

<"Provide a screenshot of the old coverage results for such function">

<img src="sep_image/f2_old_bCoverage_html.png" style="width:600px; height:auto;">

<"Provide a screenshot of the new coverage results for such function">

Instrumented result:

<img src="sep_image/f2_branch_coverage.png" style="width:600px; height:auto;">

existing tool coverage result:

<img src="sep_image/f2_new_bCoverage_html.png" style="width:600px; height:auto;">

<"State the coverage improvement with a number and elaborate on why the coverage is improved">

### Overall

<"Provide a screenshot of the old coverage results by running an existing tool (the same as you already showed at the beginning of the report)">

<img src="sep_image/old_overall_coverage.png" style="width:600px; height:auto;">

<"Provide a screenshot of the new coverage results by running the existing tool using all test modifications">

<img src="sep_image/new_overall_coverage.png" style="width:600px; height:auto;">


