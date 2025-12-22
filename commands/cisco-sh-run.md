---
id: cmd-cisco-sh-run-001
data: sh run
tags:
  - cisco-ios
  - config-view
type: command
output: |-
  Building configuration...
  Current configuration : [size] bytes
  [full config details]
executor: bash
platforms:
  - Network Device
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:44.931Z'
verified: false
validated: true
submitted: true
---
# cisco-sh-run

## Command

```bash
sh run
```

## Description

This Cisco IOS command displays the current running configuration of the device, useful for reconnaissance of sensitive settings when executed remotely via exploited endpoints.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `sh` | Abbreviation for 'show' | Yes |
| `run` | Specifies the running-config | Yes |

## Examples

### Basic Usage

```bash
sh run
```

### Advanced Usage

```bash
sh run | include secret
```

## Expected Output

Building configuration...\nCurrent configuration : [size] bytes\n[full config details including interfaces, users, secrets, and routing].

## Related

- [[commands/exploit-dump-config]]
- [[procedures/Exploiting-Auth-Bypass-for-Command-Execution-and-User-Creation]]
