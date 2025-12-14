---
id: cmd-whois-ip
data: whois target-ip
tags:
  - reconnaissance
  - verification
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:10.068Z'
verified: false
validated: true
submitted: true
---
# whois-ip-lookup

## Command

```bash
whois target-ip
```

## Description

Performs a WHOIS query on an IP address to retrieve ownership and organization details.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| target-ip | IP address to query | Yes |

## Examples

### Basic Usage

```bash
whois 192.168.1.1
```

## Expected Output

Details like 'Organization: U.S. Department of Defense', abuse contacts.

## Related

- [[commands/echo-nc-ssrf-trigger]]
- [[procedures/Verify-SSRF-via-Server-Logs-and-Whois]]
