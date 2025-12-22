---
id: 7d25831d-b45d-4548-8898-410456010c32
name: nmap-enumerate-http-methods
type: command
executor: bash
data: nmap --script http-methods $_TARGET_HOST
output: |-
  PORT   STATE SERVICE REASON
  80/tcp open  http    syn-ack
  | http-methods:
  |_  Supported Methods: GET HEAD POST OPTIONS TRACE
created_at: '2020-07-19T06:50:16.838896+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Web
tags:
  - Enumeration
  - Web
verified: true
validated: true
---

# nmap-enumerate-http-methods

## Command

```bash
nmap --script http-methods $_TARGET_HOST
```

## Description

This command uses Nmap's http-methods NSE script to scan a target web server and enumerate the HTTP methods it supports, such as GET, POST, or potentially insecure ones like TRACE. It is ideal for initial reconnaissance to identify misconfigurations without manual interaction.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_HOST | Target hostname or IP address (e.g., example.com or 192.168.1.1) | Yes |
| --script http-methods | Invokes the NSE script to perform HTTP method enumeration via OPTIONS request | Yes |

## Examples

### Basic Usage

```bash
nmap --script http-methods demo.testfire.net
```

### Advanced Usage

```bash
nmap -p 443 --script http-methods,http-methods.ssl=true example.com
```

## Expected Output

```
PORT   STATE SERVICE REASON
80/tcp open  http    syn-ack
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS TRACE
```

This output shows the open port and lists the supported methods from the Allow header.

## Related

- [[procedures/Enumerate-HTTP-Methods]]
- [[tools/Nmap]]
