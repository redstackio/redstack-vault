---
data: git checkout tags/3.12.1
tags:
  - setup
  - version-control
type: command
output: 'Note: switching to ''tags/3.12.1''.'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:14.796Z'
id: f3c20d47-0e1f-493d-b81c-f9142b759514
verified: false
validated: true
submitted: true
---
# checkout-vulnerable-version

## Command

```bash
git checkout tags/3.12.1
```

## Description

Switches to the vulnerable version tag 3.12.1 for reproduction.

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

HEAD now at commit for 3.12.1.

## Related

- [[commands/cd-rocket-chat]]
