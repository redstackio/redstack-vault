---
id: p2b3c4d5-e6f7-8901-bcde-f2345678901
tags:
  - dos
  - request-modification
  - burp-suite
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:56.808Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Intercept-and-Modify-Upload-Request

## Summary

This procedure uses a proxy tool to intercept and tamper with the HTTP POST request during profile picture upload, specifically modifying the filename to include a large payload that triggers DoS in subsequent GraphQL fetches.

## Description

By intercepting the upload request with Burp Suite, attackers can bypass client-side restrictions and inject arbitrary large strings into the filename parameter. This exploits the absence of server-side length checks, leading to storage of oversized metadata that bloats JSON responses from GraphQL endpoints querying user profiles. The result is resource exhaustion on clients loading affected pages, such as report participant lists.

## Requirements

1. Burp Suite installed and running as a proxy
2. Browser proxy settings configured to 127.0.0.1:8080 (default Burp port)
3. Prepared 3MB text payload file
4. Active HackerOne session

## Defense

Defensive measures and detection strategies:

- Enforce server-side validation on all input parameters, rejecting requests with filenames over a safe limit
- Log and alert on unusually large request bodies or modified headers
- Implement WAF rules to detect proxy tampering patterns (e.g., repeated intercepts)
- Scan for oversized blobs in storage services like S3

## Objectives

1. Capture the upload request without disrupting the flow
2. Successfully modify the filename with a large payload
3. Complete the upload to persist the exploit

## Instructions

### Step 1: Configure Proxy

**Context**: Set up interception for HTTP traffic.

Launch Burp Suite, ensure the proxy listener is active on port 8080, and configure your browser to use it as the HTTP proxy.

### Step 2: Trigger and Intercept

**Context**: Initiate the upload to capture the request.

From the profile edit page, select and submit an image file. In Burp's Proxy > Intercept tab, the POST request will pause for editing.

### Step 3: Edit Filename and Forward

**Context**: Append the payload to exploit the vulnerability.

In the request viewer, find the filename field in the form data. Replace it with `<payload_from_file>original.png` (paste 3MB text). Click Forward to send it to the server.

**Expected Output**: Server responds with 200 OK or a redirect, confirming upload success.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- dos
- request-modification
- burp-suite
- web-proxy
