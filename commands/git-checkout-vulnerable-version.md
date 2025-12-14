---
data: git checkout tags/3.12.1
tags:
  - versioning
  - vulnerable-setup
type: command
output: |-
  Note: switching to 'tags/3.12.1'.
  You are in 'detached HEAD' state.
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:20.413Z'
id: 480f20a9-466a-43f2-855d-abdd71b778a8
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

Checks out the vulnerable version tag (3.12.1) for reproduction.

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

Switched to version 3.12.1.

## Related

- [[commands/cd-rocket-chat]]
