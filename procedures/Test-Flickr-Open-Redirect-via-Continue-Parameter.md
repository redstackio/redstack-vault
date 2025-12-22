---
id: proc-flickr-open-redirect-test
tags:
  - open-redirect
  - phishing
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-test-redirect]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:30.822Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
---
# Test-Flickr-Open-Redirect-via-Continue-Parameter

## Summary

This procedure tests for an open redirect vulnerability in Flickr's upgrade page by manipulating the 'continue' GET parameter to redirect to arbitrary external domains, enabling potential phishing attacks where users are tricked into visiting malicious sites.

## Description

The vulnerability arises from improper validation of the 'continue' parameter in the URL https://www.flickr.com/browser/upgrade/?continue=, allowing redirection to any external domain without checking paths or domains. This can be exploited to craft phishing links that appear to come from Flickr but lead to attacker-controlled sites. The attack requires no authentication and works over standard HTTP/HTTPS. Expected outcomes include successful redirection, confirming the flaw, with low severity impact focused on social engineering rather than direct data compromise.

## Requirements

1. Internet access to reach https://www.flickr.com
2. Web browser or curl for testing redirects
3. Knowledge of URL parameter manipulation

## Defense

Defensive measures and detection strategies:

- Implement strict URL validation in redirect parameters, whitelisting allowed domains
- Use Content Security Policy (CSP) headers to restrict navigations
- Monitor server logs for unusual redirect patterns to external domains

## Objectives

1. Confirm open redirect by achieving redirection to an external site
2. Assess phishing potential by simulating malicious URL crafting
3. Document the vulnerability for reporting

## Instructions

### Step 1: Access the Upgrade Endpoint

**Context**: Locate the vulnerable upgrade page to prepare for parameter testing.

Navigate to https://www.flickr.com/browser/upgrade/ in a web browser or use curl to fetch the base page.

**Command** ([[commands/curl-test-redirect]]):
```bash
curl "https://www.flickr.com/browser/upgrade/" -v
```

> This command retrieves the page and verbose output shows initial response without parameters. Expected output: HTML of the upgrade page, 200 OK status.

### Step 2: Test Redirect with External URL

**Context**: Append the 'continue' parameter with an external domain to check for unvalidated redirection.

Execute [[commands/curl-test-redirect]] to send the manipulated URL and follow the redirect with -L flag.

**Command** ([[commands/curl-test-redirect]]):
```bash
curl -L "https://www.flickr.com/browser/upgrade/?continue=https://evil.com" -v
```

> This simulates the attack by requesting the URL with a malicious continue value. Expected output: 302 redirect response with Location header pointing to https://evil.com, followed by the final GET to the external site.

### Step 3: Validate Impact

**Context**: Confirm the redirect enables phishing by observing the behavior in a browser.

Open the manipulated URL in a browser: https://www.flickr.com/browser/upgrade/?continue=https://evil.com. Check if it seamlessly redirects without warnings.

> No specific command needed; manual verification. Expected output: Browser navigates directly to the external domain, demonstrating phishing feasibility.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-test-redirect]]

## Tools Used


## Tags

- open-redirect
- phishing
- web-vulnerability
