---
data: >-
  curl -X GET "https://api.omise.co/payments/paym_test_xxxx/status" -H
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
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:33.730Z'
id: c9a95c14-3900-471a-aeb3-09a910316699
verified: false
validated: true
submitted: true
---
# omise-retrieve-own-payment-status

## Command

```bash
curl -X GET "https://api.omise.co/payments/paym_test_xxxx/status" \
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

This command retrieves the payment status for the authenticated user's own payment ID using a GET request to the Omise API, establishing a baseline for IDOR exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| payment_id (path) | The payment identifier (e.g., paym_test_xxxx) | Yes |
| Headers | Browser-like headers to mimic legitimate requests | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://api.omise.co/payments/paym_test_xxxx/status" -H "Accept: */*" -H "User-Agent: Mozilla/5.0 ..."
```

### Advanced Usage

Include full headers as shown for stealthy requests.

## Expected Output

HTTP/2 200 OK with JSON response such as {"processed":true}, indicating successful retrieval of payment status.

## Related

- [[commands/omise-retrieve-unauthorized-payment-status]]
- [[procedures/Exploit-IDOR-in-Omise-Payment-Status-API]]
