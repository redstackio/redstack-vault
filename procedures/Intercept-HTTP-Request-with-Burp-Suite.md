---
id: proc-intercept-burp-revive
tags:
  - sqli
  - intercept
  - burp
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
updated_at: '2025-12-14T03:15:04.918Z'
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
# Intercept-HTTP-Request-with-Burp-Suite

## Summary

This procedure uses Burp Suite to intercept and capture an HTTP GET request to the vulnerable admin-search.php endpoint in Revive Adserver, targeting the 'keyword' parameter for SQL injection testing.

## Description

In the context of exploiting SQL injection in Revive Adserver v6.0.0, this step involves setting up Burp Suite as a proxy to monitor and capture traffic from the administrative search functionality. The vulnerability arises from unsanitized input in the 'keyword' GET parameter, processed via phpAds_registerGlobalUnslashed() and flawed escaping in PEAR MDB2's matchPattern function. By intercepting the request, attackers can inspect and modify it for injection payloads like MySQL's EXTRACTVALUE or SLEEP to confirm the vuln before automation.

## Requirements

1. Burp Suite installed and running with proxy enabled (default port 8080)
2. Access to the Revive Adserver admin interface as a manager user
3. Target URL accessible (e.g., http://localhost/www/admin/)
4. Browser configured to proxy through Burp

## Defense

Defensive measures and detection strategies:

- Implement web application firewall (WAF) rules to block proxy-like traffic patterns
- Monitor for unusual proxy configurations or tool signatures in HTTP headers (e.g., X-Requested-With from Burp)
- Use input validation and prepared statements in PHP to prevent SQLi at the source

## Objectives

1. Capture the exact HTTP request structure for the vulnerable endpoint
2. Identify the 'keyword' parameter for payload insertion
3. Prepare for further exploitation without alerting the application

## Instructions

### Step 1: Launch Burp Suite and Configure Proxy

**Context**: Start Burp Suite to intercept all traffic from the browser to the target.

No command required; launch via GUI.

> Open Burp Suite, navigate to the Proxy tab, ensure Intercept is on, and set the proxy listener to 127.0.0.1:8080.

### Step 2: Navigate to Vulnerable Endpoint

**Context**: Use Burp's built-in browser to access the search page and trigger the request.

No command required; use the browser.

> In Burp's browser (configured to use the proxy), log in as a manager and go to http://localhost/www/admin/admin-search.php?keyword=FUZZ&compact=t. Forward the intercepted request in Burp.

### Step 3: Capture and Inspect Request

**Context**: View and export the intercepted GET request for analysis.

No command required; use Burp's interface.

> In the Proxy > Intercept tab, inspect the request showing GET /admin/admin-search.php?keyword=FUZZ HTTP/1.1. Right-click and select 'Copy to file' or export raw.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- sqli
- intercept
- burp
