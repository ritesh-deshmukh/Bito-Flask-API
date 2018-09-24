<h1><b>Bito Visualization API</b></h1>
<h2>Deployed to AWS Elastic Beanstalk</h2>

<h2>MySQL Database on Amazon RDS</h2>

	test_teams - 10 static entries are present in this table
	
	test_teams_rand - to keep log of other possibilities of data in test_teams table

<h2><i>To test on your local machine</i></h2>

<p>Install virtualenv via pip:</p>
	
	$ pip install virtualenv
      
<p>Test your installation</p>
	
	$ virtualenv --version
      
<p>Create a virtual environment for a project:</p>
	
	$ virtualenv my_project  
    
<p>To begin using the virtual environment, it needs to be activated</p>
	
	$ source my_project/bin/activate
    
<p>Install the requirements.txt file for dependencies</p>
	
	$ pip install -r requirements.txt
    
<p>Run the files</p>
	
	$ python database_controller.py
	$ python database_extract.py

<h2>Relevant API Endpoints on AWS</h2>

	Insert 10 random rows - http://flask-env.vcvtfj4hvp.us-east-2.elasticbeanstalk.com/insert_random
	
	Populate Next 10 rows - http://flask-env1.xxwp3niah9.us-east-2.elasticbeanstalk.com/next10
	
	JSON to display on Front-End - http://flask-env1.xxwp3niah9.us-east-2.elasticbeanstalk.com/display10

<h2>Relevant API Endpoints Locally</h2>

	Insert 10 random rows - http://127.0.0.1:5000/insert_random
	
	Populate Next 10 rows - http://127.0.0.1:5001/next10
	
	JSON to display on Front-End - http://127.0.0.1:5001/display10

	