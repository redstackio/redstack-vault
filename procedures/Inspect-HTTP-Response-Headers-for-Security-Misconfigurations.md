---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
name: Inspect-HTTP-Response-Headers-for-Security-Misconfigurations
tags:
  - reconnaissance
  - web-security
  - xss
  - misconfiguration
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-check-headers]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T03:15:31.227Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Inspect-HTTP-Response-Headers-for-Security-Misconfigurations

## Summary

This procedure involves querying a web application's HTTP response headers to identify missing security headers, such as X-XSS-Protection, which can weaken browser defenses against reflective XSS attacks in browsers like Internet Explorer, Chrome, and Safari. It is a passive reconnaissance technique used to assess configuration weaknesses without exploitation.

## Description

In web security assessments, HTTP security headers like X-XSS-Protection instruct browsers to enable built-in protections against cross-site scripting (XSS). The absence of this header on a site like https://hosted.weblate.org/ reduces these mitigations, potentially allowing malicious scripts to execute if an XSS vulnerability is present. This procedure uses a simple HTTP HEAD request to inspect headers, revealing misconfigurations in the web server setup (e.g., nginx or Django-based). No active exploitation is involved; it focuses on discovery. Prerequisites include internet access and basic command-line tools. Expected outcomes include a list of headers confirming the missing protection, highlighting risks in environments using Python/Django tech stacks.

## Requirements

1. Network access to the target URL over HTTP/HTTPS (ports 80/443)
2. Installation of curl or equivalent HTTP client
3. Basic understanding of HTTP headers and web security concepts

## Defense

Defensive measures and detection strategies:

- Implement comprehensive security headers via server configuration (e.g., add X-XSS-Protection: 1; mode=block in nginx or Django middleware)
- Use automated scanning tools like securityheaders.com or OWASP ZAP to regularly audit headers
- Monitor access logs for unusual HEAD requests to detect reconnaissance attempts

## Objectives

1. Detect absence of X-XSS-Protection header to identify XSS mitigation gaps
2. Evaluate overall header security posture of the target web application
3. Provide evidence for remediation recommendations in vulnerability reports

## Instructions

### Step 1: Fetch HTTP Response Headers

**Context**: Perform a HEAD request to retrieve only the headers without the body, targeting the root URL of the web application to check for security configurations.

**Command** ([[commands/curl-check-headers]]):
```bash
curl -I https://hosted.weblate.org/
```

> This command sends an HTTP HEAD request and outputs the response headers. Look for lines like 'X-XSS-Protection: 1; mode=block'. If absent, it indicates a misconfiguration. Successful output will show server details (e.g., nginx) and other headers but no X-XSS-Protection, confirming weakened browser protections.

### Step 2: Analyze Headers for Missing Protections

**Context**: Manually review the output to identify security-specific headers and note any omissions related to XSS or content security.

**Command** (No specific command; use grep for filtering if needed):
```bash
curl -I https://hosted.weblate.org/ | grep -i xss
```

> If no output or empty result, the header is missing. This step validates the finding and documents the impact on browsers like Chrome and Safari.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used

- [[commands/curl-check-headers]]

## Tools Used

- [[tools/curl]]

## Tags

- [[Reconnaissance]]
- [[web-security]]
- [[xss]]
- [[misconfiguration]]
