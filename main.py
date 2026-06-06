from modules.ocean import get_similar_companies
from modules.prospeo import get_decision_makers
from modules.eazyreach import get_email
from modules.brevo import send_brevo_email

domain = input("Enter company domain: ")

companies = get_similar_companies(domain)

print("\nSimilar Companies:")

# Create CSV with fresh header
with open("results.csv", "w") as f:
    f.write("Company,Person,Email\n")

all_contacts = []

seen_emails = set()

for company in companies:

    print("\nCompany:", company)

    people = get_decision_makers(company)

    for person in people:

        try:

            email = get_email(
                person["linkedin"]
            )

        except Exception as e:

            print(
                "Email fetch failed:",
                e
            )

            continue

        # Deduplication
        if email in seen_emails:

            continue

        seen_emails.add(email)

        print(

            person["name"],
            "-",
            person["linkedin"],
            "-",
            email

        )

        # Save CSV
        with open("results.csv", "a") as f:

            f.write(

                f"{company},{person['name']},{email}\n"

            )

        all_contacts.append(

            {

                "company": company,

                "name": person["name"],

                "email": email

            }

        )

# Summary checkpoint
print("\nSUMMARY BEFORE SENDING\n")

for contact in all_contacts:

    print(

        contact["company"],
        "-",
        contact["name"],
        "-",
        contact["email"]

    )

confirm = input(

    "\nSend emails now? (yes/no): "

)

if confirm.lower() == "yes":

    for contact in all_contacts:

        message = f"""
Hi {contact['name']},

I found {contact['company']} while researching companies in your industry.

I would love to connect and explore opportunities together.

Regards,
Aishwarya
"""

        try:

            send_brevo_email(

                "aishwaryah825@gmail.com",

                f"Opportunity for {contact['company']}",

                message

            )

            print(

                "Email Sent ->",

                contact["name"]

            )

        except Exception as e:

            print(

                "Failed sending email:",

                e

            )

else:

    print(

        "Emails skipped"

    )

print(

    "\nPipeline Completed Successfully!"

)