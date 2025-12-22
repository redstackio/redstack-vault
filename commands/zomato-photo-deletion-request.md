---
id: cmd-404797-photo-deletion
data: >-
  GET
  /php/client_manage_handler?res_id=REDACTED&photo_ids%5B%5D=r_YxNDUOTE4MTYzO&removable=1&case=remove-active-photo
  HTTP/1.1

  Host: www.zomato.com

  User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101
  Firefox/61.0

  Accept: */*

  Accept-Language: en-US,en;q=0.5

  Accept-Encoding: gzip, deflate

  Referer: https://www.zomato.com/

  X-Requested-With: XMLHttpRequest

  Cookie: REDACTED

  Connection: close
tags:
  - deletion
  - capture
type: command
output: '{"status":"success"}'
executor: http
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:34.448Z'
verified: false
validated: true
submitted: true
---
# Zomato Photo Deletion Request

## Command

```http
GET /php/client_manage_handler?res_id=REDACTED&photo_ids%5B%5D=r_YxNDUOTE4MTYzO&removable=1&case=remove-active-photo HTTP/1.1
Host: www.zomato.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.zomato.com/
X-Requested-With: XMLHttpRequest
Cookie: REDACTED
Connection: close
```

## Description

This HTTP GET request initiates photo deletion in Zomato's restaurant manager endpoint, used to capture and extract photo_ids for IDOR testing. Execute via proxy like Burp to intercept during UI-initiated deletion.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| res_id | Restaurant ID for authentication context | Yes |
| photo_ids[] | Array of photo IDs to delete (r_-prefixed) | Yes |
| removable | Flag to indicate removable photos (1) | Yes |
| case | Action type (remove-active-photo) | Yes |

## Examples

### Basic Usage

```http
GET /php/client_manage_handler?res_id=12345&photo_ids%5B%5D=r_ABC123&removable=1&case=remove-active-photo HTTP/1.1
Host: www.zomato.com
...
```

### Advanced Usage

Include multiple photo_ids for batch deletion:

```http
GET /php/client_manage_handler?res_id=12345&photo_ids%5B%5D=r_ABC123&photo_ids%5B%5D=r_DEF456&removable=1&case=remove-active-photo HTTP/1.1
Host: www.zomato.com
...
```

## Expected Output

JSON response {"status":"success"} on successful deletion, or error if invalid.

## Related

- [[commands/zomato-modified-photo-deletion-idor]]
