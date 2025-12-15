---
tags:
  - csrf
  - phishing
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Drive-by Compromise]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 457b464a-b79c-451a-ad8b-e0b16a1c5db8
created_at: '2025-12-14T17:27:15.798Z'
updated_at: '2025-12-14T17:27:15.798Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Craft-and-Deliver-Malicious-CSRF-URL

## Summary

This procedure crafts a malicious URL exploiting the CSRF vulnerability to switch primary accounts on Coinbase and delivers it to trick a logged-in victim into execution.

## Description

Using the leaked account number, construct https://coinbase.com/accounts/<number>/set_as_primary. When visited by a logged-in user, the GET request uses their session cookie to perform the unauthorized switch, bypassing consents and protections.

## Requirements

1. Leaked account number
2. Method to deliver link (email, site embed)
3. Victim with active Coinbase session

## Defense

Defensive measures and detection strategies:

- Convert state-changing actions to POST with tokens
- Educate users on phishing link risks
- Implement referrer checks and same-site cookies

## Objectives

1. Trigger unauthorized account switch
2. Disrupt victim account management
3. Validate CSRF impact

## Instructions

### Step 1: Construct the URL

**Context**: Build the exploit payload.

Replace <account_number> with the leaked value: https://coinbase.com/accounts/12345/set_as_primary.

### Step 2: Deliver to Victim

**Context**: Social engineer the click.

Embed in phishing email or malicious site: "Click here to verify your account: [URL]". Ensure victim is logged in; the browser auto-sends the GET with session.

### Step 3: Verify Execution

**Context**: Confirm the switch occurred.

Instruct victim (or monitor) to check accounts page; primary should now be the targeted one.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[Phishing]]
