---
data: set secret "<leaked-secret>"
tags:
  - metasploit
  - config
type: command
output: Secret set
executor: msfconsole
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:54.941Z'
id: 6936c9f1-9180-47b3-a1b0-4fe618a46355
verified: false
validated: true
submitted: true
---
# set-secret-in-metasploit

## Command

```msfconsole
set secret "<leaked-secret>"
```

## Description

Sets the leaked Rails secret_key_base for crafting the malicious cookie in the deserialization exploit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| secret | The 128-char hex secret from GitHub | Yes |

## Examples

### Basic Usage

```msfconsole
set secret "a1b2c3d4e5f6789012345678901234567890abcdef..."
```

## Expected Output

Secret set to <value>.

## Related

- [[Related Procedure: Configure-and-Execute-Rails-Deserialization-Exploit]]
