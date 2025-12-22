---
tags:
  - form-submission
  - document-access
  - stored-file
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
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T03:46:37.439Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 15748c59-132b-4c4f-b9ed-1fe7a1fa56a8
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Submit-Request-and-Access-Details

## Summary

This procedure submits the request form with the uploaded file, generates a document number, and accesses the request details page to locate the stored malicious file link.

## Description

Following the upload in an XPages-based application, submitting the form stores the HTML payload server-side and returns a unique 14-digit Document Number. Navigating to the ModifyRequest.xsp endpoint with this number displays the full request details, including a clickable link to the uploaded file at the bottom. This step bridges upload to exploitation without authentication, assuming the file is persisted in a viewable format.

## Requirements

1. Completed form with file attached
2. Generated Document Number post-submission
3. Access to the ModifyRequest.xsp page

## Defense

Defensive measures and detection strategies:

- Validate all submissions server-side and quarantine suspicious files
- Require authentication for request modification views
- Audit logs for document number access patterns

## Objectives

1. Persist the malicious file via form submission
2. Retrieve and view the request details page
3. Identify the uploaded file link for next exploitation

## Instructions

### Step 1: Submit the Form

**Context**: Process the request to store the payload.

Click the 'submit request' button on the form page.

> A 14-digit Document Number is displayed or logged upon success.

### Step 2: Navigate to Modification Page

**Context**: Use the document number to access details.

In the browser, go to the ModifyRequest.xsp endpoint and input the Document Number.

> Request details page loads, showing form data and attachments.

### Step 3: Locate Uploaded File

**Context**: Find the link to the stored file.

Scroll to the bottom of the details page to see the 'unsure1.html' file link.

> File is listed and clickable, confirming storage.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[form-submission]]
- [[document-access]]
