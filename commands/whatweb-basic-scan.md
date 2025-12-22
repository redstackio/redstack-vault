---
id: 5a83e245-fc3e-4827-9a51-86ae571f2e04
name: whatweb-basic-scan
type: command
executor: bash
data: whatweb $_TARGET_URL
output: >-
  root@kali:~# whatweb http://10.10.10.10

  http://10.10.10.10 [200 OK] Apache[2.2.8], Country[RESERVED][ZZ],
  HTTPServer[Ubuntu Linux][Apache/2.2.8 (Ubuntu) DAV/2], IP[10.10.10.10],
  PHP[5.2.4-2ubuntu5.10], Title[Host - Linux], WebDAV[2],
  X-Powered-By[PHP/5.2.4-2ubuntu5.10]
created_at: '2019-09-13T22:29:10.949912+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Web
tags:
  - '[[Enumeration]]'
  - '[[Web Applications]]'
verified: true
validated: true
---

# whatweb-basic-scan

## Command

```bash
whatweb $_TARGET_URL
```

## Description

This command performs a basic scan of a target URL using WhatWeb to identify web technologies such as servers, CMS, and plugins. It uses default aggression level (1, stealthy) and is ideal for initial reconnaissance without triggering alerts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | The URL or IP address of the target web server (e.g., http://10.10.10.10) | Yes |

## Examples

### Basic Usage

Scan a web server at a specific IP:

```bash
whatweb http://10.10.10.10
```

### Advanced Usage

Scan with verbose output:

```bash
whatweb -v http://example.com
```

## Expected Output

The output lists detected technologies in a concise format, including HTTP status, server details, and plugins:

```
root@kali:~# whatweb http://10.10.10.10
http://10.10.10.10 [200 OK] Apache[2.2.8], Country[RESERVED][ZZ], HTTPServer[Ubuntu Linux][Apache/2.2.8 (Ubuntu) DAV/2], IP[10.10.10.10], PHP[5.2.4-2ubuntu5.10], Title[Host - Linux], WebDAV[2], X-Powered-By[PHP/5.2.4-2ubuntu5.10]
```

Success is indicated by the presence of detected components without errors.

## Related

- [[tools/WhatWeb]] (parent tool documentation).
- [[commands/whatweb-aggressive-scan]] (for more detailed probing).
