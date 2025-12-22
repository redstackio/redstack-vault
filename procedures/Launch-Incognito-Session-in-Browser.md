---
tags:
  - phishing
  - session-management
type: procedure
tools:
  - '[[tools/Google-Chrome]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[T1566.002]]'
updated_at: '2025-12-14T17:24:23.072Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 55f36c04-b9b7-4987-b487-6d1b83acd0ff
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.002]]'
---
# Launch-Incognito-Session-in-Browser

## Summary

This procedure initiates a private browsing session in Google Chrome's incognito mode to simulate a fresh user without prior session data, essential for accurately reproducing OAuth phishing attacks.

## Description

In the context of exploiting Phabricator's open redirection vulnerability, starting with a clean session prevents interference from cached cookies or existing logins, mimicking how a real victim would encounter a phishing link. This step ensures the OAuth flow behaves as intended for token theft testing, targeting secure.phabricator.com.

## Requirements

1. Google Chrome browser installed
2. No specific network access beyond internet connectivity
3. Basic familiarity with browser interfaces

## Defense

Defensive measures and detection strategies:

- Educate users on recognizing phishing links and avoiding unsolicited OAuth prompts
- Implement browser extensions that warn about suspicious redirects
- Monitor for unusual incognito usage patterns in enterprise environments via endpoint detection

## Objectives

1. Establish a clean testing environment for the phishing simulation
2. Avoid session pollution that could mask the vulnerability
3. Prepare for navigation to the crafted URL

## Instructions

### Step 1: Open Incognito Mode

**Context**: This creates an isolated session to replicate a naive user's first interaction with the phishing site.

No command required; manually launch via Chrome menu (Ctrl+Shift+N) or right-click on Chrome icon and select "New incognito window".

> Expected output: A new window with the incognito icon (spy silhouette) appears, confirming private browsing is active.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[T1566.002]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Google-Chrome]]

## Tags

- phishing
- browser-session
