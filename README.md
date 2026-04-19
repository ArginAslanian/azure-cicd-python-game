# 🚀 Azure CI/CD Pipeline: Python Web App

## Overview
This project demonstrates a complete Continuous Integration and Continuous Deployment (CI/CD) pipeline. I transformed a standard Python console application into a stateless Flask web app and automated its deployment to an Azure App Service using GitHub Actions.

## 🏗️ Architecture & Technologies Used
* **Frontend:** HTML/CSS
* **Backend:** Python 3.13, Flask, Gunicorn
* **Cloud Provider:** Microsoft Azure (Linux App Service, Free Tier)
* **CI/CD:** GitHub Actions
* **Security & IAM:** Microsoft Entra ID (Service Principal), Azure RBAC, GitHub Secrets

## ⚙️ The Deployment Workflow
1. **Trigger:** A developer pushes code to the `main` branch.
2. **Build:** GitHub Actions provisions an Ubuntu runner, installs Python 3.13, and installs application dependencies (`requirements.txt`).
3. **Authenticate:** The pipeline securely authenticates to Azure using a dedicated Service Principal stored in GitHub Secrets.
4. **Deploy:** The packaged application is pushed to an Azure Linux Web App via the `azure/webapps-deploy` action.

## 🔒 Security Best Practices Implemented
* **Zero Hardcoded Secrets:** The Flask `SECRET_KEY` is injected via Azure Environment Variables, completely decoupled from the source code.
* **Least Privilege Access:** The Azure Service Principal was granted the `Contributor` role scoped *strictly* to the specific Resource Group containing the App Service, rather than the entire subscription.
