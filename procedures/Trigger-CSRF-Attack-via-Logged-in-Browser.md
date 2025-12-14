---
id: proc-uuid-2
tags:
  - csrf
  - web
  - drive-by
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
updated_at: '2025-12-14T17:27:22.681Z'
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
# Trigger-CSRF-Attack-via-Logged-in-Browser

## Summary

This procedure delivers and executes the malicious HTML page in a victim's browser while they are authenticated to Coinbase, leveraging session cookies to perform unauthorized wallet creation via CSRF.

## Description

Once the HTML is crafted, the attacker tricks the victim into loading it (e.g., via phishing link) in a tab where they are logged into Coinbase. The browser sends the POST request with authentication cookies, exploiting the endpoint's failure to validate origins or require CSRF tokens. The 'utf8' parameter's improper rendering in some browsers (e.g., as a checkmark) can disable built-in CSRF mitigations. Expected outcome: A new wallet appears in the victim's account without direct interaction.

## Requirements

1. Victim logged into Coinbase in the same browser session.
2. Delivery method (e.g., email, malicious site link).
3. Hosted malicious HTML accessible via HTTP/HTTPS.

## Defense

Defensive measures and detection strategies:

- Enforce same-site cookie policies (Lax/Strict).
- Log and alert on rapid or anomalous account changes.
- Educate users on phishing and not visiting untrusted links while logged in.

## Objectives

1. Ensure the page loads in an authenticated session.
2. Confirm unauthorized action execution.
3. Verify impact on victim account.

## Instructions

### Step 1: Host the Malicious Page

**Context**: Make the HTML accessible to the victim, e.g., via a web server or file share.

Upload csrf.html to a hosting service (e.g., GitHub Pages, ngrok for local testing).

> Expected: Obtain a URL like http://attacker.com/csrf.html.

### Step 2: Deliver to Victim

**Context**: Trick the victim into opening the URL while logged into Coinbase.

Send via phishing email: "Click here to claim your reward: http://attacker.com/csrf.html".

> The page auto-submits on load, using the victim's cookies for authentication.

### Step 3: Verify Execution

**Context**: Check the victim's account or monitor for success.

After delivery, log into the victim's account (if compromised) or observe via secondary access to see the new wallet.

> Expected: New wallet named 'Malicious Wallet' in accounts list.

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
- [[Phishing]]
