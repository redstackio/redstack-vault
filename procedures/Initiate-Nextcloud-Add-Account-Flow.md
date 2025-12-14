---
id: proc-1
tags:
  - nextcloud
  - add-account
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Windows
  - Linux
  - Desktop
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:54.905Z'
skill_level: low
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Initiate-Nextcloud-Add-Account-Flow

## Summary

This procedure starts the Add Account wizard in the Nextcloud Desktop Client, opening a vulnerable WebView that loads content from an attacker-controlled server, setting up the exploitation vector.

## Description

The Nextcloud Desktop Client uses a QT-based WebView during the Add Account flow to display the server's login page. Without proper URI validation, this allows malicious content to be loaded and interacted with, leading to downstream exploitation. This step requires user initiation but no special privileges.

## Requirements

1. Installed Nextcloud Desktop Client (vulnerable version)
2. Attacker-controlled server accessible over HTTPS
3. User with intent to add a Nextcloud account

## Defense

Defensive measures and detection strategies:

- Disable auto-opening of external links in desktop clients
- Use network proxies to inspect WebView traffic
- Monitor for unusual client-server interactions during login flows

## Objectives

1. Open the WebView to load untrusted content
2. Establish connection to malicious server
3. Prepare for URI scheme injection

## Instructions

### Step 1: Launch Client and Start Wizard

**Context**: Open the Nextcloud Desktop Client and navigate to the account addition interface.

No specific command; manually select "Add Account" in the client UI.

> This triggers the WebView to load `https://attacker-server/login`.

### Step 2: Verify WebView Load

**Context**: Confirm the malicious login page appears in the embedded browser.

Inspect network logs on the server for the incoming request from the client.

**Expected Output**: Server logs show GET request to /login from client IP.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- nextcloud
- webview
