# Final project Documentation <h1> </h1>

## Setting up Git and Docker cloud for the project

First of all you will need a Git and Docker cloud account. To create the accounts click on the links provided [Github:]( https://github.com/) and for [Docker cloud](https://cloud.docker.com).
After, we have our accounts all set up lets start fixing the settings according to the needs of our project.

## Github Repository

Once we have our Github account set up. The next step is to have make a Github repository. To put your project up on Github, you will need to create a repository for it to live in. This is where we can keep a record of our work using the "commits". Whenever we add something new to our code we commit it before pushing it on Github. Every commit recieves a commit hash which makes keeping track of work much easier. 

### Steps to create a Github Respository

1. Sign in to your account on [Github:]( https://github.com/) and on the upper-right corner of any page, click +, and then click on **New repository**

![image3](https://github.com/Aashirya1995/Final_project/blob/master/images/file3.png)


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
 4. Add another file 'docker-compose.test.yml ' and add the following code : 
 	```bash
 	sut:
  		build: .
  		command: bash ./run-test.sh
  	```	
    	'
## Ensure that the test runs, but fails.

1. Commit the changes to run_test.sh, unh698.py, and unh698_test.py to your branch.

2. Push your branch to your github, and start a pull request.

3. Verify that the build in docker cloud attempts to run the python unit tests but fails. You should see an error like python3: command not found.

## Next, you have to make the test pass.  

1. Make changes to either Dockerfile and/or unh698.py to attempt to make the test pass.

2. Commit and push changes to the github branch. If the test passes, merge and submit a link to your pull request. If the test fails, return to step 4.


## By now your Flask server must be complete. Next, step is to set up the Flask server in AWS.

1. Before that we need to make sure that you have the following list of things done.

		a) Changes to the 'name_of_your_repo' that passes the python unit test.
		b) Changes have ben mad via a PR
		c) The last commit should have a check mark on it.
		d) You should have merged your pull request.

2. Setting up the flask server in AWS.

Task 1) You will have your private ssh key. Create a new folder in your local repo and here is what you need to know, your private ssh kay is like your password you should never push it to your github account because once, it is up anybody can see it. Also, you will be provided with t2.micro instances for your use. 
		a) Review the different types of instances here : (  https://aws.amazon.com/ec2/instance-types/) 

Task 2) Each of you will have your own instance. 
		
		a) You will ssh into a linux server using your sshkey. Once, you have a folder for the sskhey in your local repo, you will 'cd' into that and then run the following command. 
			'''
			ssh -i yoursshkey username@awsserver
			'''
			yoursshkey will look like - akaushik@21.32.***.2
			username in this case is - akaushik

Task 3) Configure the server. We want all the tools that we need for this assignment running on this AWS instance.

		a) We need Docker running, so to do that once you have ssh into your server run the following commands
			```bash
			sudo apt install docker.io
			sudo apt-get update
			sudo usermod -aG docker $(whoami)
			logout
			login ( how you logged in your server before )

			```
		b) To check the docker server is running to the following:
			```bash
			# run the following command to check if the docker service is running
			ps aux | grep docker
			# Check if you can run a simple container
			docker run ubuntu:xenial echo "hello world"
			```

		c) Once, you have your Docker all set up and running on your server. Next step is to clone your repo onto the server. 
			```bash
			git clone your_Repo
			```
		d) Now, you should be able to run the following commands
			```bash
			# This builds a local image of your docker cloud Flask server.
			docker build -t test .
			# To verify that git works fine 
			git log --oneline --decorate
			```
Task 4) To pull the latest copy of your public repo-test image. 
		
		a) Verify that you have the correct imagge.
			'docker images'

Task 5) Start a container using your public repo-test image.
		
		a) Star a docker container and keep it running in the background. 
			'
			sudo docker run -d -p 8080:8080 dockername/reponame python3 unh698.py

			'
			-d option runs the container in the background and prints container ID

			returns an ID like this “9f54f0be98f9e36b72d4cfae5fc78f6f7123b227a6d40a5a70e5330036412f2d”

			'
			# Check if the instance is running or not using the following command :
			docker ps
			# You should see something like 0.0.0.0:####->####/tcp

			'

Task 6) Test your web server. 

		a) Before going to a web browser, you can confirm connectivity by 
			' wget hhtp://awsserver:8080'

## Git Tags

A git tag is a reference to a specific commit hash. Tags are unique and can only point to a signle part of your code. In this project we will be using the tags as version of the docker images built by docker cloud and then use those versioned images to later control what version of the application is running in production.

Note : When you are tagging, make sure your local repo matches with your remote/github version of the repository.

To check that use the following commands :

	'git checkout master'
	'git pull origin master'
	 
Next, you need to set your most recent commit to your repo-test's master branch to 0.0.1

	'git checkout master'
	'git pull origin master'
	'git tag 0.0.1'
	
Now to push this tag on to your github and verify through the User Interface that the tag exists.
	'git push --tags origin master
	'
## Docker cloud settings to build Versioned Images

In oder to see the tag on Docker cloud we will have to make a few changes. Our configuration should be how we set it up in the beginning.
Now, when you go to ( https://hub.docker.com/ ) and select your repository and then go to tags and you should be able to see your tag here.

## Release the first version 0.0.1 website

To do this you will have use the same 'docker run' command but will have to append with tag version of the image. Mine would look like 'ak2526/finalproject:release-0.0.1.'

## New page

You can add new pages to your website by simply making new html templates and adding new tags and releasing them. To do this the steps to be followed stay the same :

	a) Once, your build in your branch passes. Merge your github PR
	b) Pull your newest master changes to your local repo

		'git checkout master'
		'git pull'

	c) add your next git tag of whatever you want. For example 0.0.2

		'git tag 0.0.2'

	d) push your tags to github

		'git push --tags origin master'

