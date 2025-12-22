---
data: 'wget https://www.haproxy.org/download/1.5/src/haproxy-1.5.3.tar.gz'
tags:
  - download
type: command
executor: bash
platforms:
  - Linux
id: 8da9abb7-bc69-4940-b732-3bab3e4731a3
created_at: '2025-12-13T09:01:22.120Z'
updated_at: '2025-12-13T09:01:22.120Z'
verified: false
validated: true
submitted: true
---
# wget Download HAProxy

## Command

```bash
wget https://www.haproxy.org/download/1.5/src/haproxy-1.5.3.tar.gz
```

## Description

Downloads the HAProxy 1.5.3 source code tarball from the official website, used in setting up a vulnerable proxy for smuggling demonstrations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `url` | Specifies the URL to download from | Yes |

## Examples

### Basic Usage

```bash
wget https://www.haproxy.org/download/1.5/src/haproxy-1.5.3.tar.gz
```

## Expected Output

Downloaded tarball file named haproxy-1.5.3.tar.gz.

## Related

- [[procedures/Compile-and-Setup-HAProxy-Frontend-Proxy]]
- [[tools/wget]]
