from modules.email_sender import send_email
from modules.ocean import get_similar_companies
from modules.prospeo import get_decision_makers
from modules.eazyreach import get_email

domain = input("Enter company domain: ")

companies = get_similar_companies(domain)

print("\nSimilar Companies:")

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
send_email(
    "aishwaryah825@gmail.com",
    "Testing Outreach",
    "Hello, outreach pipeline working!"
)