---
tags:
  - information-disclosure
  - path-disclosure
  - apache
  - web
  - reconnaissance
type: attack_chain
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-invalid-accept-header]]'
platforms:
  - Web
complexity: low
procedures:
  - '[[procedures/Trigger-Apache-Path-Disclosure-with-Invalid-Accept-Header]]'
step_count: 1
techniques:
  - '[[File and Directory Discovery]]'
description: >-
  A reconnaissance attack exploiting Apache server error handling to disclose
  the full webroot path through an invalid Accept header on the /index endpoint.
skill_level: beginner
impact_level: low
id: 7b772804-cbb4-434d-b502-f4ba69681c91
created_at: '2025-12-14T17:26:22.757Z'
updated_at: '2025-12-14T17:26:22.757Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Apache Full Path Disclosure via Invalid Accept Header

## Overview

This attack chain demonstrates a simple information disclosure vulnerability in an Apache web server hosted on www.rockstargames.com. By sending an HTTP GET request to the /index endpoint with an invalid Accept header, the server returns an error response that reveals the full file path to the webroot. This disclosure aids attackers in reconnaissance by providing insights into the server's file structure, potentially facilitating further attacks like directory traversal or targeted brute-forcing. The vulnerability was reported via HackerOne (Report #210238) and resolved by Rockstar Games, who subsequently excluded path disclosures from their bug bounty scope.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minute |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance] --> B[Information Disclosure]

    style A fill:#e74c3c
    style B fill:#f39c12
```

## Prerequisites & Requirements

### Required Tools

- [[commands/curl-invalid-accept-header]] (or any HTTP client like Burp Suite)

### Target Environment

- Web platform with Apache server
- Accessible HTTP endpoint (e.g., port 80 or 443)
- No authentication required

### Initial Access Requirements

- Public network access to the target website
- No credentials needed
- Basic HTTP request capability

## Detailed Attack Procedures

### Step 1: Trigger Path Disclosure
procedure: [[procedures/Trigger-Apache-Path-Disclosure-with-Invalid-Accept-Header]]

**Objective**: Send a malformed HTTP request to elicit a server error that exposes the webroot path.

**Instructions**: Use [[commands/curl-invalid-accept-header]] to send a GET request to the /index endpoint with an invalid Accept header (e.g., 'invalid/mime'):

```bash
curl -H "Accept: invalid/mime" http://www.rockstargames.com/index
```

Examine the response body for error details containing the full server path.

**Expected Output**: An HTTP 406 or 500 error response including a message like "No matching DirectoryIndex (index.html) found" followed by the full path, e.g., "/var/www/html/path/to/webroot".

**Success Indicators**:
- Error response contains absolute file path (e.g., starting with /usr/ or C:\)
- Path reveals server OS and directory structure

## Attack Chain Summary

### Key Achievements

1. Successful disclosure of Apache webroot path without authentication.
2. Identification of server file structure for potential follow-on reconnaissance.
3. Demonstration of low-effort information gathering on public-facing web applications.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[File and Directory Discovery]]

### MITRE ATT&CK Tactics

- [[Discovery]]

---
*Last updated: 2023-10-01*
