---
id: proc-uuid-detect-ssrf
tags:
  - ssrf
  - detection
  - oob
type: procedure
tools:
  - '[[tools/Burp-Collaborator]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T04:08:48.174Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Detect-Blind-SSRF-with-Burp-Collaborator

## Summary

This procedure detects Blind SSRF vulnerabilities by using out-of-band (OOB) interactions via Burp Collaborator, confirming server-side URL fetching without direct response observation.

## Description

Blind SSRF occurs when a server fetches arbitrary URLs but does not return the content, making detection challenging. By submitting a Collaborator-generated URL in the vulnerable input (e.g., image URL downloader), attackers can monitor for DNS/HTTP callbacks from the internal server, proving exploitation. This targets features like Moodle's repository URL fetcher using libcurl.

## Requirements

1. Authenticated access to the vulnerable endpoint
2. Burp Suite Professional with Collaborator module
3. Network access to generate and poll Collaborator payloads

## Defense

Defensive measures and detection strategies:

- Implement URL allowlists restricting external domains
- Monitor outbound DNS/HTTP from application servers
- Use web application firewalls (WAF) to block suspicious URL patterns

## Objectives

1. Confirm SSRF without visible responses
2. Identify internal IP making callbacks
3. Validate vulnerability for further exploitation

## Instructions

### Step 1: Generate Payload

**Context**: Create a unique OOB URL for detection.

In Burp Collaborator, generate a payload like `http://unique-id.oastify.com/test.png`.

**Expected Output**: Copyable URL for submission.

### Step 2: Submit Payload

**Context**: Trigger the server to fetch the URL.

Paste the payload into the URL downloader field in `/user/edit.php` and submit the form.

**Expected Output**: No immediate error; application may show generic success or failure.

### Step 3: Poll for Interactions

**Context**: Detect server-side activity.

Poll Burp Collaborator client; check for DNS queries and HTTP requests from the target's internal IP (e.g., fetching `/test.png`).

**Expected Output**: Logs showing interactions like DNS resolution of `unique-id.oastify.com` and HTTP GET to the endpoint.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Active Scanning]] Active Scanning: Scanning IP Blocks

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Collaborator]]

## Tags

- [[ssrf]]
- [[detection]]
- [[oob]]
