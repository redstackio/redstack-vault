---
tags:
  - delivery
  - phishing
  - social-engineering
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:57.130Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 9dbcab2c-cb7a-49f9-ae95-0ca046d685f4
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Deliver CSRF HTML to Victim

## Summary

This procedure involves sending the malicious Csrf.html file to a victim, tricking them into opening it while logged into Evernote, thereby executing the unauthorized deactivation.

## Description

Delivery relies on social engineering, such as email attachments or links hosting the HTML. The victim must be authenticated for the session cookies to be included in the forged request. This step completes the attack chain by leveraging user interaction.

## Requirements

1. Prepared Csrf.html file
2. Victim's contact method (email, messaging)
3. Plausible pretext for opening the file

## Defense

Defensive measures and detection strategies:

- User training on suspicious files
- Email filters for HTML attachments
- Session timeout on inactive logins

## Objectives

1. Ensure victim opens file in authenticated state
2. Trigger form submission silently
3. Minimize detection during delivery

## Instructions

### Step 1: Prepare Delivery Method

**Context**: Choose a vector to send the file without raising alarms.

1. Embed in email as attachment: "Please review this important update.html"
2. Host on a server and send link: e.g., via shortened URL
3. Use messaging apps for direct file share

> Avoid obvious malicious names; rename to something innocuous like update.html.

### Step 2: Instruct Victim

**Context**: Prompt interaction while ensuring Evernote session is active.

Send message: "Open this file in your browser to view the details—make sure you're logged into your accounts."

> Victim loads file; JavaScript submits form using their cookies to Evernote.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- delivery
- phishing
- social-engineering
