import subprocess
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

url = "https://www.wikipedia.org/"
output_file = "new_capture_legit.pcap"

print(f"Starting tshark to capture traffic into: {output_file}")
tshark = subprocess.Popen(
    ["tshark", "-i", "any", "-a", "duration:10", "-w", output_file],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL
)

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)

try:
    driver.get(url)
    time.sleep(10) 
except Exception as e:
    print(f"Error visiting {url}: {e}")
finally:
    driver.quit()
    tshark.terminate()

print("Capture complete. Saved as new_capture.pcap")

