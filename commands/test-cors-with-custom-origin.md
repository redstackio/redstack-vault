---
data: >-
  curl -X GET https://nordvpn.com/wp-json/ -H "Origin: http://iamsoevil.com/" -H
  "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101
  Firefox/71.0" -v
tags:
  - cors
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:12.108Z'
id: af5d304c-af79-4f04-8ff2-2b25fd8448c8
verified: false
validated: true
submitted: true
---
# test-cors-with-custom-origin

## Command

```bash
curl -X GET https://nordvpn.com/wp-json/ -H "Origin: http://iamsoevil.com/" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0" -v
```

## Description

This command tests CORS policy by sending a GET request with a custom Origin header to check if it's reflected insecurely in the response, indicating a misconfiguration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Origin: http://iamsoevil.com/"` | Custom attacker Origin header to test echoing | Yes |
| `-H "User-Agent: ..."` | Mimics browser User-Agent for realism | Yes |
| `-v` | Verbose output to inspect headers | Yes |

## Examples

### Basic Usage

```bash
curl -X GET https://nordvpn.com/wp-json/ -H "Origin: http://evil.com/" -v
```

### Advanced Usage

```bash
curl -X GET https://nordvpn.com/wp-json/ -H "Origin: http://iamsoevil.com/" -H "Accept: application/json" -v
```

## Expected Output

Verbose curl output showing HTTP/1.1 200 OK and response headers like < Access-Control-Allow-Origin: http://iamsoevil.com/ and < Access-Control-Allow-Credentials: true.

## Related

- [[Related Procedure: Test-CORS-Policy-with-Custom-Origin]]
