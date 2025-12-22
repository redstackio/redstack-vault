---
data: git checkout tags/3.12.1
tags:
  - setup
  - git
type: command
output: Checkout confirmation
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:30.552Z'
id: e31327c8-2207-49a8-a8f3-c7a12deed438
verified: false
validated: true
submitted: true
---
# checkout-vulnerable-tag

## Command

```bash
git checkout tags/3.12.1
```

## Description

Switches to the vulnerable version tag 3.12.1 for reproduction.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| tags/3.12.1 | Release tag | Yes |

## Examples

### Basic Usage

```bash
git checkout tags/3.12.1
```

## Expected Output

Note: switching to 'tags/3.12.1'.

## Related

- [[commands/change-to-rocketchat-dir]]
