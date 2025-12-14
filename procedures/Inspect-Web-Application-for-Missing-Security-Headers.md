---
tags:
  - reconnaissance
  - security-headers
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-check-headers]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:28:05.271Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 32eac5ed-4f8e-4934-a8a3-e97a05d09ef3
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Inspect-Web-Application-for-Missing-Security-Headers

## Summary

This procedure involves inspecting HTTP response headers of a web application to detect the absence of critical security headers like X-Frame-Options and Content-Security-Policy, which can indicate vulnerability to clickjacking attacks.

## Description

In the context of the Legal Robot application, a security researcher identified missing headers by examining responses, revealing potential for UI redressing where attackers iframe the site to overlay malicious elements and trick users into actions like signing documents. This reconnaissance step is foundational for confirming web misconfigurations that enable exploitation. Prerequisites include basic networking knowledge and access to tools like curl; expected outcomes are header details confirming vulnerabilities.

## Requirements

1. Network access to the target web application (e.g., https://legalrobot.com)
2. curl or equivalent HTTP client installed
3. Basic understanding of HTTP headers

## Defense

Defensive measures and detection strategies:

- Implement X-Frame-Options: DENY or SAMEORIGIN in server responses
- Use Content-Security-Policy with frame-ancestors directive to restrict framing
- Monitor for anomalous header inspection requests via WAF logs

## Objectives

1. Identify missing protective headers to assess clickjacking risk
2. Gather evidence for vulnerability reporting
3. Validate site-wide header configurations

## Instructions

### Step 1: Fetch HTTP Headers

**Context**: Use curl to retrieve the HEAD response from the target URL, focusing on security-related headers.

**Command** ([[commands/curl-check-headers]]):
```bash
curl -I https://legalrobot.com
```

> This command sends a HEAD request and outputs headers. Look for X-Frame-Options and Content-Security-Policy; their absence confirms the vulnerability. Expected output includes lines like "HTTP/2 200" followed by various headers, but no X-Frame-Options or CSP.

### Step 2: Analyze Response

**Context**: Manually review the output for missing headers.

No specific command; pipe output to grep if needed:
```bash
curl -I https://legalrobot.com | grep -i "x-frame-options\|content-security-policy"
```

> If no matches, the headers are missing, indicating successful detection.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-check-headers]]

## Tools Used


## Tags

- [[Reconnaissance]]
- [[web-security]]
