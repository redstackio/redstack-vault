---
id: proc-identify-open-redirect
tags:
  - open-redirect
  - recon
  - web-testing
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:27.132Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify Open Redirect Endpoints

## Summary

This procedure involves testing web endpoints for open redirect vulnerabilities by manipulating URL parameters to bypass validation, specifically targeting login or callback URLs on sites like Starbucks Greater Asia domains.

## Description

Open redirects occur when a web application allows user-supplied URLs in redirect parameters without proper validation, enabling attackers to send victims to malicious sites. In the Starbucks case, multiple Greater Asia domains failed to restrict redirects to trusted domains, allowing arbitrary redirections. This procedure outlines manual testing using browser tools or proxies to identify such flaws, with expected outcomes including successful redirects to external sites. Prerequisites include access to the target site and basic web debugging skills.

## Requirements

1. Web browser with developer console (e.g., Chrome DevTools)
2. Network access to target domains (publicly accessible)
3. Optional proxy tool like Burp Suite for request interception

## Defense

Defensive measures and detection strategies:

- Implement strict URL validation whitelisting only trusted domains
- Use HTTP response headers like Content-Security-Policy to restrict navigations
- Monitor access logs for unusual redirect patterns to external domains

## Objectives

1. Confirm presence of unvalidated redirect parameters
2. Document vulnerable endpoints for reporting
3. Assess potential for phishing misuse

## Instructions

### Step 1: Locate Potential Redirect Endpoints

**Context**: Identify pages that handle redirects, such as login, OAuth callbacks, or error pages, by reviewing the site's sitemap or common paths like /login or /redirect.

For Starbucks Greater Asia domains, navigate to regional login pages (e.g., https://asia.starbucks.com/login).

**Expected Output**: List of candidate URLs with redirect parameters (e.g., ?next= or ?redirect=).

### Step 2: Test Redirect Validation

**Context**: Append an arbitrary external URL to the parameter and submit the request to check if the server redirects without validation.

Use the browser address bar or a proxy to modify the request:

Example test URL: https://asia.starbucks.com/login?redirect=http://example.com

Intercept with Burp Suite if needed to inspect the Location header in the 3xx response.

**Expected Output**: Server responds with a 302 redirect to http://example.com, confirming the vulnerability.

### Step 3: Verify Impact

**Context**: Test with a controlled malicious domain to simulate phishing without causing harm.

Replace with a benign test site and confirm seamless redirection.

**Expected Output**: User is redirected to the test site, indicating low barrier for phishing.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[open-redirect]]
- [[web-vulnerability]]
