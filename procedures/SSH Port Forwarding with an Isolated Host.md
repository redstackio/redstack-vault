---
id: 6991b9b9-a7b1-4957-be03-b910338a9058
name: SSH Port Forwarding with an Isolated Host
type: procedure
verified: true
submitted: true
created_at: '2019-10-26T01:22:51.426952+00:00'
updated_at: '2023-05-26T00:53:26.716788+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
techniques:
- '[[Connection Proxy|T1090 - Connection Proxy]]'
platforms:
- Linux
tags:
- '[[Command & Control]]'
- '[[data encryption]]'
- '[[Pivot]]'
commands:
- '[[SSH Local Port Forwarding to a Remote Server]]'
- '[[SSH Remote Port Forwarding to an Attacker]]'
---

# SSH Port Forwarding with an Isolated Host

**Status**: ✓ Verified

## Summary

SSH tunneling is useful when an attacker wants to reach a host in an isolated network, which is only accessible through an intermediary host. By creating one or more SSH tunnels between the intermediary host and attacker, attackers can access and interact with the isolated host, and potentially oth

## Description

# Description

SSH tunneling is useful when an attacker wants to reach a host in an isolated network, which is only accessible through an intermediary host. By creating one or more SSH tunnels between the intermediary host and attacker, attackers can access and interact with the isolated host, and potentially others on the isolated network. Local port forwarding can allow attackers to connect into an isolated network, while remote port forwarding can accommodate connections out.

# Instructions

## Local Port Forwarding 

Forward traffic from an isolated target, through an intermediary host, to an attacker, allowing the attacker to connect to ports on the isolated machine.

**Command** ([[SSH Local Port Forwarding to a Remote Server]]):

```bash
ssh -f -N -L $_ATTACKER_PORT:$_REMOTE_IP:$_REMOTE_PORT $_USER@$_TARGET_IP
```

For example, if an attacker wants to connect to port 80 on an isolated host (10.10.10.11), they can ssh into an intermediary host (10.10.10.10), which then forwards traffic from the isolated host to the attacker, on local port 8001.

**Code**: [[ssh -f -N -L 8001:10.10.10.11:80 root@10.10.10.10]]

## Remote Port Forwarding 

Forward a port from the attacker to an intermediary host's local port, allowing the attacker to receive traffic that is sent to the intermediary host, which is then tunneled to the attacker (useful for reverse shells with isolated hosts).

**Command** ([[SSH Remote Port Forwarding to an Attacker]]):

```bash
ssh -f -N -R $_REMOTE_PORT:$_REMOTE_IP:$_LOCAL_PORT $_USER@$_TARGET_IP
```

For example, if an attacker wants traffic sent from an isolated host (10.10.10.11) to an intermediary host (10.10.10.10) on port 4444, to be sent to the attacker, the command would be:

**Code**: [[ssh -f -N -R 4444:127.0.0.1:4444 root@10.10.10.10]]

## Platforms

- Linux

## Products

- Linux

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]

### Techniques

- [[Connection Proxy|T1090 - Connection Proxy]]

## Commands Used

- [[SSH Local Port Forwarding to a Remote Server]]
- [[SSH Remote Port Forwarding to an Attacker]]

## Tags

- [[Command & Control]]
- [[data encryption]]
- [[Pivot]]
