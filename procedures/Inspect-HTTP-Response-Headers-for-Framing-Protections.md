---
id: proc-inspect-headers-framing
tags:
  - recon
  - headers
  - x-frame-options
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
updated_at: '2025-12-14T17:28:04.666Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Inspect-HTTP-Response-Headers-for-Framing-Protections

## Summary

This procedure checks HTTP response headers of web pages for the presence of framing protection headers like X-Frame-Options, identifying potential clickjacking vulnerabilities by confirming if pages can be embedded in iframes.

## Description

In a typical attack scenario, attackers inspect public-facing web applications to detect misconfigurations such as missing security headers. For APITest.IO, the sign-in, sign-up, and main pages lack X-Frame-Options, allowing arbitrary framing. This procedure uses command-line tools or browser inspection to verify headers, serving as the reconnaissance step before demonstrating exploitation. Expected outcomes include confirmation of vulnerability, enabling further PoC development. Prerequisites include internet access and basic command-line knowledge.

## Requirements

1. Internet connectivity to target domain
2. curl or equivalent tool installed
3. Browser for manual verification if needed

## Defense

Defensive measures and detection strategies:

- Implement X-Frame-Options: DENY or SAMEORIGIN in server responses
- Monitor for anomalous iframe embeddings via WAF logs
- Use Content-Security-Policy (CSP) frame-ancestors directive

## Objectives

1. Verify absence of framing protection headers
2. Document vulnerable endpoints
3. Prepare for PoC demonstration

## Instructions

### Step 1: Fetch Headers for Main Domain

**Context**: Start by checking the root domain to establish baseline header configuration.

**Command** ([[commands/curl-check-headers]]):
```bash
curl -I https://apitest.io
```

> This command sends a HEAD request and outputs response headers. Scan for X-Frame-Options; absence indicates vulnerability.

### Step 2: Check Sign-In and Sign-Up Pages

**Context**: Target authentication pages, as they are high-value for clickjacking to trick logins or registrations.

**Command** ([[commands/curl-check-headers]]):
```bash
curl -I https://apitest.io/sign-in
curl -I https://apitest.io/sign-up
```

> Repeat header inspection; expect similar missing protections. Use grep for filtering: `curl -I https://apitest.io/sign-in | grep -i frame` (should return nothing).

### Step 3: Validate in Browser

**Context**: Confirm curl findings visually to ensure no dynamic header insertion.

**Instructions**: Open browser dev tools (F12), navigate to pages, and inspect Network tab for response headers.

**Expected Output**: No X-Frame-Options in headers list.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-check-headers]]

## Tools Used


## Tags

- [[recon]]
- [[web]]

