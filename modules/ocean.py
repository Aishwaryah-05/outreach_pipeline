def get_similar_companies(domain):

    print(
        "Searching similar companies for:",
        domain
    )

    sample_data = {

        "google.com": [
            "amazon.com",
            "microsoft.com",
            "meta.com"
        ],

        "apple.com": [
            "samsung.com",
            "sony.com",
            "xiaomi.com"
        ],

        "netflix.com": [
            "primevideo.com",
            "disneyplus.com",
            "hulu.com"
        ]
    }

    return sample_data.get(
        domain,
        ["company1.com","company2.com"]
    )