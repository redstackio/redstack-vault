---
id: proc-uuid-2
tags:
  - xss
  - reflected-xss
  - nextcloud
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-05T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:23.534Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Rename-Error-to-Reflect-Payload

## Summary

This procedure simulates or induces a victim to attempt renaming the malicious file with an invalid input, causing Nextcloud to reflect the original payload in an unsanitized error message, executing the XSS.

## Description

Nextcloud's rename error handling fails to escape filenames, allowing reflected XSS. By entering an invalid character like a backslash in the rename field, the system displays an error echoing the original malicious name. This occurs in the victim's browser context, potentially leading to JavaScript execution for data theft or actions on behalf of the user. Prerequisites include victim access to the file and the malicious file already present.

## Requirements

1. Victim authenticated in Nextcloud with rename permissions
2. Access to the folder containing the malicious file
3. Web browser to perform the rename action

## Defense

Defensive measures and detection strategies:

- Sanitize all reflected user input in error messages, especially filenames
- Log and alert on rename attempts with invalid characters
- Use output encoding (e.g., HTML entity encoding) for dynamic content

## Objectives

1. Force reflection of the malicious payload
2. Execute XSS in victim session
3. Enable arbitrary JavaScript for impact

## Instructions

### Step 1: Locate the Malicious File

**Context**: Identify the target file as the victim user.

Browse to the shared folder and select the file named `<img src=x onerror=prompt(1)>.jpg`.

### Step 2: Attempt Invalid Rename

**Context**: Input invalid data to trigger the error and reflection.

Right-click the file, select "Rename", and enter a name like `newname.jpg\` (appending backslash for invalidity). Submit the rename.

> The error message will reflect the original filename unsanitized, injecting the `<img>` tag and triggering onerror.

**Expected Output**: Error dialog showing the payload, with potential JavaScript alert if CSP allows.

### Step 3: Observe Execution

**Context**: Confirm the XSS fires.

Check browser console for errors or alerts; if prompt(1) appears, execution succeeded.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- reflected-xss
- error-handling
