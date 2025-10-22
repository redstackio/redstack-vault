---
id: cfb9a7aa-fd7d-45d4-9e7b-8ef4d0cd54b7
name: Localhost SSRF Payloads
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:37.210346+00:00'
updated_at: '2023-04-10T20:24:10.133430+00:00'
tactics:
- '[[Initial Access|TA0001 - Initial Access]]'
techniques:
- '[[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]'
tags:
- '[[Payloads with localhost]]'
- '[[Server-Side Request Forgery]]'
commands:
- '[[List of Localhost Ports]]'
- '[[List of URLs]]'
---

# Localhost SSRF Payloads

## Summary

Localhost SSRF payloads are used to exploit server-side request forgery vulnerabilities that allow an attacker to send crafted requests to the server. These requests can be used to bypass access controls or to access internal resources. The payloads use localhost URLs to access resources that are n

## Description

# Description

Localhost SSRF payloads are used to exploit server-side request forgery vulnerabilities that allow an attacker to send crafted requests to the server. These requests can be used to bypass access controls or to access internal resources. The payloads use localhost URLs to access resources that are normally inaccessible from the internet. This technique can be used to exfiltrate data or to execute commands on the server.

From a technical perspective, the attacker crafts a request that includes a URL parameter pointing to a localhost resource. The server then makes a request to the specified resource, which is interpreted as a request to a local resource by the server. This allows the attacker to bypass access controls and access internal resources.

The business value of this technique is that it allows an attacker to gain unauthorized access to sensitive data or to execute commands on a server, which can result in data theft, system compromise, or other types of damage.

## Requirements

1. Access to a vulnerable server

1. Ability to craft requests with localhost URLs

## Defense

1. Implement input validation to prevent crafted requests with localhost URLs

1. Use a web application firewall to block requests with localhost URLs

1. Monitor network traffic for requests to internal resources

## Objectives

1. Gain unauthorized access to sensitive data

1. Execute commands on a server

# Instructions

1. To access a service running on your own machine, you can use the `localhost` URL followed by the port number. For example, `http://localhost:80` will access the service running on port 80 of your own machine.

**Code**: [[http://localhost:80
http://localhost:443
http://lo]]

> The `localhost` URL is a reserved hostname that always refers to the local machine. By using this URL, you can access services running on your own machine without needing to know the IP address of your machine. The port number specifies which service to access, with commonly used ports including 80 for HTTP, 443 for HTTPS, and 22 for SSH.

**Command** ([[List of Localhost Ports]]):

```bash
http://localhost:80
http://localhost:443
http://localhost:22
```

2. To access the localhost URLs mentioned above, enter the respective URL in your web browser or use a command-line tool such as cURL or PowerShell's Invoke-WebRequest command.

**Code**: [[http://127.0.0.1:80
http://127.0.0.1:443
http://12]]

> The URLs mentioned in the `data` field are for accessing services running on the local machine. `127.0.0.1` is the IP address for the loopback interface, which means that any traffic sent to this address is immediately returned back to the sender. Port `80` is the default port for HTTP traffic, port `443` is the default port for HTTPS traffic, and port `22` is the default port for SSH traffic. Accessing these URLs can be useful for testing web applications or connecting to local services via SSH.

3. To check the available ports on your machine, use the following command:

**Code**: [[http://0.0.0.0:80
http://0.0.0.0:443
http://0.0.0.]]

> This command will display a list of available ports on your machine that can be used for various applications. The `0.0.0.0` indicates that the ports are available for use on any IP address. The numbers after the colon indicate the specific port numbers that are available. Port 80 is commonly used for HTTP web traffic, port 443 is commonly used for HTTPS web traffic, and port 22 is commonly used for SSH connections.

**Command** ([[List of URLs]]):

```bash
http://0.0.0.0:80
http://0.0.0.0:443
http://0.0.0.0:22
```

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access|TA0001 - Initial Access]]

### Techniques

- [[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]

## Commands Used

- [[List of Localhost Ports]]
- [[List of URLs]]

## Tags

- [[Payloads with localhost]]
- [[Server-Side Request Forgery]]
