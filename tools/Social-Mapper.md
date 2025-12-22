---
type: tool
description: >-
  OSINT tool for automated social media profile mapping using names and facial
  recognition across multiple platforms.
url: 'https://github.com/BlueTeamTools/SocialMapper'
tags:
  - osint
  - reconnaissance
  - social-media
  - selenium
platforms:
  - Linux
  - Windows
  - macOS
verified: true
validated: true
---

# Social-Mapper

**Status**: Unverified

## Overview

Social Mapper is an open-source intelligence (OSINT) tool designed for mapping and correlating individuals across social media platforms. It automates the process of searching for targets using either a list of names or images with facial recognition, operating at scale without API limitations by leveraging Selenium for browser automation. Commonly used in reconnaissance phases to build target profiles for security assessments or investigations.

## Description

The tool instruments a web browser to perform searches on sites like LinkedIn, Twitter (X), Facebook, Instagram, and others. For name-based searches, it queries user directories; for images, it integrates facial recognition to identify matching profiles. It supports login to authenticated sites and generates comprehensive HTML reports with matched results, confidence levels, screenshots, and direct links to profiles. This makes it valuable for linking disparate online identities and aiding in target correlation during red teaming or threat intelligence gathering.

## Features

- Feature 1: Name-based searching across 10+ social media sites without API restrictions
- Feature 2: Facial recognition for image uploads to match real-world photos to profiles
- Feature 3: Automated browser control via Selenium with support for headless mode
- Feature 4: Customizable site selection and report generation with visual aids
- Feature 5: Multi-threaded operation for faster large-scale searches

## Installation

### Requirements

- Python 3.6 or higher
- Google Chrome browser
- ChromeDriver (matching Chrome version)
- OpenCV and other image processing libraries

### Install Commands

```bash
# Clone the repository
git clone https://github.com/BlueTeamTools/SocialMapper.git
cd SocialMapper

# Install Python dependencies
pip install -r requirements.txt

# Ensure ChromeDriver is in PATH (download from https://chromedriver.chromium.org/)
# Example for Ubuntu: sudo apt install chromium-chromedriver
```

## Basic Usage

```bash
python socialmapper.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -f, --file | Specify input file with names (one per line) |
| -i, --images | Specify folder with images for facial search |
| -s, --sites | Comma-separated sites to search (e.g., linkedin,facebook) |
| -e, --email | Email for site authentication |
| -p, --password | Password for authentication |
| --headless | Run browser in headless mode |
| --confidence | Minimum confidence threshold for matches (default: 50) |

## Examples

### Example 1: Basic Usage

```bash
python socialmapper.py -f names.txt -s linkedin,twitter -e user@example.com -p password
```

### Example 2: Advanced Usage

```bash
python socialmapper.py -i images_folder/ -s facebook,instagram --headless --confidence 70 -e user@example.com -p password
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Gather Victim Org Information]] Gather Victim Identity Information
- [[Email Addresses]] Gather Victim Identity Information: Email Addresses

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Selenium WebDriver signatures in browser user agents or network requests (e.g., CDP endpoints)
- Detection method 2: Unusual patterns of automated logins and searches on social media platforms from the same IP
- Detection method 3: High-volume profile queries or image uploads triggering rate limits or anomaly detection on sites like LinkedIn

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
- [[tools/Maltego]]

## References

- Official GitHub Repository: https://github.com/BlueTeamTools/SocialMapper
- Author: Jacob Wilkin (@sitedude)
- Documentation: Included in repo README
