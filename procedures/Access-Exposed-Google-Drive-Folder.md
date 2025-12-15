---
tags:
  - information-disclosure
  - pii-exposure
  - misconfiguration
  - google-drive
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:18.161Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: aab60359-ee18-4c8a-b141-cbe913491152
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Exposed-Google-Drive-Folder

## Summary

This procedure demonstrates how to exploit a public Google Drive misconfiguration linked from a government website, allowing unauthorized access to sensitive folders containing PII and operational documents. It targets read-only webpages with embedded public links, leading to information disclosure without authentication.

## Description

In this scenario, a U.S. Department of Defense website hosts a read-only page with an embedded link to a Google Drive folder set to public access. Navigating the site and following the link grants access to subfolders like "█████ Internal" and "Orders," where PDFs disclose military personnel details such as names, SSNs, addresses, marital status, dependents, and security clearances. This misconfiguration violates privacy laws like the U.S. Privacy Act and enables risks like identity theft. The procedure requires only a web browser and internet access, with no technical exploits needed.

## Requirements

1. Web browser with JavaScript enabled
2. Internet connectivity to access public DoD and Google sites
3. No credentials or special permissions

## Defense

Defensive measures and detection strategies:

- Regularly audit public-facing websites for embedded third-party links (e.g., Google Drive)
- Configure cloud storage sharing to "restricted" or require authentication
- Implement content security policies (CSP) to prevent unintended link exposure
- Monitor access logs for anomalous traffic to shared folders
- Use DLP tools to scan for PII in cloud storage

## Objectives

1. Gain unauthorized access to sensitive military documents
2. Extract PII for potential misuse (e.g., fraud, doxxing)
3. Demonstrate impact of public misconfigurations on operational security

## Instructions

### Step 1: Navigate to the Target DoD Page

**Context**: Start by accessing the publicly available read-only page on the DoD site where the vulnerable link is embedded.

No specific command required; use browser navigation.

> Open https://██████.aspx?Mode=ReadOnly&Id=90dd0d3b-0ed1-e76b-128f-11ebc799ba55 in your browser. The page should load without login.

### Step 2: Locate and Access the Google Drive Link

**Context**: Identify the public link below the page content and follow it to the exposed folder.

No specific command required; manual browsing.

> Scroll down the page to find https://drive.google.com/drive/folders/█████████ and click it. The folder opens publicly.

### Step 3: Navigate Subfolders and Access PDFs

**Context**: Drill down into internal directories to reach sensitive files.

No specific command required; folder navigation.

> In the main folder, open "█████ Internal," then "Orders," and view PDFs. Documents will display PII like SSNs and addresses.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- information-disclosure
- pii-exposure
- misconfiguration
- google-drive
