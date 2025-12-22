---
id: df3bc7da-b65e-4d60-b8f0-16c50577427d
name: create-metasploit-rc-file
type: command
executor: bash
data: touch exploit.rc
output: null
created_at: '2023-04-06T03:56:21.644947+00:00'
updated_at: '2023-04-10T20:25:01.012583+00:00'
platforms:
  - Linux
tags:
  - metasploit
  - scripting
verified: true
validated: true
---

# create-metasploit-rc-file

## Command

```bash
touch exploit.rc
```

## Description

Creates an empty Metasploit resource file (.rc) for scripting console commands. This file will later be populated with exploit and payload configurations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `exploit.rc` | Filename for the resource script (customizable) | Yes |

## Examples

### Basic Usage

```bash
touch exploit.rc
```

### Advanced Usage

```bash
touch ~/msf_scripts/payload.rc
```

## Expected Output

No output if successful; verify with `ls exploit.rc` showing the file with 0 bytes initially.

## Related

- [[commands/edit-metasploit-rc-file]]
- [[procedures/Metasploit-Scripting-with-Meterpreter-Reverse-HTTPS-Payload]]
