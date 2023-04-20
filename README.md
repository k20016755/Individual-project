# Individual-project
Evaluating tests in a python/Django application
Fork the repository https://github.com/k20016755/Individual-project.git to make changes to the codebase. Instructions are given in the project report on how to fork the repository in Chapter 5.4. Otherwise, download the ZIP file of this project and extract it to your machine to test manually.  You can also git clone the repository https://github.com/k20016755/Individual-project.git in your preferred code editor. Once the Individual-Project is opened in your preferred code editor you can carry on to the next steps.
Make sure Python and pip is installed on your system. You can check his by running the following commands in the terminal of your preferred code editor or virtual machine terminal:
$ python --version
$ pip --version
Next, install the Package for virtual environment. This can be done in the terminal with the following command:
$ apt-get install python3-venv
In the Individual-Project directory, create the virtual environment with the following
Command in the terminal:
$ python3 -m venv venv
Activate the virtual environment with the following command in the terminal:
Windows:
.\venv\Scripts\activate
macOS and Linux:
$ source venv/bin/activate

Now, the required packages listed in the file requirements.txt, which will be in the root of the Individual-Project directory, can be installed with the following command:
$ pip install -r requirements.txt
The user should ensure they read the instructions in the README.md file located in the root of the repository.
You can now start adding your files to the directory. If you have forked the directory the changes you make will be pushed to your personal directory from which a pull request will be generated to https://github.com/k20016755/Individual-project.git this repository and when your changes are merged you will be able to evaluate your tests according to the workflow runs. Before making these changes you must make some changes in the .github/workflows/ folder to the workflow files. If you have added a Django project and Django test files you must add your Django environment variable to all the files in this folder. You must then add your Django test files to the –tests-dir variable in the
.github/workflows/mutation.yml file or if you have added a Python file to be evaluated you must add it to the –paths-to-mutate variable in this same file. The steps below will help you do this:
1.	Change your mutation file:
First of all open the .github/workflows/mutation.yml file in the project in the code editor where you are making your changes. The original file looks something like this:
name: Python Mutation Test
env:
    PYTHONPATH: $PYTHONPATH:mydjangoproject
    DJANGO_SETTINGS_MODULE: mydjangoproject.settings
on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  mutation-testing:
    runs-on: ubuntu-latest
    
        
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'
    - name: Install dependencies
      run: |

        python -m pip install --upgrade pip
        pip install mutmut
        pip install -r requirements.txt
        python manage.py migrate
        python -m pip install --upgrade pip
        pip install flake8 pytest
        pip install pytest pytest-django
        pip install django
        pip install pony==0.7.14
    - name: Run mutation tests

      run: mutmut run --paths-to-mutate=test_min.py --tests-dir=mydjangoapp/tests/
    - name: Generate Mutation test report
      if: always()
      run: mutmut junitxml > test-results.xml
    - name: Upload test report Artifact
      if: always()
      uses: actions/upload-artifact@v2
      with:
        name: test-results
        path: test-results.xml
If the user has for example added a Django project by the name of userdjangoproject and created a test_views.py in their userdjangoapp/tests folder they will have to add their environment variable and change the –tests-dir variable in this file. On top of that if they have added a python file by the name of test_user.py they will have to add that to the –paths-to-mutate variable. Here is the changed file for the exemplary changes mentioned:
name: Python Mutation Test
env:
    PYTHONPATH: $PYTHONPATH:userdjangoproject
    DJANGO_SETTINGS_MODULE: userdjangoproject.settings
on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  mutation-testing:
    runs-on: ubuntu-latest
    
        
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'
    - name: Install dependencies
      run: |

        python -m pip install --upgrade pip
        pip install mutmut
        pip install -r requirements.txt
        python manage.py migrate
        python -m pip install --upgrade pip
        pip install flake8 pytest
        pip install pytest pytest-django
        pip install django
        pip install pony==0.7.14
    - name: Run mutation tests

      run: mutmut run --paths-to-mutate=test_user.py --tests-dir=userdjangoapp/tests/
    - name: Generate Mutation test report
      if: always()
      run: mutmut junitxml > test-results.xml
    - name: Upload test report Artifact
      if: always()
      uses: actions/upload-artifact@v2
      with:
        name: test-results
        path: test-results.xml

These changes will be sufficient to update the mutation.yml file to make it identify the new userdjangoproject added. The changes will also allow mutations to be run on test_user.py file and all the test files in userdjangoapp/tests.


2.	Next, the specific changes made to the environment variable in the last step will have to be done in .github/workflows/codecov.yml, .github/workflows/benchmark.yml and .github/workflows/python-app.yml. All these files will have a section like this:
env:
    PYTHONPATH: $PYTHONPATH:mydjangoproject
    DJANGO_SETTINGS_MODULE: mydjangoproject.settings
This section must be changed to this for the exemplary changes mentioned in step 1:
env:
    PYTHONPATH: $PYTHONPATH:userdjangoproject
    DJANGO_SETTINGS_MODULE: userdjangoproject.settings

This will conclude the changes you have to make to the original files except your files to be added. However, you can make certain changes to the original files and add test cases to the files like test_num.py, test_benchmark.py and mydjangoapp/tests/test_model.py file if you want. Next add these changes to your personal repository which you have forked and then create a pull request to the original repository. Once the request is merged you can see the performance of your test suite that has been added from the workflow runs in the Github Actions section of the repository according to the commit code given for your changes. 


        

3.	.github/workflows/python-app.yml
The file above is another workflow that tests the application with pytest and unittest. Although this has little importance as we are looking to go beyond just running these tests, the user can still add their files that are to be unit tested as the rest of the application just looks for test_*.py files for pytest. For example, this is the original code for the file below:



# This workflow will install Python dependencies, run tests and lint with a single version of Python
	# For more information see: https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python
	

	name: Python application
	env:
	    PYTHONPATH: $PYTHONPATH:mydjangoproject
	    DJANGO_SETTINGS_MODULE: mydjangoproject.settings
	on:
	  push:
	    branches: [ "main" ]
	  pull_request:
	    branches: [ "main" ]
	

	permissions:
	  contents: read
	

	jobs:
	  build:
	

	    runs-on: ubuntu-latest
	

	    steps:
	    
	    - uses: actions/checkout@v3
	    - name: Set up Python 3.10
	      uses: actions/setup-python@v3
	      with:
	        python-version: "3.10"
	    - name: Install dependencies
	      run: |
	        python -m pip install --upgrade pip
	        pip install flake8 pytest
	        pip install pytest pytest-django
	        pip install django
	        python manage.py migrate mydjangoapp zero
	        python manage.py makemigrations mydjangoapp
	        python manage.py migrate mydjangoapp
	        python manage.py migrate
	        pip install -r requirements.txt
	    - name: Set up virtual environment
	      run:
	        python -m venv venv
	    - name: Activate virtual environment
	      run: 
	        source venv/bin/activate
	    
	    - name: Test with pytest
	      run: |
	        pytest
	    - name: Test with unittest
	      run: |
	        python evenorodd.py
If the user for example adds a file that has unit tests, named userunit.py, the last line of the code will be changed to:
python evenorodd.py,userunit.py






