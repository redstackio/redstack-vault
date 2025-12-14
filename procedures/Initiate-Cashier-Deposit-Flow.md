---
tags:
  - web-navigation
  - cashier-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:13.000Z'
sub_techniques: []
id: c56d36b0-d926-4f98-926e-dde904ca1988
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Initiate-Cashier-Deposit-Flow

## Summary

This procedure navigates the logged-in attacker session to the cashier deposit interface, loading the vulnerable iframe for subsequent inspection and modification.

## Description

The cashier system at https://www.binary.com/cashier embeds an iframe that authenticates via URL parameters. By initiating a deposit, the iframe src exposes the attacker's PIN, setting up the environment for IDOR exploitation. This step must be performed in the attacker's session to capture the base URL structure.

## Requirements

1. Active attacker account login
2. Browser access to https://www.binary.com
3. No ad blockers interfering with page loads

## Defense

Defensive measures and detection strategies:

- Server-side validation of session tokens before loading iframes
- Obfuscate or encrypt sensitive parameters in client-side URLs
- Log and alert on unusual navigation patterns to cashier

## Objectives

1. Load the cashier iframe with attacker's credentials
2. Prepare for developer tools inspection
3. Confirm Action=DEPOSIT parameter for deposit flow

## Instructions

### Step 1: Navigate to Cashier

**Context**: Access the main cashier page from the logged-in session.

Go to https://www.binary.com/cashier in the attacker's browser.

### Step 2: Start Deposit Process

**Context**: Trigger iframe embed by initiating deposit.

Click the "Deposit" button, then "Continue" to load the iframe.

### Step 3: Verify Iframe Load

**Context**: Ensure the deposit interface is active.

Confirm the page shows deposit options; the iframe should now be embedded.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[web-navigation]]
- [[cashier-access]]
