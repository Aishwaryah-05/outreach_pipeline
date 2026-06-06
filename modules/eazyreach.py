# Fallback implementation used because API access or credits unavailable
def get_email(linkedin):

    company = linkedin.split("/")[-2]

    username = linkedin.split("/")[-1]

    company = company.replace(".com", "")

    return f"{username}@{company}.com"