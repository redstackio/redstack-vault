---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
tags:
  - initial-access
  - valid-accounts
  - router
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Router
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:27:36.126Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Gain Operator Access to Ubiquiti EdgeOS

## Summary

This procedure outlines obtaining read-only operator access to the Ubiquiti EdgeOS web interface, a prerequisite for exploiting CSRF vulnerabilities in the configuration backup feature.

## Description

In the context of attacking Ubiquiti EdgeOS routers (version 1.9.1 and prior), gaining operator access provides the necessary foothold for crafting and delivering CSRF payloads. Operator accounts have read-only permissions, allowing visibility into the system without full admin rights. This step assumes credentials are obtained via phishing, weak passwords, or prior compromise. The target environment is the router's web UI, accessible over HTTP/HTTPS on the local network.

## Requirements

1. Valid operator username and password (e.g., default or compromised credentials)
2. Network access to the router (LAN or direct IP)
3. Web browser (e.g., Chrome, Firefox)

## Defense

Defensive measures and detection strategies:

- Enforce strong, unique passwords for all accounts and enable multi-factor authentication (MFA) if supported
- Monitor login attempts and restrict access to trusted IPs via firewall rules
- Regularly audit user accounts and disable unused operator roles

## Objectives

1. Authenticate as operator to access the web interface
2. Verify read-only permissions to confirm access level
3. Prepare for subsequent CSRF exploitation

## Instructions

### Step 1: Access the Web Interface

**Context**: Navigate to the router's login page to begin authentication.

Open a web browser and go to the router's IP address (default: http://192.168.1.1). You should see the Ubiquiti login portal.

### Step 2: Authenticate with Operator Credentials

**Context**: Log in using operator-level credentials to gain read-only access.

Enter the operator username (e.g., 'ubnt' or custom) and password in the login form. Submit to authenticate.

**Expected Output**: Dashboard loads with read-only views (e.g., status, logs) but no edit capabilities.

### Step 3: Verify Access Level

**Context**: Confirm operator privileges by attempting to access restricted features.

Navigate to configuration sections; attempts to edit should be denied, confirming read-only status.

**Expected Output**: Error messages or disabled edit buttons for admin functions.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- initial-access
- valid-accounts
- router
