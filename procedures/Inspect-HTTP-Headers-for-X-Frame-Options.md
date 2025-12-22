---
id: proc-inspect-xframe-headers
tags:
  - clickjacking
  - headers
  - recon
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:12.720Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inspect-HTTP-Headers-for-X-Frame-Options

## Summary

This procedure checks the HTTP response headers of a target web application to determine if the X-Frame-Options header is present, identifying potential clickjacking vulnerabilities by confirming if the site can be embedded in iframes from other domains.

## Description

In a clickjacking attack scenario, the absence of the X-Frame-Options header allows malicious sites to frame the target, overlaying invisible elements to trick users into unintended actions like form submissions or clicks. This procedure targets public-facing web apps like WordPress sites (e.g., https://central.wordcamp.org/) and uses HTTP header inspection to validate the vulnerability. Prerequisites include command-line access and internet connectivity; expected outcomes include confirmation of header absence, enabling further POC development.

## Requirements

1. curl installed on the system (standard on most Linux/macOS)
2. Network access to the target URL over HTTPS
3. Basic knowledge of HTTP headers

## Defense

Defensive measures and detection strategies:

- Implement X-Frame-Options: DENY or SAMEORIGIN in server configuration (e.g., Apache/Nginx headers)
- Monitor server logs for unusual iframe embedding attempts or anomalous user-agent strings from PoC pages

## Objectives

1. Verify absence of X-Frame-Options to confirm clickjacking risk
2. Document headers for vulnerability reporting
3. Identify if the site is frameable by external domains

## Instructions

### Step 1: Fetch Target Headers

**Context**: Retrieve the HTTP HEAD response from the target to inspect security headers without downloading the full page.

**Command** ([[commands/curl-check-headers]]):
```bash
curl -I https://central.wordcamp.org/
```

> This command sends a HEAD request and outputs headers. Look for X-Frame-Options; its absence indicates vulnerability. Expected output includes status code 200 and a list of headers like Server, Content-Type, but no X-Frame-Options.

### Step 2: Analyze Output

**Context**: Manually review the headers for the specific absence.

No command needed; pipe to grep if desired: `curl -I https://central.wordcamp.org/ | grep -i x-frame` (should return nothing).

> If no match, the site is vulnerable. Success confirms the root cause for clickjacking.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-check-headers]]

## Tools Used


## Tags

- [[clickjacking]]
- [[web-recon]]
