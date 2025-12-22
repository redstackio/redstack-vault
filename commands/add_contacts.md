---
data: /add_contacts
tags:
  - gitlab
  - quick-action
type: command
executor: gitlab
platforms:
  - Web
id: ba599db8-4919-47d1-9408-67677f81ce99
created_at: '2025-12-11T03:47:49.251Z'
updated_at: '2025-12-11T03:47:49.251Z'
verified: false
validated: true
submitted: true
---
# /add_contacts

## Command

```gitlab
/add_contacts
```

## Description

GitLab quick action to add contacts to an issue, triggers popup loading contact list which can execute injected XSS payloads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | No parameters | No |

## Examples

### Basic Usage

```gitlab
/add_contacts
```

### Advanced Usage

N/A

## Expected Output

Popup with list of contacts; if payload present, executes injected script like alert(document.domain).

## Related

- [[commands//remove_contacts]]
- [[procedures/Victim-Triggers-Quick-Action-to-Execute-XSS]]
