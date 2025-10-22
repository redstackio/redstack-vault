---
id: 328bb037-68a3-47c9-84cc-b81210ce9f48
name: SSH Local Port Forwarding
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:22.463678+00:00'
updated_at: '2023-04-10T20:25:14.304451+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Connection Proxy|T1090 - Connection Proxy]]'
- '[[NTFS File Attributes|T1096 - NTFS File Attributes]]'
- '[[Replication Through Removable Media|T1091 - Replication Through Removable Media]]'
tags:
- '[[Local Port Forwarding]]'
- '[[Network Pivoting Techniques]]'
- '[[SSH]]'
commands:
- '[[SSH Tunneling Command]]'
---

# SSH Local Port Forwarding

## Summary

SSH Local Port Forwarding is a technique used to pivot through a network by forwarding traffic from a local port to a remote destination through a SSH tunnel. This technique is useful for evading network security measures such as firewalls and network monitoring tools. By using SSH encryption, atta

## Description

# Description

SSH Local Port Forwarding is a technique used to pivot through a network by forwarding traffic from a local port to a remote destination through a SSH tunnel. This technique is useful for evading network security measures such as firewalls and network monitoring tools. By using SSH encryption, attackers can maintain a persistent connection and bypass network security measures undetected.

From a technical perspective, SSH Local Port Forwarding works by creating a secure tunnel between a local machine and a remote server. Traffic is then forwarded through this tunnel from the local machine to the remote server. This technique can be used to gain access to internal network resources that are not directly accessible from the internet.

The business value of SSH Local Port Forwarding is that it allows attackers to gain access to sensitive data and resources that are not publicly accessible. This can lead to data theft, financial loss, and reputational damage.

## Requirements

1. Valid SSH credentials

1. Network access to the remote server

1. A tool capable of creating SSH tunnels

## Defense

1. Monitor network traffic for any suspicious SSH connections

1. Configure firewalls to restrict SSH access to trusted sources

1. Implement multi-factor authentication for SSH connections

## Objectives

1. Gain access to internal network resources

1. Bypass network security measures

1. Maintain a persistent connection

# Instructions

1. Use this command to create a secure SSH tunnel and forward traffic from a local port to a remote host and port.

**Code**: [[ssh -L [bindaddr]:[port]:[dsthost]:[dstport] [user]]

> -L: Specifies that the given port on the local (client) host is to be forwarded to the given host and port on the remote side.
[bindaddr]: The IP address or hostname of the interface on the client machine to bind the forwarded port to.
[port]: The local port number to forward.
[dsthost]: The hostname or IP address of the remote machine to forward the port to.
[dstport]: The port number on the remote machine to forward the port to.
[user]: The username to use when connecting to the remote machine.
[host]: The hostname or IP address of the remote machine to connect to.

**Command** ([[SSH Tunneling Command]]):

```bash
ssh -L [bindaddr]:[port]:[dsthost]:[dstport] [user]@[host]
```

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Initial Access|TA0001 - Initial Access]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Connection Proxy|T1090 - Connection Proxy]]
- [[NTFS File Attributes|T1096 - NTFS File Attributes]]
- [[Replication Through Removable Media|T1091 - Replication Through Removable Media]]

## Commands Used

- [[SSH Tunneling Command]]

## Tags

- [[Local Port Forwarding]]
- [[Network Pivoting Techniques]]
- [[SSH]]
