---
id: 295b7b83-8f2e-443e-8c4f-4b12414d2b0c
name: Cobalt Strike Infrastructure Redirector Installation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:16.281498+00:00'
updated_at: '2023-04-10T20:36:24.187304+00:00'
tags:
- '[[Cobalt Strike]]'
- '[[Infrastructure]]'
- '[[Redirectors]]'
commands:
- '[[Install socat and forward traffic to team server]]'
---

# Cobalt Strike Infrastructure Redirector Installation

## Summary

The Cobalt Strike Infrastructure Redirector Installation procedure involves installing Socat to forward traffic from a redirector to a Cobalt Strike server. This technique is commonly used by attackers to hide their command and control traffic and evade detection. 

Socat is a utility that allows f

## Description

# Description

The Cobalt Strike Infrastructure Redirector Installation procedure involves installing Socat to forward traffic from a redirector to a Cobalt Strike server. This technique is commonly used by attackers to hide their command and control traffic and evade detection. 

Socat is a utility that allows for bidirectional data transfer between two endpoints, and is commonly used as a network proxy. By installing Socat on a redirector, an attacker can redirect traffic to a Cobalt Strike server, allowing them to control infected machines and exfiltrate data.

The business value of this technique is that it allows an attacker to maintain a persistent foothold in a target network and steal sensitive data.

 

## Requirements

1. Access to a redirector

1. Access to a Cobalt Strike server

 

## Defense

1. Monitor network traffic for suspicious activity, such as traffic being forwarded to a Cobalt Strike server

1. Use network segmentation to limit the potential impact of an attacker who has gained access to a redirector

1. Implement strong authentication mechanisms to prevent unauthorized access to the redirector and Cobalt Strike server

 

## Objectives

1. Install Socat on a redirector to forward traffic to a Cobalt Strike server

1. Maintain a persistent foothold in a target network

1. Steal sensitive data from the target network

 

# Instructions

1. To use this command, first install Socat on your system by running the following command:

sudo apt install socat

Once Socat is installed, you can use the following command to forward traffic from port 80 to the specified TEAM SERVER:

socat TCP4-LISTEN:80,fork TCP4:[TEAM SERVER]:80

 



**Code**: [[sudo apt install socat
socat TCP4-LISTEN:80,fork T]]



> This command installs Socat, a utility that allows for bidirectional data transfer between two endpoints, and sets up a TCP4 listener on port 80 that forwards incoming traffic to the specified TEAM SERVER. The 'fork' option allows for multiple connections to be handled simultaneously. This can be useful for scenarios where you want to redirect incoming web traffic to a different server, or for setting up a reverse proxy.



**Command** ([[Install socat and forward traffic to team server]]):

```bash
sudo apt install socat
socat TCP4-LISTEN:80,fork TCP4:[TEAM SERVER]:80
```



## Commands Used

- [[Install socat and forward traffic to team server]]

## Tags

- [[Cobalt Strike]]
- [[Infrastructure]]
- [[Redirectors]]


