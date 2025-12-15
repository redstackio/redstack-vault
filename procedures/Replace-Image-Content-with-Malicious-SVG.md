---
tags:
  - svg-payload
  - content-replacement
  - xss-test
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
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
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:25:59.803Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 289c16c3-4c08-4bbe-b283-22b2132d3e56
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Replace-Image-Content-with-Malicious-SVG

## Summary

This procedure replaces the binary PNG data in the intercepted request with corrupted SVG code using Burp Suite, causing Reddit's processing to fail and store a 'None' URL value.

## Description

By injecting SVG elements (e.g., <rect>, <a>, <script onload>) into the request body, this exploits the absence of file integrity checks. The server accepts the mismatched file, but image processing errors lead to a null URL in the database. This sets up the GraphQL exception for DoS. Requires the prior intercepted request; outcome is a forwarded request that uploads the invalid file successfully from the server's perspective.

## Requirements

1. Intercepted request from previous procedure in Burp Suite
2. Sample malicious SVG payload prepared (e.g., in a text editor)
3. Understanding of base64 or hex encoding if needed for binary replacement
4. Burp Suite with Repeater or Inspector for body editing

## Defense

Defensive measures and detection strategies:

- Validate file signatures (magic bytes) on upload, e.g., check for PNG header 89 50 4E 47
- Scan uploaded content for script tags or anomalous XML structures
- Implement content-security-policy to block inline scripts in SVGs

## Objectives

1. Inject SVG payload to trigger processing failure
2. Ensure the request remains structurally valid for acceptance
3. Propagate the invalid URL to database storage

## Instructions

### Step 1: Access Request Body

**Context**: Locate the binary image data for replacement.

No command; Burp UI:

- In the intercepted request, switch to 'Inspect' or 'Raw' view.
- Find the multipart form data section with the PNG binary (appears as hex or base64).

> Expected: Body visible, e.g., ------WebKitFormBoundary... filename="test.png" Content-Type: image/png [binary data].

### Step 2: Replace with SVG Code

**Context**: Overwrite the binary with SVG payload.

No command; edit in Burp:

- Delete the binary data and insert SVG: <svg xmlns="http://www.w3.org/2000/svg"><rect width="100" height="100"/><a><script>alert(1)</script></a></rect></svg>.
- Update filename if needed to .svg, but keep as .png for disguise.

> Expected: Body now contains text-based SVG; request size decreases.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[JavaScript]] JavaScript (for XSS testing elements)

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- svg-payload
- content-replacement
- xss-test
