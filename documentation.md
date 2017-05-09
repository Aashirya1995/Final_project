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

## Steps to set up the Docker cloud.

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
