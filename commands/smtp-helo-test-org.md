---
data: HELO test.org
tags:
  - smtp
type: command
output: 'SMTP server acknowledgment (e.g., 250 OK)'
executor: smtp
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:14.606Z'
id: a10f3805-c5eb-44f6-afbd-96fea9aed377
verified: false
validated: true
submitted: true
---
# smtp-helo-test-org

## Command

```smtp
HELO test.org
```

## Description

This SMTP command initiates a connection by greeting the server with a domain name, used in the Gopher payload to start the email session from the exploited server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| test.org | Domain used for greeting the SMTP server | Yes |

## Examples

### Basic Usage

```smtp
HELO test.org
```

### Advanced Usage

In a full session: Followed by MAIL FROM, etc.

## Expected Output

SMTP server responds with 250 domain.org Hello [IP], indicating acceptance.

## Related

- [[commands/smtp-mail-from-tester]]
- [[procedures/Create-PHP-Gopher-Redirector-for-SMTP-Commands]]
