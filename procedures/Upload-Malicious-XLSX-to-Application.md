---
tags:
  - xxe
  - file-upload
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands: []
platforms:
  - Web
  - AWS
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 6514ae03-3ca7-4e72-aa89-f6d64829c350
created_at: '2025-12-13T09:00:28.074Z'
updated_at: '2025-12-13T09:00:28.074Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Upload Malicious XLSX to Application

## Summary

This procedure covers uploading a modified XLSX file to trigger XXE exploitation and disclose sensitive data in the application response.

## Description

The target application at https://rev-app.informatica.com parses the uploaded XLSX, resolving entities and displaying file contents, leading to disclosure on Linux-based AWS instances.

## Requirements

1. Modified XLSX with XXE payload
2. Access to the web application
3. Ability to create projects and import files

## Defense

Defensive measures and detection strategies:

- Implement strict input validation for uploaded files
- Log and alert on anomalous XML parsing behaviors

## Objectives

1. Trigger XML parsing
2. Disclose sensitive files
3. Confirm vulnerability exploitation

## Instructions

### Step 1: Create Project and Upload

**Context**: Interact with the web interface to upload the file.

Visit https://rev-app.informatica.com, create a new project, and select the import option to upload the modified XLSX. Observe the response for disclosed data.

> The application will process the XML and reveal /etc/passwd.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[xxe]]
- [[file-upload]]
