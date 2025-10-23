---
id: b93accbc-928e-4104-ba02-742d1b5412d0
name: Network Pivoting with sshuttle
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:22.718650+00:00'
updated_at: '2023-04-10T20:25:19.563728+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Connection Proxy|T1090 - Connection Proxy]]'
- '[[Remote Services|T1021 - Remote Services]]'
sub_techniques:
- '[[Windows Remote Management|T1021.006 - Windows Remote Management]]'
tags:
- '[[Network Pivoting Techniques]]'
- '[[sshuttle]]'
commands:
- '[[Connect to pivot host]]'
- '[[Connect to remote server]]'
- '[[Connect using private key]]'
- '[[Exclude network from tunnel]]'
- '[[Install sshuttle]]'
---

# Network Pivoting with sshuttle

## Summary

Network pivoting is a technique used by attackers to move laterally through a network by compromising an intermediate system and using it to attack other systems within the network. Sshuttle is a tool that can be used as an alternative to traditional VPNs for network pivoting. It allows a user to c

## Description

# Description

Network pivoting is a technique used by attackers to move laterally through a network by compromising an intermediate system and using it to attack other systems within the network. Sshuttle is a tool that can be used as an alternative to traditional VPNs for network pivoting. It allows a user to create a VPN-like connection between two machines, enabling the user to access resources on the remote network as if they were directly connected to it. This technique can be used by attackers to bypass network security controls and gain access to sensitive data.

From a technical perspective, sshuttle works by creating a transparent proxy server on the compromised system, which forwards traffic to the remote network. This traffic is encrypted, ensuring that it cannot be intercepted by network security controls. Business value of this technique is that it allows remote workers to access company resources without the need for a traditional VPN, which can be expensive and difficult to manage.

 

## Requirements

1. Access to a compromised system on the target network

1. SSH access to the compromised system

1. Python installed on both the compromised system and the system connecting to the VPN

 

## Defense

1. Implement strict access controls to limit who can connect to the compromised system

1. Monitor network traffic for suspicious activity, such as large amounts of encrypted traffic going to a single IP address

1. Implement network segmentation to limit the impact of a compromised system

 

## Objectives

1. Gain access to sensitive data on a remote network

1. Bypass network security controls

 

# Instructions

1. To use sshuttle as a VPN alternative, follow these steps:
1. Install sshuttle using your package manager (e.g. pacman, apt-get)
2. Connect to the remote server using sshuttle with the following command:
   sshuttle -vvr user@10.10.10.10 10.1.1.0/24
   sshuttle -vvr username@pivot_host 10.2.2.0/24
3. To use a private key, use the following command:
   sshuttle -vvr root@10.10.10.10 10.1.1.0/24 -e "ssh -i ~/.ssh/id_rsa"
4. To exclude some networks from being transmitted over the tunnel, use the -x option as follows:
   sshuttle -vvr user@10.10.10.10 10.1.1.0/24 -x x.x.x.x/24

 



**Code**: [[pacman -Sy sshuttle
apt-get install sshuttle
sshut]]



> sshuttle is a transparent proxy server that works as a poor man's VPN. It forwards over ssh and is useful for creating a VPN-like connection to a remote server. The -v option enables verbose output, -r specifies the remote server, and the IP address and subnet mask specify the network to forward traffic for. The -e option specifies the command to use to connect to the remote server. The -x option can be used to exclude some networks from being transmitted over the tunnel.



**Command** ([[Install sshuttle]]):

```bash
pacman -Sy sshuttle
apt-get install sshuttle
```





**Command** ([[Connect to remote server]]):

```bash
sshuttle -vvr user@10.10.10.10 10.1.1.0/24
```





**Command** ([[Connect to pivot host]]):

```bash
sshuttle -vvr username@pivot_host 10.2.2.0/24
```





**Command** ([[Connect using private key]]):

```bash
$ sshuttle -vvr root@10.10.10.10 10.1.1.0/24 -e "ssh -i ~/.ssh/id_rsa"
```





**Command** ([[Exclude network from tunnel]]):

```bash
# -x x.x.x.x.x/24
```



## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Connection Proxy|T1090 - Connection Proxy]]
- [[Remote Services|T1021 - Remote Services]]

### Sub-Techniques

- [[Windows Remote Management|T1021.006 - Windows Remote Management]]

## Commands Used

- [[Connect to pivot host]]
- [[Connect to remote server]]
- [[Connect using private key]]
- [[Exclude network from tunnel]]
- [[Install sshuttle]]

## Tags

- [[Network Pivoting Techniques]]
- [[sshuttle]]


