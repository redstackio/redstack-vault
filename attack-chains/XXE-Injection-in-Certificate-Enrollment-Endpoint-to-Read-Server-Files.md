---
tags:
  - xxe
  - file-disclosure
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-xxe-payload-post]]'
platforms:
  - Web
  - Linux
complexity: medium
procedures:
  - '[[procedures/XXE-Injection-to-Read-Server-Files]]'
  - '[[procedures/Analyze-XXE-Response-for-Leaked-Data]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
description: >-
  Exploitation of an XXE vulnerability in a certificate enrollment endpoint to
  read arbitrary server files, leading to potential confidentiality breaches.
skill_level: intermediate
impact_level: high
id: d64b5249-08b7-4714-8140-91e7646b0491
created_at: '2025-12-13T09:00:27.815Z'
updated_at: '2025-12-13T09:00:27.815Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# XXE Injection in Certificate Enrollment Endpoint to Read Server Files

Multi-stage attack chain demonstrating exploitation of an XML External Entity (XXE) vulnerability in a U.S. Department of Defense web application's certificate enrollment endpoint, allowing unauthorized reading of sensitive server files like /etc/passwd.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Exploitation] --> B[Response Analysis]
    style A fill:#e74c3c
    style B fill:#f39c12
```

## Prerequisites & Requirements

### Required Tools

- None specified, but a tool like curl for sending HTTP requests is recommended.

### Target Environment

- Web application running on Linux
- Services: PKI Certificate System, Apache, Tomcat
- Exposed endpoint: /ca/rest/certrequests

### Initial Access Requirements

- Network access to the target web application
- No credentials required for the vulnerable endpoint

## Detailed Attack Procedures

### Step 1: Send Malicious XXE Payload
procedure: [[procedures/XXE-Injection-to-Read-Server-Files]]

**Objective**: Exploit the XXE vulnerability by sending a crafted XML payload to the certificate enrollment endpoint to force the server to process external entities and disclose file contents.

**Instructions**: Craft and send a POST request with the malicious XML payload using [[commands/curl-xxe-payload-post]]:

```bash
curl -X POST -H "Content-Type: application/xml" -d '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><CertEnrollmentRequest><ProfileID>&xxe;</ProfileID></CertEnrollmentRequest>' https://target.com/ca/rest/certrequests
```

**Expected Output**: Server response including leaked file contents embedded in the error message.

**Success Indicators**:
- Server processes the external entity
- File contents like /etc/passwd are returned in the response

### Step 2: Analyze Server Response
procedure: [[procedures/Analyze-XXE-Response-for-Leaked-Data]]

**Objective**: Examine the server's response to extract and verify the leaked sensitive information from the arbitrary file read.

**Instructions**: Capture and review the HTTP response from the previous step. Look for embedded file contents in the XML error message, such as user entries from /etc/passwd.

**Expected Output**: Response body containing the contents of the targeted file, e.g., 'root:x:0:0:root:/root:/bin/bash'.

**Success Indicators**:
- Leaked data is present and readable
- Confirmation of file disclosure without authentication

## Attack Chain Summary

### Key Achievements

1. Successful injection of XXE payload to read arbitrary files
2. Extraction of sensitive server information like /etc/passwd
3. Demonstration of potential for SSRF, DoS, or RCE in vulnerable configurations

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Collection]]

*Last updated: 2023-10-01*
