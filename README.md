# Report for Assignment 1 resit

## Project chosen

**Name:** Junhyeok Lee

**URL:** https://github.com/data-8/datascience

**Number of lines of code and the tool used to count it:** 5.8 KLOC counted by Lizard.py

**Programming language:** Python

## Coverage measurement with existing tool  

I have used **Coverage.py**, which is an existing tool to measure coverage for python projects. 

**Step 1: clone git project to the local repository**

**Step 2: make sure to install all neccessary modules for projects to run flawlessly**   

**pip install coverage**  
**pip install pytest**  
**pip install datascience**  
**pip install -r requirements.txt**  
**pip install -r requirements-tests.txt**  

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

<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced tests for function 1>  

**Creation of test cases commit:** https://github.com/vu-Jun/datascience/commit/52a880444d99e3a2b3866a85a4e38839d2fc1a0d  

**Creation of instrumentation and flags:** https://github.com/vu-Jun/datascience/commit/bf9c76c05963e64fc2eab859c47eaf382565055b  ,
                                           https://github.com/vu-Jun/datascience/commit/8db13fa1e89a55be4da803eba829b3326985fb54  

**Existing tool old coverage result:**

<img src="sep_image/f1_old_bCoverage_html.png" style="width:600px; height:auto;">  

**Instrumented result after creating test cases:**  

<img src="sep_image/f1_branch_coverage.png" style="width:600px; height:auto;">

**Existing tool new coverage result:**  

<img src="sep_image/f1_new_bCoverage_html.png" style="width:600px; height:auto;">

<"State the coverage improvement with a number and elaborate on why the coverage is improved">  


**<Function 2: circle.draw_on>**

<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced tests for function 2>

**Creation of test cases commit:** https://github.com/vu-Jun/datascience/commit/3fde7df62976973049ef9c8b1c57597543d6f48d  

**Creation of instrumentation and flags:** https://github.com/vu-Jun/datascience/commit/07db19f7480d2eefc21240d7c8e9510a10094105  

**Existing tool old coverage result :**  

<img src="sep_image/f2_old_bCoverage_html.png" style="width:600px; height:auto;">  

**Instrumented result after creating test cases:**  

<img src="sep_image/f2_branch_coverage.png" style="width:600px; height:auto;">

**Existing tool new coverage result:**  

<img src="sep_image/f2_new_bCoverage_html.png" style="width:600px; height:auto;">

<"State the coverage improvement with a number and elaborate on why the coverage is improved">

### Overall

**Before create/enhance test cases:**

<img src="sep_image/old_overall_coverage.png" style="width:600px; height:auto;">

**After create/enhance test cases:**

<img src="sep_image/new_overall_coverage.png" style="width:600px; height:auto;">


