---
id: cmd-uuid-2
data: nc -lvp 25
tags:
  - network-listen
  - smtp
  - capture
type: command
output: >-
  Connection from ec2-18-213-100-122.compute-1.amazonaws.com, SMTP commands like
  HELO test.org, MAIL FROM:, RCPT TO:kontakt@deepsec.pl, DATA Test
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:09.336Z'
verified: false
validated: true
submitted: true
---
# nc-listen-smtp-port

## Command

```bash
nc -lvp 25
```

## Description

Uses netcat to listen on port 25 in verbose mode, capturing incoming TCP connections and data from SSRF-induced SMTP interactions on a VPS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -l | Listen mode | Yes |
| -v | Verbose output | Yes |
| -p 25 | Port 25 (SMTP) | Yes |

## Examples

### Basic Usage

```bash
nc -lvp 25
```

### Advanced Usage

```bash
nc -lvp 25 -k  # Keep listening after connection
```

## Expected Output

Listening on [0.0.0.0] (family 0, port 25)
Connection from ec2-18-213-100-122.compute-1.amazonaws.com 12345 received!
HELO test.org
MAIL FROM: <>
RCPT TO: kontakt@deepsec.pl
DATA
Test.
.

## Related

- [[Related Procedure: Exploit-SSRF-for-SMTP-Injection]]
