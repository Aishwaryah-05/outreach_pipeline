def get_decision_makers(company):

    print(
        "Finding decision makers for:",
        company
    )

    return [

        {
            "name": "CEO",
            "linkedin": f"https://linkedin.com/{company}/ceo"
        },

        {
            "name": "VP Sales",
            "linkedin": f"https://linkedin.com/{company}/vp-sales"
        }

    ]