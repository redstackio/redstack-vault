---
id: proc-uuid-2
tags:
  - csrf
  - request-forgery
  - web
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:22.960Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft Malicious CSRF Request with Stolen Token

## Summary

This procedure involves creating a forged HTTP request or HTML form that incorporates a stolen persistent CSRF token to trick the target application into processing unauthorized actions, bypassing built-in CSRF protections.

## Description

Using the extracted token, the attacker constructs a request mimicking legitimate application traffic. This can be a GET/POST link or an auto-submitting HTML form targeting sensitive endpoints like account settings. The token's persistence ensures validity when executed on the same workstation. This is effective in shared setups where the victim uses the same browser session. Expected outcomes include successful unauthorized modifications without alerting the user.

## Requirements

1. Stolen CSRF token from a valid session
2. Knowledge of target application's endpoints and form parameters
3. Text editor or HTML builder for crafting the payload

## Defense

Defensive measures and detection strategies:

- Enforce token regeneration and same-site cookie attributes
- Validate referer headers and origins in requests
- Log and alert on requests from unusual sources or with reused tokens
- Implement double-submit cookie patterns for CSRF protection

## Objectives

1. Build a functional forged request using the persistent token
2. Ensure the request targets a high-impact action (e.g., account change)
3. Test the payload for successful token validation

## Instructions

### Step 1: Identify Target Endpoint

**Context**: Determine the URL and parameters for the unauthorized action.

Review the application's network requests in dev tools to note the action URL (e.g., POST /user/update) and required fields (e.g., email, password).

**Expected Output**: Endpoint details documented.

### Step 2: Construct the Forged Form

**Context**: Embed the token into an HTML form that auto-submits or links to the endpoint.

Create an HTML file with a form:

```html
<!DOCTYPE html>
<html>
<body>
<form id="csrf-form" action="https://target.com/user/update" method="POST">
  <input type="hidden" name="authenticity" value="abc123def456ghi789">
  <input type="hidden" name="email" value="hijacked@attacker.com">
  <input type="hidden" name="commit" value="Update Email">
</form>
<script>document.getElementById('csrf-form').submit();</script>
</body>
</html>
```

Save as malicious.html or encode as data: URI for link delivery.

**Expected Output**: Payload ready for hosting or sending.

### Step 3: Validate the Payload

**Context**: Test the crafted request to ensure token acceptance.

Open the HTML in a browser on a test instance or use curl to simulate:

But since no commands, manually load and submit to verify no CSRF error.

**Expected Output**: Request succeeds with 200 OK and action performed.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[request-forgery]]
- [[web]]
