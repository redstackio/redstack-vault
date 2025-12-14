---
id: proc-trigger-integration-admin
tags:
  - privilege-escalation
  - trigger-script
  - admin-access
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:30:26.966Z'
skill_level: intermediate
impact_level: critical
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Trigger-Integration-for-Admin-Escalation

## Summary

This procedure activates the malicious integration script in Rocket.Chat to execute the embedded code, adding the 'admin' role and granting full server control.

## Description

Integration scripts run in the server application context upon triggering (e.g., via webhook). This exploits lack of isolation to call privileged APIs like Roles.addUserRoles. Targets custom integrations created with 'bot' permissions. Expected outcome: Attacker gains admin privileges, compromising the instance.

## Requirements

1. Malicious integration created and enabled
2. Trigger mechanism configured (e.g., incoming URL)
3. Monitoring access to verify role changes

## Defense

Defensive measures and detection strategies:

- Disable or restrict custom integrations for non-admin users
- Implement script execution auditing and runtime permission checks
- Alert on role additions via integrations and revoke suspicious changes

## Objectives

1. Execute script for final privilege escalation
2. Achieve full admin access
3. Validate compromise with admin actions

## Instructions

### Step 1: Identify Trigger Endpoint

**Context**: Locate the integration's execution URL from its configuration.

View integration details for incoming request URL.

> Note the webhook or trigger path. Expected output: URL like https://target.com/api/v1/integrations/...

### Step 2: Send Trigger Request

**Context**: Invoke the script by simulating an incoming request.

Use curl or browser to POST to the URL (empty body if handler is stubbed).

```bash
curl -X POST https://target.com/api/v1/integrations/<ID>/incoming -d '{}'
```

> Expected output: 200 OK response, script executes silently.

### Step 3: Verify Escalation

**Context**: Check user roles post-execution.

Query user profile or attempt admin actions.

> Look for 'admin' in roles. Expected output: Full admin dashboard access.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- privilege-escalation
- admin-access
