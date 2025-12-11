---
data: /remove_contacts
tags:
  - gitlab
  - quick-action
type: command
executor: gitlab
platforms:
  - Web
id: cfc7699a-79e4-4784-bc98-e20e11ab4213
created_at: '2025-12-11T03:47:49.217Z'
updated_at: '2025-12-11T03:47:49.217Z'
verified: false
validated: true
submitted: true
---
# /remove_contacts

## Command

```gitlab
/remove_contacts
```

## Description

GitLab quick action to remove contacts from an issue, triggers popup loading contact list which can execute injected XSS payloads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | No parameters | No |

## Examples

### Basic Usage

```gitlab
/remove_contacts
```

## Expected Output

Popup with list of contacts; if payload present, executes injected script like alert(document.domain).

## Related

- [[commands//add_contacts]]
- [[procedures/Victim-Triggers-Quick-Action-to-Execute-XSS]]
