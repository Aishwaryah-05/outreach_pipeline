from modules.ocean import get_similar_companies
from modules.prospeo import get_decision_makers
from modules.eazyreach import get_email
from modules.brevo import send_brevo_email

domain = input("Enter company domain: ")

companies = get_similar_companies(domain)

print("\nSimilar Companies:")

# Create CSV header
with open("results.csv", "w") as f:
    f.write("Company,Person,Email\n")

for company in companies:

    print("\nCompany:", company)

    people = get_decision_makers(company)

    for person in people:

        email = get_email(person["linkedin"])

        print(
            person["name"],
            "-",
            person["linkedin"],
            "-",
            email
        )

        # Save results into CSV
        with open("results.csv", "a") as f:
            f.write(
                f"{company},{person['name']},{email}\n"
            )

# Test one email only
send_brevo_email(
    "aishwaryah825@gmail.com",
    "Brevo Test",
    "This email was sent using Brevo API successfully."
)


