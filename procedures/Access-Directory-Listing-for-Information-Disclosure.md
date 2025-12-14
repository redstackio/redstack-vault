---
tags:
  - information-disclosure
  - directory-listing
  - reconnaissance
  - web
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-directory-listing-access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:24:56.137Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 2e3b5567-9888-4a06-a212-eb6ed6232795
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Access-Directory-Listing-for-Information-Disclosure

## Summary

This procedure exploits enabled directory listing on a web server, such as Apache hosting ownCloud, to disclose internal file structures and contents without authentication. It is commonly used in reconnaissance to gather information about application directories, configurations, and potential sensitive files like readme.md in development environments.

## Description

In this attack scenario, the target is a development or staging server for ownCloud where directory listing is inadvertently enabled, allowing unauthenticated users to view and access file listings via a direct URL. By navigating to a specific path like /enterprise/apps/, attackers can enumerate files, download documents such as readme.md, and extract details about internal application structures or configurations. This low-complexity technique poses a medium impact by potentially revealing proprietary information, though it does not grant code execution or direct system access. Prerequisites include public accessibility of the endpoint and no additional protections like .htaccess restrictions.

## Requirements

1. Internet connectivity to reach the target URL
2. A web browser or command-line tool like curl for accessing the endpoint
3. Knowledge of the target path (e.g., inferred from application structure like /apps/ in ownCloud)

## Defense

Defensive measures and detection strategies:

- Disable directory listing in web server configurations (e.g., Apache's Options -Indexes)
- Implement proper access controls and authentication on development/staging environments
- Use web application firewalls (WAF) to block anomalous directory access attempts
- Monitor server logs for unusual GET requests to directory paths

## Objectives

1. Enumerate and disclose internal directory contents
2. Extract sensitive files like configuration readmes
3. Gather intelligence on application structure for further attacks

## Instructions

### Step 1: Identify and Access the Directory Endpoint

**Context**: Determine the vulnerable URL based on the application's known structure (e.g., ownCloud's /apps/ path) and directly request it to trigger the directory listing.

**Command** ([[commands/curl-directory-listing-access]]):
```bash
curl -s https://daily.owncloud.com/enterprise-stable8/enterprise/apps/ | html2text
```

> This command silently fetches the directory listing and converts the HTML to readable text. Expected output includes a list of files and subdirectories, such as readme.md, revealing internal details like app configurations or development notes.

### Step 2: Review and Download Exposed Files

**Context**: Once the listing is obtained, inspect for sensitive files and download them for analysis.

**Command** ([[commands/curl-directory-listing-access]]):
```bash
curl -O https://daily.owncloud.com/enterprise-stable8/enterprise/apps/readme.md
```

> Downloads the readme.md file directly. Expected output is the file saved locally, containing potential leaks like setup instructions or config snippets.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-directory-listing-access]]

## Tools Used


## Tags

- information-disclosure
- directory-listing
- reconnaissance
