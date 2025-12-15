---
data: >-
  curl -X POST "https://www.semrush.com/projects/api/projects/?key=█████████" -H
  "Host: www.semrush.com" -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64;
  x64; rv:58.0) Gecko/20100101 Firefox/58.0" -H "Accept: application/json,
  text/javascript, */*; q=0.01" -H "Accept-Language: en-US,en;q=0.5" -H
  "Accept-Encoding: gzip, deflate, br" -H "Referer:
  https://www.semrush.com/projects/?1519503450" -H "Content-Type:
  application/json" -H "X-Requested-With: XMLHttpRequest" -H "Content-Length:
  86" -H "Cookie: cfduid=d586fa9b6fb028d425a8df52599e73d021519503413;
  PHPSESSID=██████████; ref_code= default_; usertype=Free-User;
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
  '{"domain":"BB1236.com","name":"BB12367.com","url":"BB123678.com","acl":{"write":true}}'
tags:
  - api
  - http-post
type: command
output: HTTP 200 with JSON project details
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:11.264Z'
id: f34e5043-1e82-4770-b1b3-3e0dfda32997
verified: false
validated: true
submitted: true
---
# capture-semrush-project-creation

## Command

```bash
curl -X POST "https://www.semrush.com/projects/api/projects/?key=█████████" -H "Host: www.semrush.com" -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0" -H "Accept: application/json, text/javascript, */*; q=0.01" -H "Accept-Language: en-US,en;q=0.5" -H "Accept-Encoding: gzip, deflate, br" -H "Referer: https://www.semrush.com/projects/?1519503450" -H "Content-Type: application/json" -H "X-Requested-With: XMLHttpRequest" -H "Content-Length: 86" -H "Cookie: cfduid=d586fa9b6fb028d425a8df52599e73d021519503413; PHPSESSID=██████████; ref_code= default_; usertype=Free-User; marketing=%7B%22user_cmp%22%3A%22%22%2C%22user_label%22%3A%22%22%7D; localization=%7B%22locale%22%3A%22en%22%7D; db=us; n_userid=LuWkzFqRyDaG+2bqBEeyAg==; semrush_counter_cookie=deleted; visit_first=1519503421910; userdata=%7B%22tz%22%3A%22GMT+5.5%22%2C%22ol%22%3A%22en%22%7D; utz=Asia%2FKolkata; wp13557=UWYYADDDDDDIKXCIMMK-JBZZ-XLLX-BYCY-ILTWWCUBMTICDMUMLJIZI-AZAL-XLML-CJHX-WTBKZBVKZXWVDlLtkNlo_Jht; uvts=7B3Au3azsgVbSB6R; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=en" -H "DNT: 1" -H "Connection: keep-alive" -d '{"domain":"BB1236.com","name":"BB12367.com","url":"BB123678.com","acl":{"write":true}}'
```

## Description

Sends a POST request to create a project in Semrush API during an active session, capturing the structure for replay. Use when documenting legitimate API behavior for authentication testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `key` | API key in query string | Yes |
| `domain` | Project domain in JSON | Yes |
| `name` | Project name in JSON | Yes |
| `url` | Project URL in JSON | Yes |
| `acl.write` | Write access flag in JSON | Yes |
| Cookie headers | Session cookies | Yes (for initial capture) |

## Examples

### Basic Usage

```bash
curl -X POST "https://www.semrush.com/projects/api/projects/?key=█████████" -H "Content-Type: application/json" -H "Cookie: ..." -d '{"domain":"example.com","name":"test","url":"test.com","acl":{"write":true}}'
```

### Advanced Usage

Include full headers as captured for authenticity.

## Expected Output

HTTP/1.1 200 OK with JSON body like {"id":12345,"domain":"bb1236.com","name":"BB12367.com","email":"saidutt.mekala@gmail.com",...}

## Related

- [[commands/replay-semrush-request-post-logout]]
- [[procedures/Setup-Test-Users-and-Capture-Initial-Request]]
