---
id: a161c9e0-cf3f-44b5-bee9-0ec1eebb0fad
name: curl-twitter-account-activity-subscription-count
type: command
executor: bash
data: >-
  curl --request GET --url
  https://api.twitter.com/1.1/account_activity/all/subscriptions/count.json
  --header 'authorization: Bearer $_BEARER_TOKEN'
output: null
created_at: '2023-04-06T03:55:53.250188+00:00'
updated_at: '2023-04-06T03:55:53.258813+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - api
  - twitter
  - credential-access
verified: true
validated: true
---

# curl-twitter-account-activity-subscription-count

## Command

```bash
curl --request GET --url https://api.twitter.com/1.1/account_activity/all/subscriptions/count.json --header 'authorization: Bearer $_BEARER_TOKEN'
```

## Description

This command queries the Twitter API v1.1 endpoint for the count of account activity subscriptions using a Bearer Token for authentication. It is used to validate a leaked token and retrieve basic account metadata in exploitation scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_BEARER_TOKEN | The leaked Twitter Bearer Token for API authentication | Yes |
| --request GET | Specifies the HTTP method as GET | Yes |
| --url https://api.twitter.com/1.1/account_activity/all/subscriptions/count.json | The API endpoint URL for subscription count | Yes |
| --header 'authorization: Bearer $_BEARER_TOKEN' | Authorization header with the Bearer Token | Yes |

## Examples

### Basic Usage

```bash
curl --request GET --url https://api.twitter.com/1.1/account_activity/all/subscriptions/count.json --header 'authorization: Bearer AAAAAAAAAAAAAAAAAAAAAA...'
```

### Advanced Usage

Pipe to jq for formatted output:
```bash
curl --request GET --url https://api.twitter.com/1.1/account_activity/all/subscriptions/count.json --header 'authorization: Bearer $_BEARER_TOKEN' | jq '.'
```

## Expected Output

Successful response:
```json
{"count": 5}
```

Error response (invalid token):
```json
{"errors":[{"code":89,"message":"Invalid or expired token."}]}
```

A successful output indicates valid token access; errors suggest token invalidation or insufficient permissions.

## Related

- [[procedures/Exploit-Leaked-Twitter-Bearer-Token-for-API-Access]]
