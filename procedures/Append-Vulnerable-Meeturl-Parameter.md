---
tags:
  - parameter-tampering
  - recon
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
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
updated_at: '2025-12-14T17:30:07.377Z'
sub_techniques: []
id: 2744987a-7637-4569-8b71-9d1d5a536058
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Append-Vulnerable-Meeturl-Parameter

## Summary

This procedure modifies the intercepted request by adding the meeturl parameter, discovered through reconnaissance, to test for injection points.

## Description

In the Skype for Business attack scenario, appending ?meeturl= to the URL exploits lack of input validation. Requires Burp Repeater. Outcomes: URL ready for payload insertion.

## Requirements

1. Intercepted request in Burp Repeater
2. Knowledge of vulnerable parameter from recon
3. Basic HTTP editing skills

## Defense

Defensive measures and detection strategies:

- Validate and sanitize URL parameters server-side
- Log parameter additions and flag unusual queries
- Apply input whitelisting for meeturl

## Objectives

1. Extend URL with vulnerable parameter
2. Validate request syntax
3. Prepare for payload testing

## Instructions

### Step 1: Modify URL in Repeater

**Context**: Edit the Raw or Params tab to append the parameter.

No command; GUI edit:

```plaintext
Original: /lwa/Webpages/LwaClient.aspx
Modified: /lwa/Webpages/LwaClient.aspx?meeturl=
```

> Expected output: Updated request preview without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[parameter-tampering]]
- [[recon]]
