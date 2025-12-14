---
id: cmd-404797-photo-viewer
data: >-
  POST /php/photoviewerData.php HTTP/1.1

  Host: www.zomato.com

  User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101
  Firefox/61.0

  Accept: */*

  Accept-Language: en-US,en;q=0.5

  Accept-Encoding: gzip, deflate

  Referer: https://www.zomato.com/

  Content-Type: application/x-www-form-urlencoded; charset=UTF-8

  X-Requested-With: XMLHttpRequest

  Content-Length: 384

  Cookie: REDACTED

  Connection: close

  X-Forwarded-For: 127.0.0.1


  photoviewersize=NORMAL&photo_id=u_1MDU1NjE2NzE5M&type=res&index=1&category=all&res_id=16872578&group_id=false&onPage=true&moreToFetch%5B%5D=0&moreToFetch%5B%5D=1&moreToFetch%5B%5D=2&moreToFetch%5B%5D=3&moreToFetch%5B%5D=4&moreToFetch%5B%5D=5&moreToFetch%5B%5D=6&moreToFetch%5B%5D=7&moreToFetch%5B%5D=8&moreToFetch%5B%5D=9&moreToFetch%5B%5D=10&moreToFetch%5B%5D=11&moreToFetch%5B%5D=12
tags:
  - recon
  - extraction
type: command
output: JSON with photo details and IDs
executor: http
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:34.432Z'
verified: false
validated: true
submitted: true
---
# Zomato Photo Viewer Data Request

## Command

```http
POST /php/photoviewerData.php HTTP/1.1
Host: www.zomato.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.zomato.com/
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 384
Cookie: REDACTED
Connection: close
X-Forwarded-For: 127.0.0.1

photoviewersize=NORMAL&photo_id=u_1MDU1NjE2NzE5M&type=res&index=1&category=all&res_id=16872578&group_id=false&onPage=true&moreToFetch%5B%5D=0&moreToFetch%5B%5D=1&moreToFetch%5B%5D=2&moreToFetch%5B%5D=3&moreToFetch%5B%5D=4&moreToFetch%5B%5D=5&moreToFetch%5B%5D=6&moreToFetch%5B%5D=7&moreToFetch%5B%5D=8&moreToFetch%5B%5D=9&moreToFetch%5B%5D=10&moreToFetch%5B%5D=11&moreToFetch%5B%5D=12
```

## Description

This HTTP POST request fetches photo data from a public restaurant page, leaking photo_ids for IDOR targeting. Intercept during 'All photos' interaction to extract IDs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| photoviewersize | View size (NORMAL) | Yes |
| photo_id | Initial photo ID (u_-prefixed) | Yes |
| type | res for restaurant photos | Yes |
| category | all to load all categories | Yes |
| res_id | Target restaurant ID | Yes |
| moreToFetch[] | Array of indices (0-12) for pagination | Yes |

## Examples

### Basic Usage

```http
POST /php/photoviewerData.php HTTP/1.1
Host: www.zomato.com
...

photoviewersize=NORMAL&photo_id=u_EXAMPLE&type=res&category=all&res_id=12345&...
```

### Advanced Usage

For more photos, extend moreToFetch[]:

```http
POST /php/photoviewerData.php HTTP/1.1
Host: www.zomato.com
...

photoviewersize=NORMAL&photo_id=u_EXAMPLE&type=res&category=all&res_id=12345&moreToFetch%5B%5D=0&moreToFetch%5B%5D=13&...
```

## Expected Output

JSON array with photo objects containing IDs and details for extraction.

## Related

- [[commands/zomato-photo-deletion-request]]
