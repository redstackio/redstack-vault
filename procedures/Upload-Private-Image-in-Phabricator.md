---
tags:
  - phabricator
  - file-upload
  - privacy
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 8d69ca32-7a61-44d7-9595-b1a74422a811
created_at: '2025-12-14T05:32:13.532Z'
updated_at: '2025-12-14T05:32:13.533Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Upload-Private-Image-in-Phabricator

## Summary

This procedure demonstrates uploading an image file to Phabricator with private visibility settings, simulating the handling of sensitive data like PII-containing images, as a precursor to exploiting access control flaws.

## Description

In Phabricator, the file upload feature allows users to restrict access to uploaded files. This procedure involves navigating to the upload interface, selecting a private image (e.g., a passport scan), and setting visibility to 'no one' or 'just you'. This sets up the scenario for subsequent transformations that bypass these controls, leading to unintended public exposure. The target environment is a standard Phabricator web application, requiring only authenticated access. Expected outcomes include a privately stored file that appears secure but is vulnerable to transformation-induced leaks.

## Requirements

1. Authenticated Phabricator user account with upload permissions
2. Web browser with access to the Phabricator instance (e.g., https://phabricator.allizom.org)
3. A test image file containing mock sensitive data

## Defense

Defensive measures and detection strategies:

- Enforce strict visibility policies on all file transformations
- Monitor transformation API calls for private files
- Implement user notifications for ownership changes in derived files

## Objectives

1. Securely upload an image while maintaining privacy
2. Verify initial access restrictions
3. Prepare for vulnerability exploitation in transformations

## Instructions

### Step 1: Navigate to Upload Page

**Context**: Access the Phabricator file upload interface to begin the process.

Navigate to https://phabricator.allizom.org/file/upload/ in your web browser.

> This loads the upload form where files can be selected and visibility configured.

### Step 2: Select and Upload File

**Context**: Choose a private image and apply restrictive visibility to ensure initial privacy.

Select an image file (e.g., private.jpg) and set visibility to 'no one' or 'just you' before submitting the upload.

> Upon success, the file is stored privately, with access limited to the uploader.

### Step 3: Confirm Upload

**Context**: Verify the file's private status post-upload.

Check the file details page to confirm visibility settings are applied correctly.

> Expected: File shows as private with no public links.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[phabricator]]
- [[file-upload]]
- [[privacy]]
