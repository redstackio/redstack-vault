---
id: c1b2c3d4-e5f6-7890-abcd-ef1234567895
data: grep -r "spdy" /etc/nginx/
tags:
  - config-search
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:23:32.699Z'
verified: false
validated: true
submitted: true
---
# grep-search-config

## Command

```bash
grep -r "spdy" /etc/nginx/
```

## Description

Recursively searches nginx configuration files for SPDY references to identify if the module is enabled, aiding in vulnerability verification for CVE-2014-0133.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-r` | Recursive search | Yes |
| `"spdy"` | Search term for SPDY | Yes |
| `/etc/nginx/` | Directory path | Yes |

## Examples

### Basic Usage

```bash
grep -r "spdy" /etc/nginx/
```

### Advanced Usage

```bash
grep -r -i "spdy\|http_spdy_module" /etc/nginx/ 2>/dev/null
```

## Expected Output

Lines from config files containing "spdy", e.g., "listen 443 ssl spdy;" indicating vulnerable configuration.

## Related

- [[Related Procedure: Verify-SPDY-Module-Configuration-for-CVE-2014-0133]]
