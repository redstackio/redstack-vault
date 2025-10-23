---
id: a393151c-a873-42d0-80fe-f683327ead9f
name: Ligolo Reverse Tunneling
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:22.799630+00:00'
updated_at: '2023-04-10T20:25:12.821529+00:00'
tags:
- '[[Ligolo]]'
- '[[Network Pivoting Techniques]]'
commands:
- '[[Build Ligolo]]'
- '[[Clone Ligolo and Install Dependencies]]'
- '[[Generate Self-Signed TLS Certificates]]'
---

# Ligolo Reverse Tunneling

## Summary

Ligolo is a reverse tunneling technique used for lateral movement and exfiltration. It allows an attacker to bypass network defenses by opening a connection from the victim's machine to the attacker's machine. This technique is commonly used in post-exploitation scenarios to maintain persistence an

## Description

# Description

Ligolo is a reverse tunneling technique used for lateral movement and exfiltration. It allows an attacker to bypass network defenses by opening a connection from the victim's machine to the attacker's machine. This technique is commonly used in post-exploitation scenarios to maintain persistence and to move laterally within a network.

Technical Explanation: Ligolo works by opening a reverse SSH tunnel from the victim's machine to the attacker's machine. This allows the attacker to access the victim's machine as if they were on the same network. The attacker can then use this connection to move laterally within the network, exfiltrate data, or perform other malicious activities.

Business Value: Ligolo can be used to gain access to sensitive data and systems within a network. This can lead to financial losses, reputation damage, and legal consequences for the organization.

 

## Requirements

1. Access to a vulnerable machine within the network

1. SSH access to the vulnerable machine

 

## Defense

1. Monitor network traffic for any unusual SSH connections

1. Implement network segmentation to limit lateral movement

1. Use multi-factor authentication to prevent unauthorized access

 

## Objectives

1. Gain access to sensitive data and systems within the network

1. Maintain persistence within the network

1. Move laterally within the network

 

# Instructions

1. To use Ligolo for reverse tunneling, follow these steps:
1. Clone the Ligolo repository by running the command: `git clone https://github.com/sysdream/ligolo`
2. Navigate to the cloned repository by running the command: `cd ligolo`
3. Install the dependencies by running the command: `make dep`
4. Generate self-signed TLS certificates by running the command: `make certs TLS_HOST=example.com`
5. Build the binaries by running the command: `make build-all`

 



**Code**: [[# Get Ligolo and dependencies
cd `go env GOPATH`/s]]



> The Ligolo command is used for reverse tunneling and is specifically designed for use by pentesters. The command clones the Ligolo repository and installs its dependencies. It then generates self-signed TLS certificates and places them in the certs folder. Finally, it builds the binaries required for reverse tunneling. The `TLS_HOST` argument specifies the hostname for the self-signed TLS certificate.



**Command** ([[Clone Ligolo and Install Dependencies]]):

```bash
cd `go env GOPATH`/src
git clone https://github.com/sysdream/ligolo
cd ligolo
make dep

```





**Command** ([[Generate Self-Signed TLS Certificates]]):

```bash
make certs TLS_HOST=example.com

```





**Command** ([[Build Ligolo]]):

```bash
make build-all
```



## Commands Used

- [[Build Ligolo]]
- [[Clone Ligolo and Install Dependencies]]
- [[Generate Self-Signed TLS Certificates]]

## Tags

- [[Ligolo]]
- [[Network Pivoting Techniques]]


