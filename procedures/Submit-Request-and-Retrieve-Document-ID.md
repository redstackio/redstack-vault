---
id: proc-003
tags:
  - form-submit
  - document-retrieval
  - id-extraction
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:32.397Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Submit-Request-and-Retrieve-Document-ID

## Summary

Submit the upload form to persist the malicious file and extract the unique 14-digit Document Number needed for accessing the stored attachment.

## Description

Post-upload, submission triggers server-side storage in the application's database or file system. Navigate to ModifyRequest.xsp to input the ID, which is generated upon success. This bridges upload to exploitation. Outcomes: File linked to a retrievable document for viewing.

## Requirements

1. Completed form with attached file
2. Access to post-submission pages
3. Ability to note the Document Number from response

## Defense

Defensive measures and detection strategies:

- Audit logs for submission patterns and flag anomalous file names
- Require approval workflows for requests with attachments

## Objectives

1. Persist the uploaded payload
2. Obtain access identifier (Document ID)
3. Enable retrieval without authentication bypass

## Instructions

### Step 1: Submit the Form

**Context**: Process the request to store data.

Click 'submit request' button.

> Expect success message or redirect; note any Document Number in URL or body.

### Step 2: Navigate to Modification Page

**Context**: Access the request editor.

Go to `https://target.com/ModifyRequest.xsp`.

> Page loads with input field for Document Number.

### Step 3: Enter and View Document

**Context**: Use ID to confirm storage.

Input the 14-digit number and submit.

> Success: Request details page loads, showing attachments.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[form-submit]]
- [[document-retrieval]]
