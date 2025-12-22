---
id: df44fbdb-2117-4909-ac75-1eaa8c36b7bd
name: ScrapedIn
type: tool
verified: true
created_at: '2019-08-28T21:17:27.311296+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - osint
  - reconnaissance
  - linkedin
  - scraping
url: 'https://github.com/dchrastil/ScrapedIn'
validated: true
---

# ScrapedIn

**Status**: Unverified

## Overview

ScrapedIn is an open-source Python tool designed for scraping LinkedIn data without relying on the official API, enabling unrestricted reconnaissance of profiles, companies, and search results. It uses Selenium for browser automation to bypass anti-scraping measures, making it useful for OSINT operations in red teaming and threat intelligence gathering.

## Description

ScrapedIn automates the extraction of LinkedIn information such as user profiles (experience, skills, education), company details, and search results for people or jobs. It handles login sessions, cookies, and headless browsing to simulate human interaction, reducing detection risks. Commonly used in the reconnaissance phase to map organizational structures, identify key personnel, and gather contact information for social engineering or phishing campaigns.

## Features

- Feature 1: Profile scraping with detailed extraction of professional history and connections.
- Feature 2: Advanced search capabilities for targeting specific roles or companies.
- Feature 3: Export options in JSON/CSV for easy integration with other tools.
- Feature 4: Support for authenticated sessions via cookies to access restricted data.
- Feature 5: Headless mode for stealthy operation without visible browser windows.

## Installation

### Requirements

- Python 3.6+
- Selenium library
- Chrome browser and ChromeDriver
- Optional: LinkedIn cookies for authenticated access

### Install Commands

```bash
# Clone the repository
git clone https://github.com/dchrastil/ScrapedIn.git
cd ScrapedIn

# Install dependencies
pip install -r requirements.txt

# Download ChromeDriver (match your Chrome version)
# Available from https://chromedriver.chromium.org/
```

For Ubuntu/Kali:
```bash
sudo apt update
sudo apt install python3-pip chromium-browser
pip3 install selenium
```

## Basic Usage

```bash
tool-name --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| --headless | Run in headless mode |
| --cookies COOKIES_FILE | Load session cookies from file |
| --output FILE | Specify output file format (json/csv) |

## Examples

### Example 1: Basic Usage

```bash
scrapedin --profile https://www.linkedin.com/in/target-user
```

### Example 2: Advanced Usage

```bash
scrapedin --search "security team at example.com" --limit 10 --output results.json --headless
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Search Open Websites-Domains]] Search Open Websites and Services
- [[Email Addresses]] Gather Victim Identity Information: Email Addresses

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual browser automation patterns in network traffic (Selenium WebDriver signatures).
- Detection method 2: High volume of LinkedIn requests from a single IP without API keys.
- Detection method 3: Presence of ChromeDriver processes or temporary profile directories.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/theHarvester]]
- [[LinkedIn-OSINT-Tools]]

## References

- Official GitHub: https://github.com/dchrastil/ScrapedIn
- Selenium Documentation: https://www.selenium.dev/documentation/
