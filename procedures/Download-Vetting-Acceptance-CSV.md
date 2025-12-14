---
tags:
  - information-disclosure
  - pii-leak
  - misconfiguration
  - csv-download
  - hackerone
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-download-hackerone-vetting-csv]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:18.090Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 95b72dc9-94c4-4746-a270-89367c171ce2
validated: true
mitre_tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
---
# Download-Vetting-Acceptance-CSV

## Summary

This procedure exploits a misconfiguration in HackerOne's Advanced Vetting system to download CSV files containing PII of users who accepted vetting terms, bypassing program access controls.

## Description

The vulnerability stems from CSV files being publicly downloadable via direct URLs like /program_handle/terms_acceptance_data.csv, even for logged-in users without permissions to the specific programs. Affected programs expose real PII including names, usernames, addresses, and countries, while others use demo data. The attack requires an authenticated session but no further privileges, leading to potential privacy breaches for vetted researchers. HackerOne fixed this by restricting access, but the procedure demonstrates the original flaw.

## Requirements

1. Authenticated HackerOne session (from login procedure)
2. Knowledge of program handles (e.g., █████, █████ – can be guessed or enumerated)
3. HTTP client like curl or browser
4. Write permissions for output file

## Defense

Defensive measures and detection strategies:

- Enforce proper access controls on all endpoints using role-based permissions
- Audit file storage and serving configurations to prevent public exposure
- Log and monitor direct file access requests, alerting on unauthorized downloads
- Use encryption for PII at rest and in transit

## Objectives

1. Retrieve sensitive CSV data without authorization
2. Expose PII for vetted users to demonstrate disclosure risk
3. Validate misconfiguration in multiple programs

## Instructions

### Step 1: Identify Target Endpoint

**Context**: Determine the vulnerable URL using known or enumerated program handles.

Construct the URL as https://hackerone.com/{program_handle}/terms_acceptance_data.csv, e.g., https://hackerone.com/█████/terms_acceptance_data.csv.

### Step 2: Send Authenticated Request

**Context**: Use the session cookie to download the file, exploiting the lack of permission checks.

**Command** ([[commands/curl-download-hackerone-vetting-csv]]):
```bash
curl -H "Cookie: _hackerone_session=XXXXX" -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36" "https://hackerone.com/program_handle/terms_acceptance_data.csv" -o vetting_data.csv
```

> This command sends a GET request mimicking a browser, using the authentication cookie to access the endpoint. Replace 'program_handle' with actual values and 'XXXXX' with the real session cookie from browser dev tools. Expected output is a CSV file download; inspect it to confirm PII presence.

### Step 3: Verify Contents

**Context**: Analyze the downloaded file for PII to confirm successful exploitation.

Open vetting_data.csv in a text editor or spreadsheet tool. Look for columns like 'Name of Finder', 'Username', 'Address (optional)', etc.

**Expected Output**: CSV with user data entries.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery
- [[Collection]] Collection

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used

- [[commands/curl-download-hackerone-vetting-csv]]

## Tools Used

- [[tools/curl]]

## Tags

- information-disclosure
- pii-leak
- misconfiguration
