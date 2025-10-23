---
id: b720e655-13f1-4c80-b9b2-45331bf6fbb8
name: SSH Tunneling and SOCKS Proxy
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:22.430126+00:00'
updated_at: '2023-04-10T20:25:19.990384+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
techniques:
- '[[Connection Proxy|T1090 - Connection Proxy]]'
- '[[Standard Application Layer Protocol|T1071 - Standard Application Layer Protocol]]'
sub_techniques:
- '[[Web Protocols|T1071.001 - Web Protocols]]'
tags:
- '[[Network Pivoting Techniques]]'
- '[[SOCKS Proxy]]'
- '[[SSH]]'
commands:
- '[[Enter Command]]'
- '[[SSH in Background]]'
- '[[SSH Port Forwarding]]'
---

# SSH Tunneling and SOCKS Proxy

## Summary

SSH tunneling and SOCKS proxy are network pivoting techniques that allow an attacker to bypass firewalls and access remote systems. SSH tunneling is the process of forwarding network traffic through an encrypted SSH connection. SOCKS proxy is a protocol that allows a client to establish a TCP conne

## Description

# Description

SSH tunneling and SOCKS proxy are network pivoting techniques that allow an attacker to bypass firewalls and access remote systems. SSH tunneling is the process of forwarding network traffic through an encrypted SSH connection. SOCKS proxy is a protocol that allows a client to establish a TCP connection to a server and then route all the traffic through that connection. These techniques can be used to access systems that are not directly accessible from the attacker's machine.

From an offensive perspective, these techniques can be used to gain access to sensitive systems, exfiltrate data, and maintain persistence. From a technical standpoint, SSH tunneling and SOCKS proxy rely on the ability to establish a connection between the attacker's machine and the target system. The attacker must have valid credentials and network access to the target system. From a business value standpoint, these techniques can be used to steal sensitive data, disrupt operations, and cause reputational damage.

 

## Requirements

1. Valid credentials for the target system

1. Network access to the target system

1. SSH client software

 

## Defense

1. Monitor network traffic for signs of SSH tunneling and SOCKS proxy usage

1. Implement network segmentation to limit lateral movement

1. Enforce strong authentication policies to prevent credential theft

 

## Objectives

1. Gain access to sensitive systems

1. Exfiltrate data

1. Maintain persistence

 

# Instructions

1. To create an SSH tunnel, use the following commands:

1. ssh -D8080 [user]@[host]
This command creates a dynamic application-level port forwarding tunnel. It listens on port 8080 on your local machine and forwards all traffic to the specified [host] via SSH.

2. ssh -N -f -D 9000 [user]@[host]
This command creates a dynamic SOCKS proxy tunnel. It listens on port 9000 on your local machine and forwards all traffic to the specified [host] via SSH. The -N option tells SSH not to execute a remote command and the -f option tells SSH to run in the background.

 



**Code**: [[ssh -D8080 [user]@[host]

ssh -N -f -D 9000 [user]]]



> The -D option specifies the local port number to use for the SOCKS proxy. The -N option tells SSH not to execute a remote command and the -f option tells SSH to run in the background. The [user]@[host] argument specifies the username and hostname of the remote server to connect to. Once the tunnel is created, you can configure your applications to use the local SOCKS proxy on the specified port (8080 or 9000) to route their traffic through the remote server.



**Command** ([[SSH Port Forwarding]]):

```bash
ssh -D8080 [user]@[host]
```





**Command** ([[SSH in Background]]):

```bash
ssh -N -f -D 9000 [user]@[host]
```



2. To use Konami SSH Port Forwarding, press the Enter key followed by the ~C key combination. Then type -D 1090 and hit Enter again.

 



**Code**: [[[ENTER] + [~C]
-D 1090]]



> Konami SSH Port Forwarding is a technique used to forward traffic from a local machine to a remote machine through an SSH connection. The -D flag specifies the local port to use for the forwarding and 1090 is the port number. This command is useful for accessing web services or applications running on a remote machine that are not accessible from the local network.



**Command** ([[Enter Command]]):

```bash
[ENTER] + [~C]
-D 1090
```



## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]

### Techniques

- [[Connection Proxy|T1090 - Connection Proxy]]
- [[Standard Application Layer Protocol|T1071 - Standard Application Layer Protocol]]

### Sub-Techniques

- [[Web Protocols|T1071.001 - Web Protocols]]

## Commands Used

- [[Enter Command]]
- [[SSH in Background]]
- [[SSH Port Forwarding]]

## Tags

- [[Network Pivoting Techniques]]
- [[SOCKS Proxy]]
- [[SSH]]


