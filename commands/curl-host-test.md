---
id: cmd-uuid-004
data: 'curl -H "Host: mta1a1.spmail.uber.com" http://your-ec2-ip'
tags:
  - http
  - test
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:10.913Z'
verified: false
validated: true
submitted: true
---
# curl-host-test

## Command

```bash
curl -H "Host: mta1a1.spmail.uber.com" http://your-ec2-ip
```

## Description

Tests HTTP access to a server by spoofing the Host header, verifying subdomain resolution post-takeover.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -H "Host: ..." | Sets custom Host header | Yes |
| http://ip | Target server IP | Yes |

## Examples

### Basic Usage

```bash
curl -H "Host: mta1a1.spmail.uber.com" http://52.XX.XX.XX
```

### Advanced Usage

```bash
curl -H "Host: mta1a1.spmail.uber.com" -v http://52.XX.XX.XX
```

## Expected Output

HTML or content from your server, confirming control.

## Related

- [[Related Procedure: Verify-Subdomain-Takeover]]
