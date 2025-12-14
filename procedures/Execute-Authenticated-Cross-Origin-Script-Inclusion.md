---
tags:
  - xssi
  - cross-origin
  - information-disclosure
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:25:13.226Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: d2b481ff-0e53-4bd8-8581-9f1c48b7d12d
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Execute-Authenticated-Cross-Origin-Script-Inclusion

## Summary

This procedure demonstrates loading the malicious HTML page while authenticated to Liberapay, triggering the JSONP script to execute cross-origin and disclose private donation data via the callback function.

## Description

With the user logged into Liberapay, visiting the hosted malicious page causes the browser to issue a cross-origin <script> request to /username/charts.json?callback=rip. Since requests include authentication cookies, the server responds with the private JSON wrapped in the callback (e.g., rip([...donation data...])), which executes as JavaScript, invoking the 'rip' function to extract and display (e.g., alert) the data. This bypasses privacy settings, leading to unwanted disclosure of receiving donations. Target environment is any browser with Liberapay session.

## Requirements

1. Active authenticated session to Liberapay
2. Hosted malicious HTML page from prior procedure
3. Modern web browser

## Defense

Defensive measures and detection strategies:

- Apply CORS policies to block credentialed cross-origin requests to sensitive endpoints
- Audit and remove legacy JSONP implementations
- Implement client-side checks for privacy-sensitive data loads
- Detect anomalous script inclusions via WAF or browser extensions

## Objectives

1. Trigger cross-origin request with credentials
2. Execute callback to process private JSON
3. Achieve data disclosure

## Instructions

### Step 1: Authenticate to Target

**Context**: Ensure a valid session exists for the target account.

No command; log in to Liberapay.com via browser.

> Verify session by accessing a protected page.

### Step 2: Load Malicious Page

**Context**: Visit the hosted page to initiate the script inclusion.

No command; navigate to http://your-host/index.html in the same browser.

> The <script src> will fire automatically.

### Step 3: Observe Data Disclosure

**Context**: Monitor for callback execution and data output.

No command; check browser console or alert for JSON data.

> Expect the first array element showing donation details like amounts and dates.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xssi
- cross-origin
- information-disclosure
