# Final project Documentation <h1> </h1>

## Setting up Git and Docker cloud for the project

First of all you will need a Git and Docker cloud account. To create the accounts click on the links provided [Github:]( https://github.com/) and for [Docker cloud](https://cloud.docker.com).
After, we have our accounts all set up lets start fixing the settings according to the needs of our project.

## Github Repository

Once we have our Github account set up. The next step is to have make a Github repository. To put your project up on Github, you will need to create a repository for it to live in. This is where we can keep a record of our work using the "commits". Whenever we add something new to our code we commit it before pushing it on Github. Every commit recieves a commit hash which makes keeping track of work much easier. 

### Steps to create a Github Respository

1. Sign in to your account on [Github:]( https://github.com/) and on the upper-right corner of any page, click +, and then click on **New repository**

2. Enter a name for your project

3. Add a description of your project (optional)

4. Choose between creating a *public* or a *private* repository. For your project you will choose *public*

5. Select ** Initialize this repository with a README.**

6. Click on **Create repository**

CONGRATULATIONS!!!! Your repository is all set. 

### Steps to set up the Docker cloud.

Once you have created your Docker Cloud account, next step is to create a repository on Docker Cloud that connects to our Github repository. To do this do the following:

1. Click on the Repositories tab.

2. Then on the "Create" button.

3. Name your repository whatever you like.

4. Add a description. (Optional)

5. Add your github account to the build settings and select the git repository for your project. 

6. Next, click on the "Create" button.

7. Then click on the Builds.

8. Click on the **Configure Automated Builds** 

9. Next, you have to select **Internal Pull Requests**

10. Leave the current build alone.

11. Select Internal Pull Requests

12. Put this in the source box: /^[0-9.]+$/

13. Add release-{sourceref} in the Docker tag box.

14. Next step is to save.

Your Docker is set up now.

## Branch

A branch in Git is simply a lightweight movable pointer to one of these commits. The default brnach name in **Git** is **master**. 

1. Create a new branch using the following command : 
	'git checkout -b branch name'
	Once you do that you will notice that from 'master' branch you have been switched to 'branch name' branch.

## Next step is to create the files.

These are the files that we need in order to run docker containers and to build images.

'1. Create a file  'run_test.sh'. Add the following code to the file:
	```bash
    #!/bin/bash
    echo "Running Flask Unit Tests"
    python3 testName.py
    ```
 2. Next, you need to create a python file and name it anything that you would like. This would include the methods for each of your templates that you would want to display. Add the following code:
 	```python
    from flask import Flask, render_template
    from prometheus_metrics import setup_metrics
    app = Flask(__name__)
    setup_metrics(app) 

    @app.route('/')
    def run_flask():
      return render_template('Nameoftemp.html') 
      
    if __name__ == '__main__':
      app.run(debug=True, host='0.0.0.0')
    ```
 3. Now create a another python file that will run own code from the above mentioned python file. Add the following code to this file:
 	```python
 	import unittest

	import unh698


	class FlaskrTestCase(unittest.TestCase):

    	def setUp(self):
        	self.app = unh698.app.test_client()

    	def tearDown(self):
        	pass

    	def test_home_page(self):
        	# Render the / path of the website
        	rv = self.app.get('/')
        	# Chech that the page contians the desired phrase
       	 	assert b'UNH698 Website' in rv.data

    	def test_link_to_my_page(self):
       	 	rv = self.app.get('/')  
        	# Search the page contents for the link to your topic page 
        	# Replace xxxxxxxxxxxx with text you'd expect to see on your main page that links to your subpage
        	assert b'Topic: DOGS' in rv.data

  
	if __name__ == '__main__':
    	unittest.main()
    ```

    	'



