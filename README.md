# Outreach Pipeline

## Project Overview

This project automates the outreach workflow by finding similar companies, identifying decision makers, generating email addresses, and sending emails automatically using SMTP.

## Features

* Find similar companies from a company domain
* Get decision makers from companies
* Find email addresses
* Send emails using custom domain email
* Store generated data in CSV format
* SMTP email integration using Private Email

## Technologies Used

* Python
* SMTP
* CSV
* Git & GitHub

## Project Structure

outreach_pipeline/
│── modules/
│   ├── ocean.py
│   ├── prospeo.py
│   ├── eazyreach.py
│   ├── email_sender.py
│── main.py
│── config.py
│── requirements.txt
│── README.md

## Installation

Install dependencies:

pip install -r requirements.txt

## Run Project

Run the project using:

python main.py

Enter company domain when prompted:

Example:
google.com

## Output

* Sends emails using configured SMTP
* Generates outreach results
* Stores output in CSV format

