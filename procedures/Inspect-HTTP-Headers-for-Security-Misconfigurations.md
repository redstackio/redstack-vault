---
id: proc-inspect-headers-clickjacking
tags:
  - reconnaissance
  - headers
  - security-misconfig
type: procedure
tools:
  - '[[tools/curl]]'
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
  - '[[Gather Victim Host Information]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:04.642Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
  - '[[Exploit Public-Facing Application]]'
---
# Inspect-HTTP-Headers-for-Security-Misconfigurations

## Summary

This procedure involves querying a web server's HTTP response headers to detect missing security headers, such as X-Frame-Options, which can expose sites to clickjacking attacks. It is commonly used in reconnaissance to identify web application vulnerabilities.

## Description

In a typical attack scenario, attackers inspect headers of public-facing web applications to find misconfigurations. For clickjacking, the absence of X-Frame-Options allows browsers to embed the site in iframes from external domains, enabling UI redressing where invisible overlays trick users into actions. This procedure targets Django sites like django.aspen.io, where no such header is set, confirming vulnerability. Prerequisites include internet access and basic command-line knowledge; expected outcomes are a list of headers highlighting the gap.

## Requirements

1. Network access to the target domain (e.g., http://django.aspen.io)
2. curl tool installed on a Linux/macOS system or equivalent
3. No authentication needed for public pages

## Defense

Defensive measures and detection strategies:

- Implement X-Frame-Options: DENY or SAMEORIGIN in server config (e.g., Nginx/Apache/Django middleware)
- Monitor for anomalous header requests via WAF logs
- Use Content-Security-Policy (CSP) frame-ancestors directive as an alternative

## Objectives

1. Detect absence of anti-framing headers
2. Confirm potential for iframe-based attacks
3. Gather evidence for vulnerability reporting

## Instructions

### Step 1: Fetch Response Headers

**Context**: Use curl to retrieve only the headers from the target URL without downloading the body, focusing on security-related ones.

**Command** ([[commands/curl-check-headers]]):
```bash
curl -I http://django.aspen.io/en/latest/
```

> This command sends a HEAD request and outputs headers like Server, Content-Type, but notably lacks X-Frame-Options, indicating the site can be iframed.

### Step 2: Analyze Output

**Context**: Review the output for key security headers; absence confirms misconfiguration.

**Command** (Manual inspection):
No command needed; pipe to grep if desired:
```bash
curl -I http://django.aspen.io/en/latest/ | grep -i frame
```

> Expected: No output for frame-related headers, signaling vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Gather Victim Host Information]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-check-headers]]

## Tools Used

- [[tools/curl]]

## Tags

- [[recon]]
- [[web]]
- [[headers]]
