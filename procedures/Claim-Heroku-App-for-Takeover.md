---
id: d4e5f6g7-h8i9-0123-defg-456789012345
name: Claim-Heroku-App-for-Takeover
tags:
  - heroku-takeover
  - cloud-compromise
  - dns-hijack
type: procedure
tools:
  - '[[tools/Heroku-CLI]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/heroku-login]]'
  - '[[commands/heroku-create-app]]'
  - '[[commands/heroku-deploy]]'
verified: false
platforms:
  - Cloud
  - Heroku
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:18.249Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Claim-Heroku-App-for-Takeover

## Summary

This procedure claims a dangling Heroku application name associated with a target's subdomain, redirecting traffic to attacker-controlled content for further exploitation like OAuth interception.

## Description

Heroku allows claiming deleted app names if DNS points to them. In the Uber report, claiming 'dangling-app' allowed control over 'dangling.uber.com'. Requires a Heroku account and CLI; deploys a basic web server to capture traffic.

## Requirements

1. Heroku account with verified email
2. Installed Heroku CLI
3. Local Git repo for deployment

## Defense

Defensive measures and detection strategies:

- Remove dangling DNS records promptly after service deletion
- Monitor Heroku app claims via API webhooks
- Use custom domains instead of default Heroku subdomains

## Objectives

1. Authenticate and create the app with the dangling name
2. Deploy malicious payload to handle incoming requests
3. Confirm subdomain resolution to the new app

## Instructions

### Step 1: Authenticate to Heroku

**Context**: Log in to enable app creation.

**Command** ([[commands/heroku-login]]):
```bash
heroku login
```

> Prompts for credentials; expected: Successful login confirmation.

### Step 2: Create the Dangling App

**Context**: Attempt to create app with the exact dangling name.

**Command** ([[commands/heroku-create-app]]):
```bash
heroku create dangling-app
```

> If available, outputs app URL like 'https://dangling-app.herokuapp.com'. Expected: Creation success.

### Step 3: Deploy Malicious App

**Context**: Push a simple server (e.g., Express.js for callback capture) to the app.

**Command** ([[commands/heroku-deploy]]):
```bash
git init
heroku git:remote -a dangling-app
git add .
git commit -m "deploy"
git push heroku main
```

> Deploys code; expected: App live and responding at the URL.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/heroku-login]]
- [[commands/heroku-create-app]]
- [[commands/heroku-deploy]]

## Tools Used

- [[tools/Heroku-CLI]]

## Tags

- [[heroku-takeover]]
- [[cloud-compromise]]
