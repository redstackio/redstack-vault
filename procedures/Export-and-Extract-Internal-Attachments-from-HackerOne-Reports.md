---
tags:
  - information-disclosure
  - web
  - hackerone
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Data from Information Repositories]]'
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 5835cf9b-85e7-4608-8624-593c5ccfa894
created_at: '2025-12-11T03:47:47.741Z'
updated_at: '2025-12-11T03:47:47.741Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0007]]'
  - '[[TA0009]]'
mitre_techniques:
  - '[[T1213]]'
  - '[[T1190]]'
---
# Export and Extract Internal Attachments from HackerOne Reports

## Summary

This procedure exploits a vulnerability in HackerOne's 'Export as .zip' feature to download and extract internal or removed attachments from disclosed reports, leading to unauthorized information disclosure.

## Description

The attack targets the report export functionality on HackerOne, where internal attachments visible only to team members or removed from public view are inadvertently included in the exported zip file. This can reveal confidential information, such as images or files with identifiers like {F134909}. The procedure is web-based and requires no special tools beyond a browser and file extraction capability. It was demonstrated on a specific report (https://hackerone.com/reports/182358) but could apply to others. Expected outcomes include access to non-public attachments, potentially leading to further reconnaissance or data exfiltration.

## Requirements

1. Access to a web browser
2. Publicly disclosed HackerOne report URL
3. Basic file extraction utility (built-in to most OS)

## Defense

Defensive measures and detection strategies:

- Implement proper filtering in export features to exclude internal files
- Monitor for unusual export activities on report pages

## Objectives

1. Gain unauthorized access to internal attachments
2. Demonstrate information disclosure vulnerability
3. Collect potentially confidential data

## Instructions

### Step 1: Navigate to the Target Report Page

**Context**: Access the disclosed report to begin the export process.

Visit the report URL: https://hackerone.com/reports/182358

> This loads the report page where the export feature is available.

### Step 2: Export the Report as a Zip File

**Context**: Use the export feature to download the report contents.

Click the 'Export as .zip' button on the report page.

> This downloads a zip file containing the report and attachments, including internal ones.

### Step 3: Extract the Downloaded Zip File

**Context**: Unpack the zip to view files.

Use a file manager or utility to extract HackerOne_Report-security#182358.zip.

> Extraction reveals all included files, including those not publicly visible.

### Step 4: Observe the Presence of Unauthorized Attachments

**Context**: Inspect extracted files for internal content.

Review the extracted directory for removed or internal attachments, such as images with lingering references.

> Confirm presence of unauthorized files to validate the disclosure.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]
- [[Collection]]

### Techniques

- [[Data from Information Repositories]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- #information-disclosure
- #web
- #hackerone
