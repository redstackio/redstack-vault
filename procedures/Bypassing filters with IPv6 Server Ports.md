---
id: 4a168eaa-ad30-45a4-b0d1-1cf907f7ea0c
name: Bypassing filters with IPv6 Server Ports
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:37.278604+00:00'
updated_at: '2023-04-10T20:23:54.515250+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation for Defense Evasion|T1211 - Exploitation for Defense Evasion]]'
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[Bypassing filters]]'
- '[[Bypass localhost with [::]]]'
- '[[Server-Side Request Forgery]]'
commands:
- '[[Accessing HTTP service]]'
- '[[Accessing SMTP service]]'
- '[[Accessing Squid service]]'
- '[[Accessing SSH service]]'
- '[[Access Squid proxy on IPv6 address]]'
- '[[Access website on IPv6 address]]'
- '[[Connect to SSH on IPv6 address]]'
- '[[Send email using SMTP on IPv6 address]]'
---

# Bypassing filters with IPv6 Server Ports

## Summary

Bypassing filters with IPv6 Server Ports is a technique used in Server-Side Request Forgery attacks. This technique involves bypassing filters by using IPv6 Server Ports instead of the traditional IPv4 ports. This technique can be used to access internal resources that are not intended to be access

## Description

# Description

Bypassing filters with IPv6 Server Ports is a technique used in Server-Side Request Forgery attacks. This technique involves bypassing filters by using IPv6 Server Ports instead of the traditional IPv4 ports. This technique can be used to access internal resources that are not intended to be accessible from the outside. 

From a technical perspective, this technique involves sending a request to the target server with an IPv6 address and a port number. The server will then attempt to connect to the specified address and port, which can allow the attacker to access internal resources. 

The business value of this technique is that it allows attackers to access sensitive or confidential information that would otherwise be inaccessible, which can lead to data theft, unauthorized access, and other malicious activities.

## Requirements

1. Access to a vulnerable server

1. Knowledge of IPv6 Server Ports

## Defense

1. Implement input validation and sanitization to prevent Server-Side Request Forgery attacks

1. Use a web application firewall (WAF) to block requests to known malicious IPv6 addresses and ports

1. Monitor network traffic for unusual activity, such as connections to internal resources from external IP addresses

## Objectives

1. Access sensitive or confidential information

1. Gain unauthorized access to internal resources

1. Perform malicious activities on the target system

# Instructions

1. To check if a port is open, use the 'Test-NetConnection' cmdlet followed by the IP address and port number. For example, 'Test-NetConnection -ComputerName [::] -Port 80'

**Code**: [[http://[::]:80/
http://[::]:25/ SMTP
http://[::]:2]]

> This command provides a list of common network ports and the services that use them. It is useful for network administrators and security professionals who need to monitor network traffic and ensure that only authorized services are running on their systems. The 'Test-NetConnection' cmdlet can be used to test whether a specific port is open or closed on a remote computer. This can help identify potential security vulnerabilities and ensure that network services are functioning correctly.

**Command** ([[Accessing HTTP service]]):

```bash
http://[::]:80/
```

**Command** ([[Accessing SMTP service]]):

```bash
http://[::]:25/ SMTP
```

**Command** ([[Accessing SSH service]]):

```bash
http://[::]:22/ SSH
```

**Command** ([[Accessing Squid service]]):

```bash
http://[::]:3128/ Squid
```

2. To access the services running on this IPv6 server, use the following commands:

**Code**: [[http://0000::1:80/
http://0000::1:25/ SMTP
http://]]

> 1. HTTP: Use the command 'http://[0000:0000:0000:0000:0000:0000:0001]:80/' to access the web server.
2. SMTP: Use the command 'telnet [0000:0000:0000:0000:0000:0000:0001] 25' to access the SMTP server.
3. SSH: Use the command 'ssh [0000:0000:0000:0000:0000:0000:0001]' to access the SSH server.
4. Squid: Use the command 'telnet [0000:0000:0000:0000:0000:0000:0001] 3128' to access the Squid proxy server.

**Command** ([[Access website on IPv6 address]]):

```bash
http://0000::1:80/
```

**Command** ([[Send email using SMTP on IPv6 address]]):

```bash
http://0000::1:25/ SMTP
```

**Command** ([[Connect to SSH on IPv6 address]]):

```bash
http://0000::1:22/ SSH
```

**Command** ([[Access Squid proxy on IPv6 address]]):

```bash
http://0000::1:3128/ Squid
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation for Defense Evasion|T1211 - Exploitation for Defense Evasion]]
- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Commands Used

- [[Accessing HTTP service]]
- [[Accessing SMTP service]]
- [[Accessing Squid service]]
- [[Accessing SSH service]]
- [[Access Squid proxy on IPv6 address]]
- [[Access website on IPv6 address]]
- [[Connect to SSH on IPv6 address]]
- [[Send email using SMTP on IPv6 address]]

## Tags

- [[Bypassing filters]]
- [[Bypass localhost with [::]]]
- [[Server-Side Request Forgery]]
