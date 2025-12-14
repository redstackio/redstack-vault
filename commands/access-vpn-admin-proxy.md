---
id: cmd-uuid-1
data: 'curl -b "vpn_session=active" https://vpn.example.com/proxy/https/0/admin/'
tags:
  - proxy-access
type: command
output: Admin login page or interface
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.978Z'
verified: false
validated: true
submitted: true
---
# access-vpn-admin-proxy

## Command

```bash
curl -b "vpn_session=active" https://vpn.example.com/proxy/https/0/admin/
```

## Description

Access the internal admin interface via the VPN web proxy using an active session cookie, forwarding to localhost/admin.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-b` | Cookie for VPN session | Yes |
| `https://vpn.example.com/proxy/https/0/admin/` | Proxy URL to internal admin | Yes |

## Examples

### Basic Usage

```bash
curl -b "JSESSIONID=abc123" https://vpn.example.com/proxy/https/0/admin/
```

### Advanced Usage

```bash
curl -b "JSESSIONID=abc123" -k https://vpn.example.com/proxy/https/0/admin/ --verbose
```

## Expected Output

HTML of the admin login page or dashboard, indicating successful proxy forwarding.

## Related

- [[procedures/Access-Admin-Interface-via-VPN-Web-Proxy]]
