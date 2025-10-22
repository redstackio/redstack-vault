---
id: 1efefb00-e73a-4428-889d-eed2d4d2acbc
name: SMB and HTTP Relay Attack
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:05.406061+00:00'
updated_at: '2023-04-10T20:25:57.814988+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Adversary-in-the-Middle|T1557 - Adversary-in-the-Middle]]'
- '[[Signed Script Proxy Execution|T1216 - Signed Script Proxy Execution]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Man-in-the-Middle attacks & relaying]]'
- '[[SMB Signing Disabled and IPv4]]'
commands:
- '[[Disable SMB and HTTP servers in Responder Core]]'
---

# SMB and HTTP Relay Attack

## Summary

The SMB and HTTP Relay Attack is a Man-in-the-Middle attack that leverages the disabling of SMB signing and IPv4 to intercept and relay network traffic. This attack is commonly used to gain access to sensitive information such as user credentials or to execute code on a target system. The attacker 

## Description

# Description

The SMB and HTTP Relay Attack is a Man-in-the-Middle attack that leverages the disabling of SMB signing and IPv4 to intercept and relay network traffic. This attack is commonly used to gain access to sensitive information such as user credentials or to execute code on a target system. The attacker can use this technique to relay authentication requests to a target system, which can result in the attacker gaining access to the target system. This attack can also be used to execute code on a target system by relaying a malicious payload through the intercepted network traffic.

Technical Explanation: The attacker uses the Responder tool to intercept network traffic and relay authentication requests to a target system. The attacker can then capture the authentication response and use it to gain access to the target system. This attack can also be used to execute code on a target system by relaying a malicious payload through the intercepted network traffic.

Business Value: This attack can be used to gain access to sensitive information such as user credentials or to execute code on a target system. This can result in the attacker gaining access to sensitive data or causing damage to the target system.

## Requirements

1. Responder tool

1. Access to network traffic

1. SMB signing disabled

1. IPv4 enabled

## Defense

1. Enable SMB signing to prevent relay attacks

1. Use IPsec to encrypt network traffic

1. Implement authentication mechanisms such as multi-factor authentication

## Objectives

1. Gain access to sensitive information such as user credentials

1. Execute code on a target system

# Instructions

1. To disable SMB and HTTP servers in Responder, follow these steps:
1. Open the Responder.conf file.
2. Locate the `[Responder Core]` section.
3. Set the values of `SMB` and `HTTP` to `Off`.
4. Save the changes and exit the file.

**Code**: [[[Responder Core]
; Servers to start
...
SMB = Off ]]

> This command disables the SMB and HTTP servers in Responder. The `Responder.conf` file is a configuration file for Responder, and it contains various settings that can be customized. The `SMB` and `HTTP` options determine whether the SMB and HTTP servers are started when Responder is run. By setting these options to `Off`, you can disable these servers and prevent them from being used in any attacks.

**Command** ([[Disable SMB and HTTP servers in Responder Core]]):

```bash
[Responder Core]
; Servers to start
...
SMB = Off     # Turn this off
HTTP = Off    # Turn this off
```

2. To use NTLM RelayX as a SOCKS proxy, run the following command: impacket-ntlmrelayx -tf /tmp/targets.txt -socks -smb2support. Once the servers have started, wait for connections and type 'socks' to see the available targets. You can select a target with '-t' and use the following protocols: smb://, mssql://, http://, https://, imap://, imaps://, ldap://, ldaps:// and smtp://. Once you have selected a target, use the 'impacket-ntlmrelayx' command with the '-socks' and '-smb2support' options. The SOCKS proxy can then be used with Impacket tools or CrackMapExec.

**Code**: [[$ impacket-ntlmrelayx -tf /tmp/targets.txt -socks ]]

> NTLM RelayX can act as a SOCKS proxy with every compromised session. This allows for further exploitation of the compromised system by using Impacket tools or CrackMapExec through the SOCKS proxy. The '-socks' and '-smb2support' options must be used when running the 'impacket-ntlmrelayx' command to enable the SOCKS proxy functionality.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]
- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Adversary-in-the-Middle|T1557 - Adversary-in-the-Middle]]
- [[Signed Script Proxy Execution|T1216 - Signed Script Proxy Execution]]

## Commands Used

- [[Disable SMB and HTTP servers in Responder Core]]

## Tags

- [[Active Directory Attacks]]
- [[Man-in-the-Middle attacks & relaying]]
- [[SMB Signing Disabled and IPv4]]
