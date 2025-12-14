---
tags:
  - deserialization-trigger
  - rce
  - notification-view
type: procedure
tools:
  - '[[tools/Python-Pickle-Module]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Python]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: d9baf342-3aef-4dab-bfe1-280fc9643f6c
created_at: '2025-12-14T03:46:19.791Z'
updated_at: '2025-12-14T03:46:19.791Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Python]]'
---
# Trigger-Deserialization-by-Viewing-Notifications

## Summary

This procedure triggers the deserialization of the malicious pickle payload by accessing the notifications page as the target user, resulting in code execution.

## Description

Logging in as the invited user and visiting the notifications endpoint calls render_notifications in liberapay/models/participant.py, which uses pickle.loads on the context field from the database. This deserializes the injected payload, executing arbitrary code like os.system commands in the Python environment.

## Requirements

1. Credentials of the invited/target user
2. Malicious payload already injected (from prior steps)
3. Access to the notifications page

## Defense

Defensive measures and detection strategies:

- Avoid pickle for untrusted data; switch to safe formats like CBOR
- Sandbox deserialization processes
- Log and monitor deserialization attempts for errors or hangs

## Objectives

1. Invoke deserialization on victim side
2. Execute the RCE payload
3. Observe impact like application hang or command output

## Instructions

### Step 1: Authenticate as Target User

**Context**: Gain session as the user who received the notification.

Use Liberapay login with target credentials.

> Session established for notifications access.

### Step 2: Access Notifications Page

**Context**: Trigger render_notifications to deserialize context.

Navigate to /notifications or equivalent endpoint.

> Deserialization occurs, executing payload (e.g., sleep causes 500-second hang).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Python]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Python-Pickle-Module]]

## Tags

- [[deserialization-trigger]]
- [[rce]]
- [[notification-view]]
