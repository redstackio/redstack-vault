---
id: proc-create-malicious-integration
tags:
  - code-execution
  - integration-script
  - javascript
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/addUserRoles-JS-Script]]'
  - '[[commands/basic-integration-class-script]]'
verified: false
platforms:
  - Web
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:30:26.972Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-Integration-Script

## Summary

This procedure uses 'bot' permissions to create a custom integration in Rocket.Chat with an embedded script that executes role additions, setting up for admin escalation.

## Description

With manage-own-integrations from the 'bot' role, users can define scripts that run in the server context without isolation. This procedure crafts a script calling Roles.addUserRoles to target the attacker's _id. It targets the Integrations UI in vulnerable Rocket.Chat versions. Expected outcome: Persistent malicious integration ready for triggering.

## Requirements

1. 'bot' role obtained from prior escalation
2. Access to Integrations panel
3. Known user _id for script targeting

## Defense

Defensive measures and detection strategies:

- Isolate integration scripts in sandboxed environments (e.g., VM or restricted Node.js context)
- Review and approve all custom integrations manually
- Scan scripts for dangerous API calls like Roles.addUserRoles and block execution

## Objectives

1. Embed arbitrary code in a triggerable integration
2. Prepare for server-side role modification
3. Achieve code execution in admin context

## Instructions

### Step 1: Access Integrations

**Context**: Navigate to create a new custom integration.

Go to Administration > Integrations > New Integration.

> Select custom type. Expected output: Script editor interface.

### Step 2: Embed Malicious Script

**Context**: Insert the escalation code and basic structure.

Add [[commands/addUserRoles-JS-Script]] followed by [[commands/basic-integration-class-script]]:

```javascript
this.Roles.addUserRoles("<USER_ID>", "admin");

classScript {
  process_incoming_request({ request }) {};
}
```

> Replace <USER_ID>. Save integration. Expected output: No syntax errors, integration enabled.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/addUserRoles-JS-Script]]
- [[commands/basic-integration-class-script]]

## Tools Used


## Tags

- code-execution
- javascript
