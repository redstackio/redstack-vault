---
id: proc-uuid-1
name: Identify-FlowId-Parameter-Reflection
tags:
  - recon
  - html-injection
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-fetch-settings]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T03:47:23.625Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-FlowId-Parameter-Reflection

## Summary

This procedure identifies the reflection of the flowId query parameter in the HTML response of the Firefox Accounts settings page, confirming lack of proper escaping for HTML injection attacks.

## Description

In the attack scenario, the /settings endpoint at https://accounts.firefox.com/settings echoes the flowId parameter directly into the HTML without neutralization, allowing attackers to inject tags. This is tested by sending requests and inspecting responses. Prerequisites include public access to the endpoint and basic web debugging tools. Expected outcomes: confirmation of injection point for further exploitation like redirects.

## Requirements

1. Internet access to the target URL
2. Command-line tool like curl for requests
3. Browser or text editor to inspect HTML

## Defense

Defensive measures and detection strategies:

- Implement HTML entity encoding for user inputs reflected in responses
- Use Content Security Policy (CSP) with strict policies, though it only blocks JS here
- Monitor for anomalous query parameters in access logs

## Objectives

1. Verify parameter reflection vulnerability
2. Assess CSP limitations on non-JS attacks
3. Identify potential for script-less exploits

## Instructions

### Step 1: Send Test Request

**Context**: Fetch the page with a test flowId to observe reflection.

**Command** ([[commands/curl-fetch-settings]]):
```bash
curl "https://accounts.firefox.com/settings?flowId=test123" -v
```

> This command retrieves the response; grep for 'test123' in the HTML body to confirm unescaped insertion.

### Step 2: Inspect Response

**Context**: Analyze the HTML for direct parameter echo.

**Command** ([[commands/grep-reflection]]):
```bash
curl "https://accounts.firefox.com/settings?flowId=test123" | grep -i "test123"
```

> Expected output shows the parameter value inserted raw, e.g., <div>flowId: test123</div> without &lt; or similar encoding.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-fetch-settings]]
- [[commands/grep-reflection]]

## Tools Used


## Tags

- [[recon]]
- [[web-vuln]]
