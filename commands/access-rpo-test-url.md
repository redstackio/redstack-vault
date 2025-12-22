---
id: 9845e8ae-0039-481e-8c50-f1bafc054f64
name: access-rpo-test-url
type: command
executor: bash
data: >-
  curl
  "http://challenge.hackvertor.co.uk/xss_horror_show/chapter7/rpo2.php/fakedirectory/fakedirectory2/fakedirectory3"
output: null
created_at: '2023-04-06T03:56:43.832948+00:00'
updated_at: '2023-04-06T03:56:43.857225+00:00'
platforms:
  - Web
tags:
  - rpo
  - traversal
verified: true
validated: true
---

# access-rpo-test-url

## Command

```bash
curl "http://challenge.hackvertor.co.uk/xss_horror_show/chapter7/rpo2.php/fakedirectory/fakedirectory2/fakedirectory3"
```

## Description

This command accesses a test URL demonstrating RPO via directory traversal, simulating access to sensitive paths outside the web root.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Target RPO test endpoint with traversal paths | Yes |

## Examples

### Basic Usage

```bash
curl "http://challenge.hackvertor.co.uk/xss_horror_show/chapter7/rpo2.php/fakedirectory/fakedirectory2/fakedirectory3"
```

## Expected Output

HTTP response indicating successful traversal, e.g., contents of traversed directory or error revealing path info.

## Related

- [[procedures/Exploit-RPO-for-Stored-XSS-via-CSS-Injection-in-IE]]
