---
id: 4f60e98a-e886-46dc-b772-eb2ff197d9e2
name: metasploit-show-smb-relay-targets
type: command
executor: msfconsole
data: show targets
output: null
created_at: '2023-04-06T03:56:05.334406+00:00'
updated_at: '2023-04-10T20:26:13.144161+00:00'
platforms:
  - Linux
  - Windows
tags:
  - metasploit
  - smb-relay
verified: true
validated: true
---

# Metasploit Show SMB Relay Targets

## Command

```msfconsole
show targets
```

## Description

This command displays the available target operating systems supported by the loaded SMB relay exploit module. Use it to identify compatible versions for the relay attack, such as older Windows systems without SMB signing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | No parameters; run within the module context. | No |

## Examples

### Basic Usage

```msfconsole
msf6 exploit(smb_relay) > show targets
Exploit targets:

   Id  Name
   --  ----
   0   Automatic Target
   1   Windows 2000
   2   Windows XP
   3   Windows 2003
```

## Expected Output

A table listing target IDs and names, e.g., Windows 2000 to Server 2008 variants. Select with `set TARGET <id>`.

## Related

- [[commands/metasploit-use-smb-relay-exploit-module]]
- [[procedures/ntlm-reflection-smb-relay-attack]]
