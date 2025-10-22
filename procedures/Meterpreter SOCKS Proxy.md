---
id: cd6de114-152e-4f75-918b-1f7f89182646
name: Meterpreter SOCKS Proxy
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:21.626597+00:00'
updated_at: '2023-04-10T20:25:04.007867+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
techniques:
- '[[Connection Proxy|T1090 - Connection Proxy]]'
tags:
- '[[Metasploit]]'
- '[[Meterpreter - Basic]]'
- '[[Use SOCKS Proxy]]'
commands:
- '[[Set Proxies]]'
---

# Meterpreter SOCKS Proxy

## Summary

Meterpreter SOCKS Proxy is a technique used to redirect network traffic through a compromised system to a remote host. This technique is commonly used by attackers to hide their true location and identity while performing malicious activities. The SOCKS proxy can be used to tunnel traffic for any p

## Description

# Description

Meterpreter SOCKS Proxy is a technique used to redirect network traffic through a compromised system to a remote host. This technique is commonly used by attackers to hide their true location and identity while performing malicious activities. The SOCKS proxy can be used to tunnel traffic for any protocol, making it a versatile tool for attackers. 

From a technical standpoint, Meterpreter's SOCKS proxy works by opening a local port on the compromised system and forwarding traffic from that port to a remote host. This allows attackers to route traffic from any tool or application through the compromised system, making it appear as if the traffic is originating from that system.

From a business perspective, this technique can allow attackers to bypass network security controls and exfiltrate sensitive data without detection. It is important for organizations to be aware of this technique and take steps to prevent it from being used against them.

## Requirements

1. Compromised system with Meterpreter access

## Defense

1. Disable unnecessary services and protocols on network devices

1. Use network segmentation to limit the spread of a compromise

1. Monitor network traffic for unusual activity

## Objectives

1. Redirect network traffic through a compromised system to a remote host

1. Bypass network security controls

# Instructions

1. This command sets global proxies for the system using the 'setg' keyword followed by the name of the variable and its value.

**Code**: [[setg Proxies socks4:127.0.0.1:1080]]

> The 'setg' command is used to set global variables in PowerShell. In this case, we are setting the 'Proxies' variable to the value 'socks4:127.0.0.1:1080', which specifies a SOCKS4 proxy server running on the local machine at port 1080. This command will affect all network traffic on the system that uses the default proxy settings. Note that this command may require administrative privileges to execute.

**Command** ([[Set Proxies]]):

```bash
setg Proxies socks4:127.0.0.1:1080
```

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]

### Techniques

- [[Connection Proxy|T1090 - Connection Proxy]]

## Commands Used

- [[Set Proxies]]

## Tags

- [[Metasploit]]
- [[Meterpreter - Basic]]
- [[Use SOCKS Proxy]]
