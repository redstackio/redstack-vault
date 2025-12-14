---
tags:
  - reconnaissance
  - headers
  - x-frame-options
type: procedure
tools:
  - '[[tools/OWASP-Clickjacking-Defense-Cheat-Sheet]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-fetch-headers]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-05T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:28:12.584Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 08071b10-7c5b-4b57-8339-1a96a4a51142
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Inspect-HTTP-Response-Headers-for-X-Frame-Options

## Summary

This procedure involves fetching and analyzing the HTTP response headers of a target web application to identify misconfigurations in the X-Frame-Options header, specifically checking for unsupported values like 'ALLOW-FROM' that fail to provide clickjacking protection in modern browsers such as Chrome.

## Description

In the context of web security testing, inspecting headers is a key reconnaissance step to uncover framing vulnerabilities. For Periscope.tv, the header was set to 'ALLOW-FROM https://twitter.com/', which Chrome ignores, allowing any site to frame the content. This procedure uses command-line tools to retrieve headers and manual inspection to confirm the issue, as per OWASP guidelines on clickjacking defenses. Prerequisites include basic command-line access and internet connectivity; expected outcomes are identification of vulnerable header configurations enabling further exploitation.

## Requirements

1. Command-line tool like curl installed
2. Network access to the target URL (https://www.periscope.tv/)
3. Knowledge of HTTP headers and browser behaviors

## Defense

Defensive measures and detection strategies:

- Implement proper X-Frame-Options: DENY or SAMEORIGIN
- Use Content-Security-Policy (CSP) frame-ancestors directive
- Monitor server logs for unusual header requests or iframe attempts

## Objectives

1. Retrieve and parse HTTP response headers from the target
2. Identify X-Frame-Options value and assess browser support
3. Confirm vulnerability for clickjacking exploitation

## Instructions

### Step 1: Fetch Headers

**Context**: Use curl to send a HEAD request and retrieve only the headers without the body, focusing on security-related headers.

**Command** ([[commands/curl-fetch-headers]]):
```bash
curl -I https://www.periscope.tv/
```

> This command outputs the HTTP status and all response headers. Look for 'X-Frame-Options: ALLOW-FROM https://twitter.com/' in the response, indicating ineffective protection in Chrome as the 'ALLOW-FROM' directive is deprecated and unsupported.

### Step 2: Analyze Output

**Context**: Manually review the headers against OWASP references to determine if framing is possible.

**Command** (No command; manual inspection):

> Cross-reference with [[tools/OWASP-Clickjacking-Defense-Cheat-Sheet]] to confirm that Chrome treats the header as absent, allowing iframes.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-fetch-headers]]

## Tools Used

- [[tools/OWASP-Clickjacking-Defense-Cheat-Sheet]]

## Tags

- [[Reconnaissance]]
- [[web-security]]
