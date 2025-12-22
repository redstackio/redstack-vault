---
id: 55c3fdc9-6d77-40ec-84d5-69fc7401189f
name: edit-metasploit-rc-file
type: command
executor: bash
data: nano exploit.rc
output: null
created_at: '2023-04-06T03:56:21.645019+00:00'
updated_at: '2023-04-10T20:25:01.012583+00:00'
platforms:
  - Linux
tags:
  - metasploit
  - scripting
verified: true
validated: true
---

# edit-metasploit-rc-file

## Command

```bash
nano exploit.rc
```

## Description

Opens the Metasploit resource file in the nano text editor for adding scripted commands. Replace 'nano' with 'vim' or 'gedit' if preferred.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `nano` | Text editor command | Yes |
| `exploit.rc` | Path to the resource file | Yes |

## Examples

### Basic Usage

```bash
nano exploit.rc
```

### Advanced Usage

```bash
vim + exploit.rc
```

## Expected Output

Editor interface opens; no console output until saved and exited.

## Related

- [[commands/create-metasploit-rc-file]]
- [[procedures/Metasploit-Scripting-with-Meterpreter-Reverse-HTTPS-Payload]]
