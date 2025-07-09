import requests
import pandas as pd

def fetch_phishing_urls():
    url = "https://openphish.com/feed.txt"
    try:
        response = requests.get(url)
        phishing_urls = response.text.splitlines()
        return phishing_urls[:40]  # Use only first 40
    except:
        return []

def fetch_legit_urls():
    return [
        "https://www.google.com", "https://www.wikipedia.org", "https://www.bbc.com",
        "https://www.nytimes.com", "https://www.microsoft.com", "https://www.apple.com",
        "https://www.amazon.com", "https://www.github.com", "https://www.stackoverflow.com",
        "https://www.reddit.com", "https://www.linkedin.com", "https://www.medium.com",
        "https://www.mozilla.org", "https://www.quora.com", "https://www.deeplearning.ai",
        "https://www.ibm.com", "https://www.dropbox.com", "https://www.salesforce.com",
        "https://www.airbnb.com", "https://www.netflix.com",
    ] * 2

phishing = fetch_phishing_urls()
legit = fetch_legit_urls()
df = pd.DataFrame({
    'url': phishing + legit,
    'label': [1]*len(phishing) + [0]*len(legit)
})
df.to_csv("dataset.csv", index=False)
print("Created dataset.csv with", len(df), "entries.")

