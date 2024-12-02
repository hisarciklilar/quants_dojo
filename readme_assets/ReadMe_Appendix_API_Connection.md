# Establishing an API connection

As of November 2024, below are the steps that need to be followed for establishing an API connection with a Google sheet document. See [ReadMe Appendix API Connection](./readme_assets/ReadMe_Appendix_API_Connection.md) for more information with screenshots.

- Login to `Google Cloud` and select `New Project`. Link to Google Cloud Platform <https://console.cloud.google.com/>

![Google Cloud New Project](./images/api_connection/api_ss1.png)

- Give project a name and click `Create`

![Create New Project](./images/api_connection/api_ss2.png)

- From the left-hand-side menu, choose `APIs and services` and select `Library`

![APIs - Library](./images/api_connection/api_ss3.png)

- Search for the `Google Drive API` in the `API Library`

![Google Drive API search](./images/api_connection/api_ss4.png)

![Google Drive API](./images/api_connection/api_ss5.png)


- Select `Google Drive API` and click `Enable`

![Google Drive API Enable](./images/api_connection/api_ss6.png)

- As `Google Drive API` is selected, click on the `Create Credentials` button

![Google Drive API - Create Credentials](./images/api_connection/api_ss7.png)

- Under `Which API are you using?`, choose `Google Drive API` and select `Application data`. Click `Next`.

![Google Drive API - Application data](./images/api_connection/api_ss8.png)

- Under `Service account details`, provide a `Service account name`. You will see a `Service account ID` being created with an email address for service account. Click `Create and Continue`.

![Google Drive API - Service account details](./images/api_connection/api_ss9.png)

- Under `Grant this service account to the poject`, choose `Project` and `Editor` as role.

![Google Drive API - Service account access](./images/api_connection/api_ss10.png)

- Under `Credential`, `Service Accounts`, choose the account you would like to work with.

![Google Drive API - Credentials](./images/api_connection/api_ss11.png)

- Under `Service accounts`, ensure service account is enabled.

![Service Account Enabled](./images/api_connection/api_ss12.png)

- Under `Service accounts`, select the `KEY` tab on top and then on the `KEY` page, select `ADD KEY` --> `Create new key`.

![Create new key](./images/api_connection/api_ss13.png)

- In the opening window, choose `JSON` as the `Key type`.

![Private key - json](./images/api_connection/api_ss14.png)

- Once this is complete, go to `APIs and services` again and choose `Library`.

![APIs Library](./images/api_connection/api_ss15.png)

- This time search for `Google Sheets API`. Select and `Enable` `Google Sheets API`.

![Google Sheets API](./images/api_connection/api_ss16.png)

![Google Sheets API](./images/api_connection/api_ss17.png)

![Google Cloud New Project](./images/api_connection/api_ss18.png)

- Once your `JSON` file is downloaded, copy this into your project folder and rename it as `creds.json`. Add this file to `.gitignore` so that private sensitive information is not chared with public.

- Open the `creds.json` file and copy the `client_email` address to clipboard. Paste this address on the Google sheet's `Share` window. Confirm share. This will allow to establish a connection between the workspace and Google sheet.

![Google Cloud New Project](./images/api_connection/api_ss20.png)
