---
id: proc-twitter-dm-trigger-share-001
tags:
  - xss
  - trigger
  - twitter
  - dm
  - tweet-sharing
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:47.319Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger XSS via Tweet Sharing in DM

## Summary

This procedure triggers the stored XSS payload in a Twitter DM group name by simulating or inducing a victim to share a tweet to the group, causing unsanitized rendering and JavaScript execution.

## Description

When a user shares a tweet via the DM interface to a group with a malicious name, Twitter renders the group name in the share dialog without proper escaping, executing the embedded script in the user's browser. This leverages the JavaScript interpreter in the web context, allowing arbitrary code like alerts, cookie theft, or redirects. Targets non-technical users in the group. Prerequisites: Existing vulnerable group. Outcome: JS execution in victim's session, potentially leading to account compromise.

## Requirements

1. Access to a vulnerable DM group (from Step 1)
2. Victim account in the group
3. Twitter web interface

## Defense

Defensive measures and detection strategies:

- Sanitize group names on render in all UI components (e.g., share dialogs)
- Log and alert on script execution attempts in DM contexts
- Educate users on suspicious DM interactions

## Objectives

1. Execute payload via natural user action (tweet sharing)
2. Confirm arbitrary JS in victim browser
3. Demonstrate low-effort trigger

## Instructions

### Step 1: Select a Tweet for Sharing

**Context**: Prepare the trigger action from the victim's perspective.

As victim, browse to any tweet, click the share icon (envelope), and select 'Send via Direct Message'.

> This opens the DM selection interface.

### Step 2: Choose the Vulnerable Group

**Context**: Render the group name to execute the payload.

In the DM selector, choose the group with the XSS name. The name displays unsanitized, triggering the script.

> Payload executes immediately; e.g., alert(1) pops up.

### Step 3: Validate Execution

**Context**: Inspect for successful JS run.

Check browser console for errors or use a payload that logs to console (e.g., `console.log('XSS')`).

> Success: Script runs in victim's context, accessing DOM/cookies.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[trigger]]
- [[twitter]]
- [[dm]]
- [[tweet-sharing]]
