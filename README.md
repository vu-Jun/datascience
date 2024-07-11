# Report for Assignment 1 resit

## Project chosen

**Name:** Junhyeok Lee

**URL:** https://github.com/data-8/datascience

**Number of lines of code and the tool used to count it:** 5.8 KLOC counted by Lizard

**Programming language:** Python

## Coverage measurement with existing tool  

I have used **Coverage.py**, which is an existing tool to measure coverage for python projects. 

**Step 1: clone git project to the local repository**

**Step 2: make sure to install all neccessary modules for projects to run flawlessly**   

- pip install coverage  
- pip install pytest  
- pip install datascience  
- pip install -r requirements.txt  
- pip install -r requirements-tests.txt  

**Step 3: Once all modules are installed, change current directory to the root directory of the project and run coverage by Coverage.py**    

**coverage run --branch -m pytest**    

<img src="sep_image/coverage_run.png" style="width:600px; height:auto;">  

**coverage report**  

<img src="sep_image/coverage_report.png" style="width:600px; height:auto;">  

**coverage html**  

<img src="sep_image/old_overall_coverage.png" style="width:600px; height:auto;">  


## Coverage improvement

### Individual tests  

**<Function 1: _varargs_labels_as_list>**

**Creation of test cases commit:** https://github.com/vu-Jun/datascience/commit/52a880444d99e3a2b3866a85a4e38839d2fc1a0d  

**Creation of instrumentation and flags:** https://github.com/vu-Jun/datascience/commit/bf9c76c05963e64fc2eab859c47eaf382565055b  ,
                                           https://github.com/vu-Jun/datascience/commit/8db13fa1e89a55be4da803eba829b3326985fb54  

**Existing tool old coverage result:**

<img src="sep_image/f1_old_bCoverage_html.png" style="width:600px; height:auto;">  

**Instrumented result after creating test cases:**  

<img src="sep_image/f1_branch_coverage.png" style="width:600px; height:auto;">

**Existing tool new coverage result:**  

<img src="sep_image/f1_new_bCoverage_html.png" style="width:600px; height:auto;">  

As you see the structure of "_varargs_labels_as_list" function, it consists of 4 different branches that cannot be satisfied in one go, thus I have made 4 test cases to satisfy each branch hit at least once and those four cases of 25 percent of coverage adds upto 100 percent branch coverage. By using existing coverage tool, it is shown that it has covered from 69 percent to 100 percent.

- test_varargs_labels_as_list_empty_list ensures the function handles empty input correctly.   
- test_varargs_labels_as_list_not_iterable verifies that a list of labels is processed as expected.   
- test_varargs_labels_as_list_single_list checks the function’s behavior when a single list is passed.   
- test_varargs_labels_as_list_raise_value_error tests the error handling when multiple lists are passed, raising a ValueError.  


**<Function 2: circle.draw_on>**

**Creation of test cases commit:** https://github.com/vu-Jun/datascience/commit/3fde7df62976973049ef9c8b1c57597543d6f48d  

**Creation of instrumentation and flags:** https://github.com/vu-Jun/datascience/commit/07db19f7480d2eefc21240d7c8e9510a10094105  

**Existing tool old coverage result :**  

<img src="sep_image/f2_old_bCoverage_html.png" style="width:600px; height:auto;">  

**Instrumented result after creating test cases:**  

<img src="sep_image/f2_branch_coverage.png" style="width:600px; height:auto;">

**Existing tool new coverage result:**  

<img src="sep_image/f2_new_bCoverage_html.png" style="width:600px; height:auto;">  

Again, it consists of if and else statement, creating two branches to be taken consider of when measuring coverage. Thus, I have created 2 test cases to satisfy each branch at least once and two branch coverage measurement adds up to 100 percent coverage.  

- test_draw_on_radius_in_meters_true checks the behavior when radius_in_meters is set to True, ensuring the branch is executed and the coverage is recorded.   
- test_draw_on_radius_in_meters_false verifies the function's behavior when radius_in_meters is set to False, ensuring this branch is also covered.  


### Overall

**Before create/enhance test cases:**

<img src="sep_image/old_overall_coverage.png" style="width:600px; height:auto;">

**After create/enhance test cases:**

<img src="sep_image/new_overall_coverage.png" style="width:600px; height:auto;">


