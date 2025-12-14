---
id: p-reflected-xss-cookies-params
tags:
  - xss
  - reflected-xss
  - cookies
  - parameters
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-test-xss-cookie-param]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-13T23:52:55.700Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
---
# Identify Reflected XSS in Cookies and Parameters

## Summary

This procedure identifies unexploitable reflected XSS vulnerabilities triggered by combinations of cookies and URL parameters on endpoints like https://glassdoor.com/Job/, where payloads are reflected but sanitized, setting the stage for escalation via cache poisoning.

## Description

In the attack on Glassdoor, reflected XSS was found on every page under /Job/ when a malicious payload is set in a cookie and echoed via a parameter. Due to output encoding, the XSS does not execute directly but can be leveraged in poisoning attacks. The target environment is a web application with cookie-based state management. Expected outcomes include confirming the reflection point for payload crafting.

## Requirements

1. Access to the target web application (e.g., Glassdoor /Job/ endpoints)
2. Ability to set and modify HTTP cookies and query parameters
3. Proxy tool or curl for request crafting

## Defense

Defensive measures and detection strategies:

- Implement strict output encoding for cookies and parameters (e.g., HTML entity encoding)
- Use Content-Security-Policy (CSP) to block inline scripts
- Monitor for anomalous cookie values in logs

## Objectives

1. Confirm presence of reflected XSS sink
2. Validate unexploitable nature due to encoding
3. Document payload format for later chaining

## Instructions

### Step 1: Craft and Send Test Request

**Context**: Set up a request with XSS payload in cookie and parameter to trigger reflection on /Job/ page.

**Command** ([[commands/curl-test-xss-cookie-param]]):
```bash
curl -H "Cookie: test=\"<script>alert(1)</script>\"" "https://glassdoor.com/Job/some-job?param=\"<script>alert(1)</script>\"" -v
```

> This sends a GET request with the payload. Inspect the verbose output and response body for reflection. No alert should fire due to encoding.

### Step 2: Verify Reflection in Response

**Context**: Analyze the response to ensure payload is echoed without execution.

**Command** ([[commands/curl-test-xss-cookie-param]]):
```bash
curl -H "Cookie: test=\"<script>alert(1)</script>\"" "https://glassdoor.com/Job/some-job?param=\"<script>alert(1)</script>\"" | grep -i script
```

> Grep for script tags in the output to confirm reflection. Success if payload appears but is encoded (e.g., &lt;script&gt;).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used

- [[commands/curl-test-xss-cookie-param]]

## Tools Used


## Tags

- xss
- reflected-xss
