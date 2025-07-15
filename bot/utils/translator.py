languages = {
    "en": {
        "categories": "Categories",
        "contact": "Contact",
        "rate": "Rate",
        "rating_thanks": "Thanks for your rating!",
        "open_store": "Open Store",
        # Add more UI strings here
    },
    "am": {
        "categories": "ምድቦች",
        "contact": "አግኙ",
        "rate": "ደረጃ ስጡ",
        "rating_thanks": "ስለ ደረጃዎ እናመሰግናለን!",
        "open_store": "ሱቅን ክፈት",
    },
    # Add more languages here
}

def translate(lang, key):
    return languages.get(lang, languages["en"]).get(key, key)
