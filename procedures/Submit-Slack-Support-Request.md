---
tags:
  - csrf
  - form-submission
  - slack
type: procedure
tools:
  - '[[tools/Tamper-Data]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:22.858Z'
sub_techniques: []
id: f8f340c2-a5dd-4dc4-ae7d-88873d4971d9
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Submit-Slack-Support-Request

## Summary

This procedure simulates a legitimate form submission in Slack's help system to trigger the HTTP POST request for vulnerability inspection.

## Description

Submitting the support request form generates the exact request that an attacker could forge in a CSRF attack. With Tamper Data active, this step captures the payload, highlighting the lack of anti-CSRF tokens and enabling confirmation of the vulnerability's exploitability for unauthorized submissions.

## Requirements

1. Loaded form page from previous access step
2. Tamper Data actively capturing traffic
3. Sample data for form fields (non-sensitive)

## Defense

Defensive measures and detection strategies:

- Enforce CSRF tokens in all state-changing forms
- Rate-limit support request submissions

## Objectives

1. Generate the POST request for analysis
2. Ensure interception occurs without alteration
3. Validate form functionality

## Instructions

### Step 1: Fill Form Fields

**Context**: Provide input to mimic a real request.

Enter a description (e.g., "Test support issue") and any optional fields like attachments or category.

> This populates the form data that will be sent in the POST body.

**Expected Output**: Fields filled, submit button enabled.

### Step 2: Initiate Submission

**Context**: Trigger the request while monitored.

Click the "Submit" or "Create Request" button.

> Tamper Data intercepts the request, pausing for review.

**Expected Output**: Interception dialog appears with request details.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Tamper-Data]]

## Tags

- [[csrf]]
- [[submission]]
