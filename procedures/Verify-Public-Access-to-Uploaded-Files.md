---
id: proc-verify-access-filecloud
tags:
  - access-verification
  - public-hosting
  - filecloud
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:10.209Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify-Public-Access-to-Uploaded-Files

## Summary

This procedure confirms that uploaded files are accessible without authentication, validating the vulnerability's impact for public hosting on the .mil domain.

## Description

After uploads, files in shared directories become publicly readable via direct URLs. Even after partial remediation blocking writes, read access persists, allowing retrieval of sensitive or malicious content. This step tests direct links and UI visibility to assess ongoing exposure.

## Requirements

1. Successful file uploads from prior procedure
2. Browser or incognito mode for verification
3. Target domain details

## Defense

Defensive measures and detection strategies:

- Revoke public read access on shared folders post-remediation
- Implement access logs and anomaly detection for direct file requests
- Use URL signing or expiration for shared links
- Scan hosted files periodically for malware

## Objectives

1. Validate unauthenticated read access to uploaded content
2. Confirm hosting on trusted domain
3. Assess remediation effectiveness

## Instructions

### Step 1: Access Directory Listing

**Context**: Reload the public mode UI to check file visibility.

No command required.

Navigate back to the endpoint URL and refresh.

> Expected output: Uploaded files listed without login.

### Step 2: Test Direct File Access

**Context**: Construct and visit direct URLs for files to verify download.

No command required.

Right-click a file, copy link (e.g., https://target.mil/path/to/file.exe), and open in new tab/incognito.

> File downloads or displays. Success if accessible publicly; post-fix, reads may still work while writes fail.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- access-verification
- public-hosting
- filecloud
