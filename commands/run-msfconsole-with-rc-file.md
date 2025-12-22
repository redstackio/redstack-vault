---
id: 418f1f8c-2079-4b15-b293-bbbc6082e5f1
name: run-msfconsole-with-rc-file
type: command
executor: bash
data: msfconsole -r ./exploit.rc
output: null
created_at: '2023-04-06T03:56:21.645128+00:00'
updated_at: '2023-04-10T20:25:01.012583+00:00'
platforms:
  - Linux
tags:
  - metasploit
  - scripting
verified: true
validated: true
---

# run-msfconsole-with-rc-file

## Command

```bash
msfconsole -r ./exploit.rc
```

## Description

Launches Metasploit console and automatically executes commands from the specified resource file (.rc), automating exploit setups and payload generations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-r` | Flag to load and run the resource file | Yes |
| `./exploit.rc` | Path to the .rc file containing msf commands | Yes |

## Examples

### Basic Usage

```bash
msfconsole -r ./exploit.rc
```

### Advanced Usage

```bash
msfconsole -r /path/to/script.rc -q
```

## Expected Output

msf6 > Loading of modules and execution logs, e.g., [*] Handler started, [*] Created document.doc

## Related

- [[commands/create-metasploit-rc-file]]
- [[procedures/Metasploit-Scripting-with-Meterpreter-Reverse-HTTPS-Payload]]
