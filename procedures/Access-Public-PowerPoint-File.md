---
tags:
  - pii-leak
  - information-disclosure
  - web
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T17:24:56.470Z'
skill_level: low
impact_level: high
detection_risk: low
sub_techniques: []
id: 75d5b004-de45-44f5-bac7-ee97e286f583
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Access-Public-PowerPoint-File

## Summary

This procedure involves directly accessing and downloading a publicly hosted PowerPoint file from a DoD-related WordPress site, exposing initial entry to sensitive content without any barriers.

## Description

In this attack scenario, the target is a WordPress-hosted website with an unprotected uploads directory. Attackers use a web browser or curl to fetch the PPTX file via its direct URL, gaining immediate access to embedded screenshots of health records. No authentication is required, making this a passive reconnaissance step. Expected outcomes include obtaining the file for further analysis, potentially revealing PII like names and IDs.

## Requirements

1. Internet connectivity to reach the public URL
2. Web browser or command-line tool like curl
3. No special permissions or VPN access needed

## Defense

Defensive measures and detection strategies:

- Implement access controls on file upload directories (e.g., .htaccess restrictions on wp-content/uploads)
- Scan public websites for sensitive file exposures using tools like Google dorks or automated crawlers
- Use file integrity checks and watermarking on sensitive documents

## Objectives

1. Obtain the PPTX file containing health record screenshots
2. Confirm public accessibility without login
3. Prepare for deeper content examination

## Instructions

### Step 1: Locate and Access the File URL

**Context**: Identify the direct link to the PowerPoint file, typically exposed in WordPress media libraries.

No specific command; use a browser to navigate to the URL or curl for download:

```bash
curl -O https://███████/wp-content/uploads/2018/12/HR_TECH_WOBC_Perform_eMILPO_Functions_eMILPO_Brief.pptx
```

> This downloads the file locally. Expected output: A 200 OK response and the PPTX saved.

### Step 2: Verify File Integrity

**Context**: Ensure the file is complete and opens without issues.

Open in PowerPoint:

```bash
# Or use file command to check type:
file HR_TECH_WOBC_Perform_eMILPO_Functions_eMILPO_Brief.pptx
```

> Output: "Zip archive data" confirming it's a valid PPTX.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Hardware]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- pii-leak
- web-access
