---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
name: Access Vulnerable Download Endpoint
tags:
  - idor
  - web
  - unauthenticated
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-download-file]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:34.641Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access Vulnerable Download Endpoint

## Summary

This procedure demonstrates initial access to a vulnerable Download.aspx endpoint in an ASP.NET web application without authentication, confirming the presence of an IDOR vulnerability by retrieving a document using a known ID.

## Description

In the context of a U.S. Department of Defense website, the Download.aspx endpoint lacks proper authentication and authorization checks, allowing any user to download files by specifying an 'id' parameter. This step verifies the endpoint's behavior by accessing a specific valid ID, revealing sensitive content immediately.

## Requirements

1. Internet access to the target URL (https://www.█████████/Download.aspx)
2. Web browser or curl installed
3. Known valid ID (e.g., 4675 from reconnaissance)

## Defense

Defensive measures and detection strategies:

- Implement authentication on all endpoints handling sensitive data
- Use indirect object references or UUIDs instead of sequential IDs
- Log and monitor access to download endpoints for anomalous ID patterns

## Objectives

1. Confirm unauthenticated access to documents
2. Retrieve initial sensitive file for validation
3. Establish baseline for ID enumeration

## Instructions

### Step 1: Navigate to Endpoint with Known ID

**Context**: Use a browser or curl to request the endpoint with a specific ID, expecting a direct file download.

**Command** ([[commands/curl-download-file]]):
```bash
curl -o initial_document.pdf "https://www.█████████/Download.aspx?id=4675"
```

> This command fetches the file associated with ID 4675 and saves it locally. Successful execution downloads a PDF or similar file without any login prompt, indicating the IDOR flaw.

### Step 2: Inspect Downloaded File

**Context**: Open the file to verify it contains sensitive information, such as PII.

No command needed; use a PDF viewer or text editor to examine contents.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-download-file]]

## Tools Used

- [[tools/curl]]

## Tags

- idor
- web-access
