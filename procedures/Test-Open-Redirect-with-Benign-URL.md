---
tags:
  - open-redirect
  - testing
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-open-redirect-test]]'
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: e3213a53-77fb-4127-ab77-d4145eb8f533
created_at: '2025-12-14T17:24:23.184Z'
updated_at: '2025-12-14T17:24:23.184Z'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-Open-Redirect-with-Benign-URL

## Summary

This procedure tests for an open redirect vulnerability by sending a request to the target endpoint with a benign external URL, confirming if the server redirects without validation. It is the initial verification step in identifying exploitable redirect flaws for potential phishing.

## Description

In the context of the reviewnic.com vulnerability, the redirect.php endpoint accepts a 'url' parameter without checking if it points to an allowed domain. By supplying a trusted site like bing.com, an attacker verifies that arbitrary redirects are possible, setting the stage for malicious exploitation. This works on any web application with unvalidated redirect logic, typically in PHP or similar server-side scripts. Expected outcome: Successful redirect to the benign site, indicating the vulnerability exists.

## Requirements

1. Internet access to the target URL (https://reviewnic.com/redirect.php)
2. Web browser or curl tool installed
3. No authentication or special permissions needed

## Defense

Defensive measures and detection strategies:

- Implement URL validation using allowlists of permitted domains
- Use relative redirects or server-side checks to ensure redirects stay within the application's domain
- Monitor access logs for suspicious 'url' parameter values containing external domains

## Objectives

1. Confirm the endpoint accepts and follows arbitrary external URLs
2. Verify no validation blocks the redirect
3. Establish proof-of-concept for further exploitation

## Instructions

### Step 1: Prepare the Test Request

**Context**: Construct the URL with a benign parameter to avoid any false positives from security filters.

**Command** ([[commands/curl-open-redirect-test]]):
```bash
curl -L -v "https://reviewnic.com/redirect.php?url=http://bing.com"
```

> This command follows redirects (-L) and provides verbose output (-v) to show the 302 response and Location header pointing to bing.com. Expected output includes a redirect chain ending at the benign site.

### Step 2: Validate in Browser

**Context**: Manually confirm the redirect behavior in a user-facing scenario.

**Command** (Browser Access):
```bash
# Open in browser: https://reviewnic.com/redirect.php?url=http://bing.com
```

> Visit the URL directly; the browser should seamlessly redirect to bing.com without warnings.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-open-redirect-test]]

## Tools Used


## Tags

- [[open-redirect]]
- [[web-testing]]
