# Outreach Pipeline

## Project Overview

This project is an automated outreach pipeline that:

* Takes a company domain as input
* Finds similar companies
* Finds decision makers from those companies
* Generates email addresses
* Stores results in CSV format
* Sends outreach emails using Brevo API

---

## Features

* Similar company discovery
* Decision maker extraction
* Email generation
* CSV export
* Brevo email integration
* Domain-based email authentication

---

## Project Structure

```text
outreach_pipeline/
│
├── modules/
│   ├── ocean.py
│   ├── prospeo.py
│   ├── eazyreach.py
│   ├── brevo.py
│   └── email_sender.py
│
├── main.py
├── config.py
├── requirements.txt
├── results.csv
├── .env
├── README.md
```

---

## Installation

Clone repository:

```bash
git clone <repository-link>
cd outreach_pipeline
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create `.env` file:

```env
EMAIL=your_domain_email
PASSWORD=your_password
SMTP_SERVER=mail.privateemail.com
SMTP_PORT=587
BREVO_API_KEY=your_brevo_api_key
```

---

## Run Project

```bash
python main.py
```

Example input:

```text
google.com
```

---

## Output

The project generates:

* `results.csv`
* Outreach emails via Brevo
* Console output with company data

Example CSV:

```text
Company,Person,Email
amazon.com,CEO John,ceo@meta.com
meta.com,VP Sarah,ceo@meta.com
```

---

## APIs / Services Used

* Ocean API / Similar company lookup
* Prospeo API
* EazyReach API
* Brevo API
* Namecheap Private Email

