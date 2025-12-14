---
tags:
  - takeover
  - heroku
  - initial-access
type: procedure
tools:
  - '[[tools/heroku-cli]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/heroku-login]]'
  - '[[commands/heroku-create-app]]'
verified: false
platforms:
  - Cloud (Heroku)
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Compromise Infrastructure]]'
updated_at: '2025-12-14T04:38:39.932Z'
sub_techniques: []
id: afe93580-e14b-4631-9800-c8a75e542324
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Compromise Infrastructure]]'
---
# Claim-and-Takeover-Heroku-App

## Summary

This procedure claims an unclaimed Heroku app by creating it under the attacker's account, effectively taking over the subdomain pointed to by a dangling CNAME record.

## Description

Once verified as unclaimed, authenticate to Heroku and create the app with the exact name from the DNS record. This redirects the subdomain traffic to the new app. Target: Heroku platform; requires a free Heroku account. Outcomes: Full control over the app and associated subdomain for hosting malicious content.

## Requirements

1. Valid Heroku account credentials
2. Heroku CLI installed
3. Git for deployment (if demonstrating)

## Defense

Defensive measures and detection strategies:

- Reserve critical app names in Heroku organizations
- Monitor for new app creations matching known DNS records
- Use custom domains with strict CNAME validation

## Objectives

1. Secure ownership of the unclaimed app
2. Redirect subdomain to attacker-controlled instance
3. Enable arbitrary content hosting

## Instructions

### Step 1: Authenticate to Heroku

**Context**: Login to gain permission to create apps.

**Command** ([[commands/heroku-login]]):
```bash
heroku login
```

> Opens browser for authentication. Expected output: Successful login confirmation.

### Step 2: Create the Target App

**Context**: Register the unclaimed app name to takeover.

**Command** ([[commands/heroku-create-app]]):
```bash
heroku create tim-exclusive
```

> Creates the app and sets up git remote. Expected output: "Created https://tim-exclusive.herokuapp.com/ | https://git.heroku.com/tim-exclusive.git".

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Compromise Infrastructure]] Compromise Infrastructure

### Sub-Techniques

- None

## Commands Used

- [[commands/heroku-login]]
- [[commands/heroku-create-app]]

## Tools Used

- [[tools/heroku-cli]]

## Tags

- [[takeover]]
- [[initial-access]]
