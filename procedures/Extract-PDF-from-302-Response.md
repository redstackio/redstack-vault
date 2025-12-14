---
id: proc-uuid-004
tags:
  - extraction
  - pdf
  - exfiltration
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Information Repositories]]'
updated_at: '2025-12-14T17:25:29.981Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Information Repositories]]'
---
# Extract-PDF-from-302-Response

## Summary

This procedure saves the embedded PDF containing unauthorized PHI/PII from the 302 redirect response body using Burp Suite's file export feature, completing the data disclosure.

## Description

The vulnerable endpoint attaches the full PDF to the 302 response body, allowing direct extraction without additional requests. In Burp Suite, the response is intercepted, and the body is copied to a file, resulting in a viewable PDF with sensitive medical data. This step finalizes the collection phase. Prerequisites: Successful IDOR exploitation with response in Burp.

## Requirements

1. Intercepted 302 response with PDF body in Burp Suite
2. Local filesystem access for saving files
3. PDF viewer to validate extraction

## Defense

Defensive measures and detection strategies:

- Avoid embedding binary data in HTTP response bodies; use Content-Disposition headers for downloads
- Scan logs for large response bodies in redirects
- Implement DLP to detect PHI in outbound traffic

## Objectives

1. Persist the unauthorized record as a local PDF file
2. Verify content contains PII/PHI of target individual
3. Enable offline analysis or further exfiltration

## Instructions

### Step 1: Intercept the Response

**Context**: Ensure the manipulated request's 302 response is captured in Burp Proxy or Repeater.

No command; view the response tab.

> Confirm PDF binary data in the body (starts with %PDF header).

### Step 2: Save Response Body as PDF

**Context**: Export the body to create the file.

Right-click response body in Burp > Copy to File > Save as .pdf.

> Open the saved file in a PDF reader to confirm vaccination records and PII.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Information Repositories]] Data from Information Repositories

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[extraction]]
- [[pdf]]
- [[Exfiltration]]
