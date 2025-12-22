---
id: cef1bf46-ab4e-44bf-8be0-818380e8f399
name: host-resolve-domain
type: command
executor: bash
data: host $_DOMAIN
output: null
created_at: '2020-07-24T17:11:26.799981+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
  - Unix
tags:
  - reconnaissance
  - dns
verified: true
validated: true
---

# host-resolve-domain

## Command

```bash
host $_DOMAIN
```

## Description

This command performs a DNS lookup on the specified domain name using the 'host' tool, retrieving A records (IP addresses) and other available DNS information. It is used for basic reconnaissance to verify domain resolution and gather initial network details.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | The domain name to resolve (e.g., example.com) | Yes |

## Examples

### Basic Usage

```bash
host owasp.com
```

### Advanced Usage

For more verbose output or specific query types:

```bash
host -t MX owasp.com
```

## Expected Output

When successful, the command outputs DNS records for the domain. For example, resolving 'owasp.com':

```
owasp.com has address 185.199.108.153
owasp.com has IPv6 address 2606:50c0:8000::153
owasp.com mail is handled by 10 smtp.github.com.
```

If the domain does not exist:

```
Host owasp.com not found: 3(NXDOMAIN)
```

## Related

- [[procedures/Resolve-Domain-Using-Host-Command]]
- [[tools/host]]
