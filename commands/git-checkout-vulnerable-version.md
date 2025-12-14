---
id: cmd-git-checkout-3-12-1
data: git checkout tags/3.12.1
tags:
  - setup
  - versioning
type: command
output: 'Note: switching to ''tags/3.12.1'''
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:19.906Z'
verified: false
validated: true
submitted: true
---
# git-checkout-vulnerable-version

## Command

```bash
git checkout tags/3.12.1
```

## Description

Switches the repository to the vulnerable version tag 3.12.1 for reproduction of the NoSQL injection flaw.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| tags/3.12.1 | Version tag | Yes |

## Examples

### Basic Usage

```bash
git checkout tags/3.12.1
```

## Expected Output

Switched to commit for tag 3.12.1.

## Related

- [[commands/cd-rocketchat]]
