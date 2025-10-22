---
id: 09c18375-cb75-4d26-915c-0b981d999a20
name: Remote Port Forwarding with Reverse SSH Tunneling
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:22.492622+00:00'
updated_at: '2023-04-10T20:25:19.119356+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Connection Proxy|T1090 - Connection Proxy]]'
- '[[Remote Services|T1021 - Remote Services]]'
tags:
- '[[Network Pivoting Techniques]]'
- '[[Remote Port Forwarding]]'
- '[[SSH]]'
commands:
- '[[Reverse SSH tunneling to local machine]]'
- '[[Reverse SSH tunneling to remote machine]]'
---

# Remote Port Forwarding with Reverse SSH Tunneling

## Summary

Remote port forwarding with reverse SSH tunneling is a technique used by attackers to bypass network security measures and gain access to a remote host. This technique involves creating a secure SSH tunnel between the attacker's machine and the remote host, and forwarding traffic from a local port 

## Description

# Description

Remote port forwarding with reverse SSH tunneling is a technique used by attackers to bypass network security measures and gain access to a remote host. This technique involves creating a secure SSH tunnel between the attacker's machine and the remote host, and forwarding traffic from a local port on the attacker's machine to a port on the remote host. This allows the attacker to access resources on the remote host as if they were on their own machine. This technique can be used to bypass firewalls and other network security measures, and can be particularly useful for exfiltrating data from a compromised network.

From a technical perspective, this technique requires the attacker to have access to a machine on the target network that has SSH access to the remote host. The attacker can then use the `ssh` command to create a reverse SSH tunnel, which will forward traffic from a local port on their machine to a port on the remote host. The attacker can then connect to the forwarded port on their own machine to access resources on the remote host.

From a business perspective, this technique can be used by attackers to steal sensitive data from a compromised network. By bypassing network security measures, attackers can gain access to data that would otherwise be protected. It is important for organizations to be aware of this technique and take steps to prevent it from being used against them.

## Requirements

1. SSH access to a machine on the target network

1. Ability to create a reverse SSH tunnel

## Defense

1. Monitor network traffic for signs of SSH tunneling

1. Restrict SSH access to only trusted hosts

1. Implement two-factor authentication for SSH access

## Objectives

1. Gain access to a remote host

1. Bypass network security measures

1. Exfiltrate data from a compromised network

# Instructions

1. To create a reverse SSH tunnel, use the ssh command with the -R option. This will allow you to connect to a remote server and forward traffic from a local port to a remote port on the server. The bindaddr is the IP address to bind the remote port to, port is the remote port number, localhost is the IP address of the local machine, localport is the local port number, user is the username on the remote server, and host is the IP address or hostname of the remote server.

**Code**: [[ssh -R [bindaddr]:[port]:[localhost]:[localport] []]

> The reverse SSH tunneling is a technique used to access a remote system securely even if the remote system is behind a firewall or NAT. This technique works by creating a tunnel between the local and remote systems, allowing traffic to be forwarded from the local system to the remote system via the tunnel. The -R option is used to specify the reverse tunnel, and the bindaddr, port, localhost, and localport options are used to specify the details of the tunnel. The username and hostname of the remote server are also required to establish the SSH connection.

**Command** ([[Reverse SSH tunneling to local machine]]):

```bash
ssh -R [bindaddr]:[port]:[localhost]:[localport] [user]@[host]
```

**Command** ([[Reverse SSH tunneling to remote machine]]):

```bash
ssh -R 3389:10.1.1.224:3389 root@10.11.0.32
```

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Connection Proxy|T1090 - Connection Proxy]]
- [[Remote Services|T1021 - Remote Services]]

## Commands Used

- [[Reverse SSH tunneling to local machine]]
- [[Reverse SSH tunneling to remote machine]]

## Tags

- [[Network Pivoting Techniques]]
- [[Remote Port Forwarding]]
- [[SSH]]
