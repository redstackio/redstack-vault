---
data: >-
  curl -X POST "https://www.semrush.com/projects/api/projects/?key=█████████" -H
  "Host: www.semrush.com" -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64;
  x64; rv:58.0) Gecko/20100101 Firefox/58.0" -H "Accept: application/json,
  text/javascript, */*; q=0.01" -H "Accept-Language: en-US,en;q=0.5" -H
  "Accept-Encoding: gzip, deflate, br" -H "Referer:
  https://www.semrush.com/projects/?1519503450" -H "Content-Type:
  application/json" -H "X-Requested-With: XMLHttpRequest" -H "Content-Length:
  104" -H "Cookie: cfduid=d586fa9b6fb028d425a8df52599e73d021519503413;
  PHPSESSID=██████; ref_code= default_; usertype=Free-User;
  marketing=%7B%22user_cmp%22%3A%22%22%2C%22user_label%22%3A%22%22%7D;
  localization=%7B%22locale%22%3A%22en%22%7D; db=us;
  n_userid=LuWkzFqRyDaG+2bqBEeyAg==; semrush_counter_cookie=deleted;
  visit_first=1519503421910;
  userdata=%7B%22tz%22%3A%22GMT+5.5%22%2C%22ol%22%3A%22en%22%7D;
  utz=Asia%2FKolkata;
  wp13557=UWYYADDDDDDIKXCIMMK-JBZZ-XLLX-BYCY-ILTWWCUBMTICDMUMLJIZI-AZAL-XLML-CJHX-WTBKZBVKZXWVDlLtkNlo_Jht;
  uvts=7B3Au3azsgVbSB6R;
  org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=en" -H "DNT:
  1" -H "Connection: keep-alive" -d
  '{"domain":"Walterwhite12.com","name":"Walterwhite12.com","url":"Walterwhite12.com","acl":{"write":true}}'
tags:
  - replay
  - api
type: command
output: HTTP 200 with JSON project details
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:11.261Z'
id: 304f0f9a-c6e5-4f10-84cd-da32ab9fd719
verified: false
validated: true
submitted: true
---
# replay-semrush-request-post-logout

## Command

```bash
curl -X POST "https://www.semrush.com/projects/api/projects/?key=█████████" -H "Host: www.semrush.com" -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0" -H "Accept: application/json, text/javascript, */*; q=0.01" -H "Accept-Language: en-US,en;q=0.5" -H "Accept-Encoding: gzip, deflate, br" -H "Referer: https://www.semrush.com/projects/?1519503450" -H "Content-Type: application/json" -H "X-Requested-With: XMLHttpRequest" -H "Content-Length: 104" -H "Cookie: cfduid=d586fa9b6fb028d425a8df52599e73d021519503413; PHPSESSID=██████; ref_code= default_; usertype=Free-User; marketing=%7B%22user_cmp%22%3A%22%22%2C%22user_label%22%3A%22%22%7D; localization=%7B%22locale%22%3A%22en%22%7D; db=us; n_userid=LuWkzFqRyDaG+2bqBEeyAg==; semrush_counter_cookie=deleted; visit_first=1519503421910; userdata=%7B%22tz%22%3A%22GMT+5.5%22%2C%22ol%22%3A%22en%22%7D; utz=Asia%2FKolkata; wp13557=UWYYADDDDDDIKXCIMMK-JBZZ-XLLX-BYCY-ILTWWCUBMTICDMUMLJIZI-AZAL-XLML-CJHX-WTBKZBVKZXWVDlLtkNlo_Jht; uvts=7B3Au3azsgVbSB6R; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=en" -H "DNT: 1" -H "Connection: keep-alive" -d '{"domain":"Walterwhite12.com","name":"Walterwhite12.com","url":"Walterwhite12.com","acl":{"write":true}}'
```

## Description

Replays a Semrush project creation request after logout to test session-independent authentication via API key.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `key` | API key (same as capture) | Yes |
| `domain` | New domain in JSON | Yes |
| `name` | New name in JSON | Yes |
| `url` | New URL in JSON | Yes |
| Cookie headers | Stale session cookies | Optional (ignored by server) |

## Examples

### Basic Usage

```bash
curl -X POST "https://www.semrush.com/projects/api/projects/?key=█████████" -H "Content-Type: application/json" -d '{"domain":"test.com","name":"test","url":"test.com","acl":{"write":true}}'
```

## Expected Output

HTTP/1.1 200 OK {"id":1266025,"domain":"walterwhite12.com","name":"Walterwhite12.com","email":"saidutt.mekala@gmail.com",...}

## Related

- [[commands/capture-semrush-project-creation]]
- [[procedures/Replay-Request-Post-Logout-for-Same-User]]
