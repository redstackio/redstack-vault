---
tags:
  - xss
  - recon
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-access-page]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:53.508Z'
sub_techniques: []
id: 2a8c8e25-fd81-4e51-a0bf-39fd0cfdc545
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Vulnerable-Registration-Page

## Summary

This procedure involves navigating to the publicly accessible registration page on a DoD subdomain to verify reachability and parameter reflection, setting the stage for XSS exploitation.

## Description

The target page at https://target-dod-subdomain.com/path/user/NextRequestAccount.action is a registration endpoint that does not require authentication. Analysis shows the 'militarybranch' GET parameter is reflected in the HTML without sanitization, making it vulnerable to XSS. This step confirms the endpoint's availability and lack of protections.

## Requirements

1. Internet access to the public DoD subdomain
2. Web browser or curl for HTTP requests
3. No credentials or prior access needed

## Defense

Defensive measures and detection strategies:

- Implement Content Security Policy (CSP) to restrict inline scripts
- Monitor for anomalous GET parameters in access logs
- Use web application firewall (WAF) rules to block common XSS payloads

## Objectives

1. Confirm the registration page is publicly accessible
2. Verify the militarybranch parameter is reflected unsanitized
3. Establish baseline for payload injection

## Instructions

### Step 1: Navigate to the Endpoint

**Context**: Use a browser or curl to access the base URL and inspect the response for parameter reflection.

**Command** ([[commands/curl-access-page]]):
```bash
curl "https://target-dod-subdomain.com/path/user/NextRequestAccount.action?militarybranch=test"
```

> This fetches the page with a benign parameter value. Inspect the HTML output for 'test' reflected in plain text without encoding.

### Step 2: Inspect Page Source

**Context**: In a browser, view source to locate where the militarybranch value appears in the HTML.

**Command** (Manual browser inspection):
No command needed; right-click and 'View Page Source' to search for the parameter value.

> Expected to see the value inserted directly into HTML attributes or text nodes without escaping.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-access-page]]

## Tools Used


## Tags

- [[xss]]
- [[recon]]
