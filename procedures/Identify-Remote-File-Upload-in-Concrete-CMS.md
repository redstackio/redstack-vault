---
tags:
  - ssrf
  - concrete-cms
  - recon
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
updated_at: '2025-12-14T04:39:09.904Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 55980c9e-d8fa-459d-841a-c589086b86ad
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify Remote File Upload in Concrete CMS

## Summary

This procedure involves locating the file upload functionality in Concrete CMS that supports fetching files from remote URLs, setting the stage for SSRF exploitation.

## Description

In Concrete CMS, the file upload feature allows administrators or users to specify a remote URL for the system to fetch and upload files automatically. This is implemented in the backend via PHP, making it vulnerable to SSRF if not properly restricted. The procedure requires access to the CMS dashboard and basic testing to confirm remote fetch behavior, typically in a web-based environment hosted on AWS.

## Requirements

1. Access to Concrete CMS instance (user session)
2. Web browser or API testing tool
3. Knowledge of CMS file management interface

## Defense

Defensive measures and detection strategies:

- Disable remote URL uploads or whitelist domains
- Implement URL parsing to block internal IPs
- Log all remote fetch attempts for anomaly detection

## Objectives

1. Confirm presence of remote URL upload capability
2. Understand fetch mechanism for exploitation planning
3. Identify potential SSRF entry point

## Instructions

### Step 1: Access File Upload Interface

**Context**: Navigate to the file manager in Concrete CMS dashboard.

No specific command; use the web interface to select 'Upload File' and look for remote URL option.

> Expected: Option to paste a URL for remote fetch.

### Step 2: Test with Harmless External URL

**Context**: Verify the server fetches external content.

Provide a public image URL (e.g., https://example.com/image.jpg) in the remote URL field and submit.

> Expected: File uploaded successfully from remote source, confirming SSRF vector.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[ssrf]]
- [[concrete-cms]]
