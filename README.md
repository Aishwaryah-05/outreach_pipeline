# Outreach Pipeline

## Overview

This project is an automated outreach pipeline that:

* Finds similar companies from a given company domain
* Finds decision makers for each company
* Generates email addresses
* Saves results into CSV format
* Sends outreach emails using Brevo
* Provides a confirmation step before sending emails

---

## Features

* Company discovery module
* Decision maker extraction
* Email generation
* CSV export
* Brevo email integration
* Confirmation before bulk sending
* Modular architecture
* Error handling for API failures
* Environment variable support

---

## Project Structure

```
outreach_pipeline/
│
├── modules/
│   ├── ocean.py
│   ├── prospeo.py
│   ├── eazyreach.py
│   ├── brevo.py
│   └── email_sender.py
│
├── .env
├── .gitignore
├── config.py
├── main.py
├── requirements.txt
├── results.csv
└── README.md
```

---

## Technologies Used

* Python
* Brevo API
* SMTP
* CSV Handling
* Environment Variables
* Git & GitHub

---

## Setup Instructions

### Clone Repository

```bash
git clone https://github.com/Aishwaryah-05/outreach_pipeline.git
cd outreach_pipeline
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
EMAIL=your_email
PASSWORD=your_password
SMTP_SERVER=mail.privateemail.com
SMTP_PORT=587
BREVO_API_KEY=your_brevo_key
PROSPEO_API_KEY=your_prospeo_key
```

---

## Run Project

```bash
python main.py
```

Enter:

```text
google.com
```

---

## Workflow

1. Enter company domain
2. Find similar companies
3. Extract decision makers
4. Generate emails
5. Save output to CSV
6. Show summary
7. Confirm sending
8. Send emails using Brevo

---

## Output

### CSV Output

Results are stored in:

```text
results.csv
```

Example:

```text
amazon.com,CEO,ceo@amazon.com
amazon.com,VP Sales,vp-sales@amazon.com
```

---

## API / Tool Notes

### Brevo

* Used for sending emails
* API integration completed

### Ocean.io

* Signup/API limitations encountered
* Fallback implementation used

### Prospeo

* API endpoint issues encountered
* Modular replacement maintained

### EazyReach

* No accessible API / credits unavailable
* Fallback implementation maintained

---

## Error Handling

Implemented for:

* API failures
* Empty responses
* Email sending failures
* Invalid results

---

## Future Improvements

* Real API integrations
* Better email personalization
* Logging system
* Database support
* Analytics dashboard

---

## GitHub Repository

Repository:

https://github.com/Aishwaryah-05/outreach_pipeline
