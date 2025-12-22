---
id: proc-uuid-3
tags:
  - csrf
  - phishing
  - hosting
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:29.892Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Host and Distribute CSRF POC to Trick Victim

## Summary

This procedure hosts the malicious HTML page on an attacker-controlled domain and uses social engineering to lure the victim into visiting it while authenticated on the target site.

## Description

For applications like secure.login.gov, hosting involves uploading the POC to a web server. The attack relies on the victim being logged in, allowing session cookies to be sent with the forged request. Prerequisites: Web hosting access and phishing capabilities. Expected outcomes: Victim loads page, triggering the CSRF.

## Requirements

1. Web hosting service (e.g., free tier on Vercel or GitHub Pages)
2. Means to distribute link (email, social media)
3. Victim's email or contact info

## Defense

Defensive measures and detection strategies:

- Educate users on phishing and suspicious links
- Implement referrer policy checks
- Log and alert on cross-origin state changes

## Objectives

1. Deploy POC to accessible location
2. Socially engineer victim access
3. Confirm request transmission

## Instructions

### Step 1: Host the HTML File

**Context**: Upload the POC to make it publicly accessible.

Use a service like GitHub Pages: Create repo, add index.html, enable Pages. Note the URL (e.g., attacker.github.io/csrf-poc).

**Expected Output**: Live URL serving the HTML.

### Step 2: Distribute to Victim

**Context**: Trick the victim into visiting while logged in.

Send phishing email: "Click here to view important update: [URL]". Ensure timing aligns with their session.

**Expected Output**: Victim visits, form submits.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[social-engineering]]
- [[hosting]]