After you push your tags, if you go to your Docker cloud you will see a build building in that version suppose 0.0.1. Once, this build is successful. Go to your aws server and pull the most recent version using command 'git pull'.


## Points to keep in mind for Docker images.

If you keep pulling images down from docker to your AWS server, if it exceedes a certain limit it might give you an error 'not enough space' to fix that you can do the following :

	'docker images 
	 docker rmi [image name]
	'
When you run 'docker images' it will display all the images and you can decide which ones you want to remove. They will still be on docker hub in case you need to pull them down again using the following command:

	'docker pull ak2526/finalproject:release-0.0.#'

## Ansible

1) What is ansible? To read more about it go on the following link (http://docs.ansible.com/ansible/) and to see what can be configured with it check the link (http://docs.ansible.com/ansible/list_of_all_modules.html)

2) Install Ansible on your laptop.

	'pip install ansible'

3) Create the start of your ansible playbooks

Checkout another branch of your repo for your ansible work and in that branch add the following :

	a) Create an ansible folder

### Ansible deployment

Now you will use an ansible playbook to run the two versions of your website discussed above. The production is the one with first 3 pages of the website and the staging version is the one with additional pages. 

For the deployment you will be provided with a folder with generally structured playbook required to set up docker.

We will now be running two instances of your website in seperate containers. As discussed before the first version will be the production and will be accessible on port 8080 and the second version will be the production which will be accessible on port 8081. 

### Set up

#### a) The AWS servers provided to you will have ansible and git set up on it.

#### b) Copy the 'ansible' folder into your project repository.

#### c) Create a branch, add ansible folder and push the branch to your github repository.

	'git checkout master
	 git pull
	 git checkout -b pick-a-branch-name
	 git add ansible
	 git commit -m " add a message about what you are doing in this commit"
	 git push origin pick-a-branch-name'

#### d) Login to your AWS server, clone your repository and switch to your newly created branch. 
	'cd ~
	 git clone [your-repo]
	 cd [your-repo]
	 git checkout pick-a-branch-name'

#### e) In your ansible folder there will be playbooks. First run the configure-host.yml playbook (on your AWS server). This is done to verify that ansible is set up or not.

	'ansible-playbook configure-host.yml -v --extra-vars "student_username=xxxxxxx"
	# replace xxxxxxxx with your AWS username. For example mine is akaushik
	'
	Make changes to the ansible playbook locally, 'git push' them and then 'git pull' them on your AWS server.

#### f) Fixing the playbooks
		
		The three following playbooks should look like this : 

		a) configure-host.yml. Replace the xxxxx and make your playbook look like the following.

			```bash
			---
			# This playbook configures the local machine to run docker.
			# When fixed, the playbook should install and run the
			# community edition of docker found from docker's official
			# apt repository.
		   	-name: Install the community edition of docker
  			 hosts: localhost
  			 become: true
  			 roles:
    			- docker
    		```

    	b) deploy-website-production.yml. Again replace the xxxxxx and make it look like the following.

    		```bash
    		---
			# The production version of docker-cloud-test should be the image that has just
			# a main page with the 'UNH698 Website' text.  This version of the website
			# should be available on port 8080 of your server.
			- name: Deploy the production version of your website based on the previous tag of your docker-cloud-test image
			  hosts: localhost
			  become: true
			  vars:
			    unh698_environment: production
			    unh698_image_version: release-0.0.16
			    unh698_host_port: 8080
			    unh698_container_port: 5000
			  roles:
			    - unh698

			 ```

		c) deploy-website-staging.yml. Replace the xxxxxx to make it look like the following 

			```bash
			---
			# The production version of docker-cloud-test should be the image that includes the website with
			# your topic subpage.  This version of the website should be available on port 8081 of your server.
			- name: Deploy the staging version of your website based on the newest tag of your docker-cloud-test image
			  hosts: localhost
			  become: true
			  vars:
			    unh698_environment: staging
			    unh698_image_version: release-0.0.18
			    unh698_host_port: 8081
			    unh698_container_port: 5000
			  roles:
			    - unh698

			```
#### Playbook - configure-host.yml
	
This playbook configures the local machine to run docker. When fixed, the playbook should install and run the community edition of docker found from docker's official apt repository.

You need to need the files in roles/docker and once you have made the required changes you can run the following command on your AWS instance to see if it worked or not 

		'# Replace xxxxxxx with your AWS username
		ansible-playbook configure-host.yml -v --extra-vars "student_username=xxxxxxx"'

#### Playbook - deploy-website-staging.yml, deploy-website-production.yml


These playbooks deploy and start two versions of your website. One a production instance and second the staging one.

To run the playbooks use the following commands:
	'ansible-playbook deploy-website-production.yml -v'

	This will go through the deploy-website-production.yml file and run the test and if everything works fine you will see something like this

![image1](https://github.com/Aashirya1995/Final_project/blob/master/images/file1.PNG)

	'ansible-playbook deploy-website-staging.yml -v'

	This will go through the deplot-website-staging.yml, you will see a similar picture. If any test fails it will show in red. 

![image2](https://github.com/Aashirya1995/Final_project/blob/master/images/file2.png)

Points to be kept in mind:

1) Staging and production containers are running 'release-#.#.#' versions of the docker image

2) Production instance is your first version.

3) Staging is the second version with more pages.

4) Production instance would be availabe on host's port 8080

5) Staging would be available on 8081.















