import os
from pathlib import Path

# Define the directory and file path
workflow_dir = Path(".github/workflows")
yaml_file = workflow_dir / "selenium-ci.yml"

# Create the directory if it doesn't exist
workflow_dir.mkdir(parents=True, exist_ok=True)

# Define the YAML content
yaml_content = """\
name:  Run Selenium Tests

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  selenium-test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'

      - name: Install Dependencies
        run: |
          pip install selenium
          sudo apt update
          sudo apt install -y wget unzip

      - name:  Install Chrome and ChromeDriver
        run: |
          wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
          sudo dpkg -i google-chrome-stable_current_amd64.deb || sudo apt-get -f install -y
          CHROME_VERSION=$(google-chrome --version | awk '{print $3}' | cut -d '.' -f1)
          wget https://chromedriver.storage.googleapis.com/${CHROME_VERSION}.0.0/chromedriver_linux64.zip
          unzip chromedriver_linux64.zip
          sudo mv chromedriver /usr/local/bin/

      - name:  Run Selenium Tests
        run: python test_selenium.py
"""

# Create and write the YAML file
yaml_file.write_text(yaml_content)

print(f"✅ GitHub Actions workflow file created: {yaml_file}")
