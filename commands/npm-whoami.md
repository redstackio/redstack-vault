---
data: npm whoami
tags:
  - npm
  - auth
type: command
output: Current npm username
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:44.385Z'
id: 2b094fe5-0974-4a96-bb05-1c7c8234bfd0
verified: false
validated: true
submitted: true
---
# npm-whoami

## Command

```bash
npm whoami
```

## Description

Shows the current logged-in npm user, used in attacks to innocently trigger .npmrc loading.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Displays current user | No |

## Examples

### Basic Usage

```bash
npm whoami
```

## Expected Output

Current npm username or error if not logged in.

## Related

- [[commands/npm-help]]
- [[procedures/Trick-Victim-to-Run-npm]]
