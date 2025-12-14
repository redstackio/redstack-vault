---
tags:
  - web-access
  - wallet-setup
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
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
updated_at: '2025-12-14T03:15:53.040Z'
skill_level: beginner
impact_level: low
sub_techniques: []
id: 4230004e-a840-462c-8c87-755fb0dde388
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Operator-Wallet-and-Navigate-to-API-Key-Settings

## Summary

This procedure sets up an operator wallet in the target web application and navigates to the API key creation interface, establishing the foundation for exploiting the stored XSS vulnerability in the key name field.

## Description

In the context of a web-based operator wallet feature, this procedure involves authenticating into the application, creating a new wallet, accessing its settings, and initiating API key generation. It targets environments lacking server-side validation, preparing for payload injection. Expected outcomes include positioning at the vulnerable input without triggering defenses.

## Requirements

1. Valid user credentials for the web application
2. Modern web browser with access to the wallet feature
3. No special network access beyond standard HTTPS

## Defense

Defensive measures and detection strategies:

- Implement role-based access controls to limit wallet creation
- Monitor for unusual wallet creation patterns in application logs
- Use client-side integrity checks with server-side enforcement

## Objectives

1. Gain access to the operator wallet interface
2. Prepare the environment for API key manipulation
3. Confirm navigation to the vulnerable form

## Instructions

### Step 1: Authenticate and Create Wallet

**Context**: Log in to establish a session and create a new operator wallet to serve as the attack target.

**Action**:
- Navigate to the application's login page and authenticate with valid credentials.
- Access the operator wallet creation feature and submit a new wallet request.

> This step ensures a dedicated wallet for testing the vulnerability. Expected output: Confirmation of wallet creation with a unique ID.

### Step 2: Open Wallet Settings and Initiate New Key

**Context**: Navigate to the settings of the created wallet and start the API key generation process to expose the name input field.

**Action**:
- Click on the created wallet to open its settings page.
- Locate and press the 'New key' button to load the API key creation form.

> Successful execution shows the form with fields for key name and generation options. No errors should occur.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- [[web-access]]
- [[wallet-setup]]
