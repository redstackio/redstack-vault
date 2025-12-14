---
tags:
  - submit
  - post-request
  - exploitation
type: procedure
tools:
  - '[[tools/Burp]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:26.749Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: e14398ca-0c9b-4bbb-a467-44a21c99214b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Submit-Tampered-Job-Application

## Summary

This procedure forwards the modified POST request in Burp Suite to the Greenhouse server, completing the job application submission with tampered external URLs that enable open redirect attacks.

## Description

With the request tampered, forwarding it via Burp sends the multipart/form-data to boards.greenhouse.io/scout24/jobs/{job_id}. Due to no validation on the URL parameters, the server accepts and stores the arbitrary URLs as if they were legitimate S3 links. The application is processed normally, and the impact materializes later when hiring managers access downloads. This step was key in the penetration test to confirm the vulnerability; the environment involves web forms and AWS backend without domain restrictions.

## Requirements

1. Tampered POST request ready in Burp Intercept
2. Stable connection to the target endpoint
3. No rate limiting on submissions

## Defense

Defensive measures and detection strategies:

- Implement request validation post-submission for URL formats
- Rate-limit job applications per IP
- Audit stored application data for anomalous URLs

## Objectives

1. Successfully submit the application without rejection
2. Store malicious URLs in the backend
3. Set up conditions for redirect exploitation

## Instructions

### Step 1: Review Tampered Request

**Context**: Double-check modifications before forwarding.

No command required; in Burp, inspect the request for correct URLs, filenames, and Content-Length.

> Expected: No syntax errors; parameters point to external sites.

### Step 2: Forward to Server

**Context**: Release the request to complete submission.

No command required; click 'Forward' in Burp's Intercept tab to send the request to the server.

> Expected: Server responds with 200 OK or redirect to success page; application logged with tampered URLs.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp]]

## Tags

- [[submit]]
- [[post-request]]
- [[exploitation]]
