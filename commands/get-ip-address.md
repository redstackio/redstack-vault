---
id: 4e16f546-6f20-4556-bf8a-421489497a99
name: get-ip-address
type: command
executor: bash
data: nslookup $_MALICIOUS_HOST
output: null
created_at: '2023-04-06T03:56:31.693426+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - recon
verified: true
validated: true
---

# get-ip-address

## Command

```bash
nslookup $_MALICIOUS_HOST
```

## Description

Resolves the IP address of the malicious domain to verify DNS setup before using in redirects.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_MALICIOUS_HOST | Domain to resolve (e.g., evil-website.tld) | Yes |

## Examples

### Basic Usage

```bash
nslookup evil-website.tld
```

## Expected Output

Server: 8.8.8.8
Address: 192.168.1.100#53

Name: evil-website.tld
Address: 192.168.1.100

## Related

- [[procedures/Open-URL-Redirection-Exploitation]]
- [[commands/ping-evil-website]]
