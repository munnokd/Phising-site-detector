import os
import subprocess
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

df = pd.read_csv("dataset.csv")
os.makedirs("captures", exist_ok=True)

def capture_traffic(url, label, index):
    pcap_file = f"captures/{label}_{index}.pcap"
    tshark = subprocess.Popen(
        ["tshark", "-i", "any", "-a", "duration:10", "-w", pcap_file],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )

    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)

    try:
        driver.get(url)
        time.sleep(10)
    except Exception as e:
        print(f"Error visiting {url}: {e}")
    driver.quit()
    tshark.terminate()

for i, row in df.iterrows():
    print(f"[{i}] Capturing: {row['url']}")
    capture_traffic(row['url'], row['label'], i)

