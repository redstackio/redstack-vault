---
id: 8926b4e6-8e1c-4ea5-8cff-676167efc96b
type: tool
verified: true
created_at: '2019-08-28T21:17:40.296743+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - reconnaissance
  - osint
  - linkedin
  - enumeration
url: 'https://github.com/christian-kingsley/InSpy'
commands:
  - '[[commands/inspy-techspy-enumerate-technologies]]'
  - '[[commands/inspy-empspy-enumerate-employees]]'
  - '[[commands/inspy-show-help]]'
validated: true
---

# inspy

**Status**: Unverified

## Overview

InSpy is a Python-based tool for enumerating information from LinkedIn, primarily used in open-source intelligence (OSINT) and reconnaissance phases of security assessments. It features two main modules: TechSpy for identifying technologies used by a target company through job listings, and EmpSpy for discovering employees by job titles and departments, with optional email address generation.

## Description

InSpy automates the crawling of LinkedIn job postings and employee profiles to gather actionable intelligence. TechSpy matches keywords from job descriptions to a provided list, helping identify tech stacks without direct access to the company. EmpSpy searches for personnel matching specified criteria, which can aid in social engineering or phishing preparations. The tool requires a LinkedIn account for authentication and respects rate limits to avoid detection. It's particularly useful in red teaming for initial reconnaissance on corporate targets.

## Features

- **TechSpy**: Crawls LinkedIn job listings and matches technologies against a custom keyword file.
- **EmpSpy**: Enumerates employees by title and/or department, with email pattern generation.
- **Output Flexibility**: Results can be saved to files for further analysis.
- **Email Generation**: Supports common email formats to hypothesize contact addresses.
- **Cross-Platform**: Runs on any system with Python 3 and required dependencies.

## Installation

### Requirements

- Python 3.6+
- pip
- LinkedIn account credentials (for authentication)

### Install Commands

```bash
# Clone the repository
git clone https://github.com/christian-kingsley/InSpy.git
cd InSpy

# Install dependencies
pip3 install -r requirements.txt

# For Kali/Ubuntu (if git and pip not installed)
sudo apt update && sudo apt install git python3-pip -y
```

On macOS with Homebrew:

```bash
brew install git python3
# Then follow the clone and pip steps above
```

## Basic Usage

```python
python3 inspy.py -h
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| techspy | Run technology enumeration mode |
| empspy | Run employee enumeration mode |

## Examples

### Example 1: Basic Usage (TechSpy)

Prepare a keywords file (technologies.txt) with one tech per line, e.g.:

Java
Python
AWS

Then run:

```python
python3 inspy.py techspy -c "Target Company" -k technologies.txt
```

### Example 2: Advanced Usage (EmpSpy)

Prepare titles.txt:

Software Engineer
DevOps Engineer

And run:

```python
python3 inspy.py empspy -c "Target Company" -t titles.txt --email-format "first.last@target.com"
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Code Repositories]] Search Open Websites and Services: Code Repositories (adapted for social media enumeration)
- [[Email Addresses]] Gather Victim Identity Information: Employee Accounts

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

- Monitor for automated LinkedIn scraping via browser automation signatures (e.g., Selenium WebDriver user agents).
- LinkedIn rate limiting or CAPTCHA triggers on suspicious account activity from security tools.
- Network logs showing repeated requests to linkedin.com from reconnaissance tools.
- Employee reports of unusual profile views or connection requests.

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

- Official GitHub: https://github.com/christian-kingsley/InSpy
- LinkedIn Terms of Service (scraping restrictions)
- OSINT Framework: https://osintframework.com/
