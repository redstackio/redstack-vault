---
tags:
  - idor
  - enumeration
  - access-bypass
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-download-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:47.179Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 42178288-bb37-41a9-80e8-14a1356f8b70
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Discover IDOR via File ID Iteration

## Summary

This procedure tests for Insecure Direct Object Reference (IDOR) by iterating file IDs on the resume download endpoint, bypassing authorization checks to access unauthorized resources.

## Description

LinkedIn's resume endpoint failed to validate user permissions for file IDs, allowing any authenticated user to access any resume by guessing or incrementing IDs. This IDOR was discovered by systematically testing sequential IDs around known valid ones, revealing that access was not restricted to the owner or authorized recruiters. The vulnerability affected resumes from Easy Apply attachments and direct uploads in Recruiter, potentially exposing vast amounts of PII.

## Requirements

1. Known valid file ID from the endpoint identification step.
2. Valid session token or cookies from an authenticated LinkedIn session.
3. Tool for sending HTTP requests (curl or browser).

## Defense

Defensive measures and detection strategies:

- Enforce server-side authorization checks comparing user ID to file owner.
- Obfuscate or randomize file IDs to prevent enumeration.
- Log and alert on high-volume ID iteration attempts.

## Objectives

1. Confirm lack of authorization on file ID access.
2. Identify accessible unauthorized resumes.
3. Map the scope of exposed data.

## Instructions

### Step 1: Prepare Test IDs

**Context**: Generate a range of file IDs to test based on the known valid ID.

Start with a known ID (e.g., 12345) and create sequential variants: 12344, 12346, up to 12400.

### Step 2: Send Test Requests

**Context**: Probe the endpoint with modified IDs to detect IDOR.

Use curl to send GET requests to the endpoint, replacing {fileId} and including auth headers. Execute [[commands/curl-download-test]] for each ID:

```bash
curl -H "Authorization: Bearer YOUR_TOKEN" "https://www.linkedin.com/api/resumes/12346/download" -o test_12346.pdf --fail --silent
```

If the response is a PDF (200 OK with content), IDOR is confirmed.

**Expected Output**: Successful download for non-owned IDs, no 403 Forbidden.

### Step 3: Validate Unauthorized Access

**Context**: Review downloaded files to confirm they belong to others.

Open the PDFs and check for unfamiliar names, job histories, or companies.

**Expected Output**: Resumes from unrelated users or jobs.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

-

## Commands Used

- [[commands/curl-download-test]]

## Tools Used

- [[tools/curl]]

## Tags

- [[idor]]
- [[enumeration]]
- [[access-bypass]]
