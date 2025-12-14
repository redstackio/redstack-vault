---
tags:
  - tamper
  - url-modification
  - open-redirect
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
  - '[[T1566.002]]'
updated_at: '2025-12-14T17:24:26.753Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 34e8b836-6389-475d-83a8-02ba1762874c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[T1566.002]]'
---
# Tamper-File-URL-Parameters

## Summary

This procedure modifies the intercepted POST request in Burp Suite by replacing S3 URLs in job_application[resume_url] and job_application[cover_letter_url] with arbitrary external URLs, exploiting the lack of validation to set up an open redirect.

## Description

During the penetration test, after intercepting the request, the attacker edits the form parameters to point to external sites (e.g., https://google.com for resume, http://google.com for cover letter) while keeping the original filenames (e.g., neu.pdf). The Content-Length header is adjusted to match the changes. This bypasses any implicit expectation of S3 domains (like grnhse-prod-jben-*.s3.amazonaws.com), allowing the server to store the malicious URLs. When hiring managers download files, they are redirected, enabling phishing or CSRF. The target is the Greenhouse web application; prerequisites include an intercepted request.

## Requirements

1. Intercepted POST request in Burp Suite
2. Knowledge of original parameter values and filenames
3. Attacker-controlled external URLs for testing (e.g., benign like google.com)

## Defense

Defensive measures and detection strategies:

- Server-side validation restricting URLs to trusted domains (e.g., *.s3.amazonaws.com)
- Sanitize and whitelist URL parameters in form processing
- Alert on submissions with non-S3 URLs via backend logging

## Objectives

1. Replace legitimate S3 URLs with external malicious ones
2. Maintain request integrity to avoid submission errors
3. Enable redirect to attacker sites upon file download

## Instructions

### Step 1: Edit URL Parameters

**Context**: Locate and modify the vulnerable parameters in the request body.

No command required; in Burp's Intercept tab, switch to Inspector or raw view, find job_application[resume_url] and change its value to https://google.com, similarly for job_application[cover_letter_url] to http://google.com; keep filename=neu.pdf intact.

> Expected: Parameters updated; request body reflects external URLs.

### Step 2: Adjust Request Headers

**Context**: Ensure the modified body doesn't cause length mismatches.

No command required; update the Content-Length header to the new body size (Burp can auto-calculate), and verify no other headers are affected.

> Expected: Headers aligned; request ready for forwarding without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[T1566.002]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp]]

## Tags

- [[tamper]]
- [[url-modification]]
- [[open-redirect]]
