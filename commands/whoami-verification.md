---
id: cmd-whoami
data: whoami
tags:
  - verification
  - rce
type: command
output: rocketchat
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:19.892Z'
verified: false
validated: true
submitted: true
---
# whoami-verification

## Command

```bash
whoami
```

## Description

Displays the current username in the shell obtained via webhook RCE to confirm execution as the Rocket.Chat process user.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | None | No |

## Examples

### Basic Usage

```bash
whoami
```

## Expected Output

rocketchat

## Related

- [[commands/id-verification]]
