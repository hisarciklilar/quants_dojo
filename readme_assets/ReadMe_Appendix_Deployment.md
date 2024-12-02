# Deploying the app on Heroku

Steps that need to be followed for deployment are provided on the README.md file. This document provides more detailed information using screenshots using love sandwiches walkthrough as an example.

- Place the main code for running the app in the `run.py` file
- Place the dependencies in the `requirements.txt` file using `pip3 freeze > requirements.txt`.

 ![Requirements](./images/deployment/deployment_requirements.png)

- Create an account on Heroku
- Click on the `Create New App` button

![Create New App](./images/deployment/deployment_ss1.png)

- Provide an app name and choose location: Europe for residents of Europe.

![Provide App Name](./images/deployment/deployment_ss2.png)

- Go to `Settings` tab.

![Provide App Name](./images/deployment/deployment_ss3.png)

- In the `Config Vars` section, click on `Reveal Config Vars` button.

![Provide App Name](./images/deployment/deployment_ss4.png)

- In the `KEY` field, type in capital letters `CREDS`. In the `VALUE` field, copy-paste the contents of the `creds.json` file

![Provide App Name](./images/deployment/deployment_ss5.png)

- In the new `KEY` field that appears below, type `PORT` and type `8000` in the corresponding value field

- Click `Add buildpack` button. Two buildpanks will be needed:
  
  1. `heroku/python`
  2. `heroku/nodejs`

    Ensure that Python is listed before nodejs.

![Provide App Name](./images/deployment/deployment_ss7.png)

- Find and select `python` from the officially supported buildpacks. Click `Add buildpack` button.

![Provide App Name](./images/deployment/deployment_ss8.png)

- Do the same for `nodejs`.

![Provide App Name](./images/deployment/deployment_ss9.png)

- Go to `Deploy` tab on top. Choose `GitHub` as the `Deployment method`. Heroku will try to establish a conneciton with GitHub account. Authorize the connection.

![Provide App Name](./images/images/deployment/deployment_ss10.png)

![Provide App Name](./images/deployment/deployment_ss11.png)

- Search for the repository name that you want to deploy and click `connect`.

![Provide App Name](./images/deployment/deployment_ss13.png)

![Provide App Name](./images/deployment/deployment_ss14.png)

- Choose `Deploy branch` for manual deployment, where one can see the progress of deployment. Click `Enable Automatic Deploys` for automatic deplomyment. This will update the files as GitHub is being updated.

![Provide App Name](./images/deployment/deployment_ss15.png)
