import requests
import certifi
import os

certificate_url = "https://gu-st.ru/content/Other/doc/russian_trusted_root_ca.cer"
certifi_path = certifi.where()

try:
    response = requests.get(certificate_url)
    response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

    certificate_content = response.text + "\n"  # Add newline

    with open(certifi_path, "a") as f:
        f.write(certificate_content)

    print(f"Successfully appended certificate from {certificate_url} to {certifi_path}")

except requests.exceptions.RequestException as e:
    print(f"Error downloading certificate: {e}")
except Exception as e:
    print(f"An error occurred: {e}")