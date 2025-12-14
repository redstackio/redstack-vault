---
id: cmd-uuid-1
data: >-
  curl --user "██████:███" --data 'grant_type=client_credentials'
  'https://api.twitter.com/oauth2/token'
tags:
  - oauth
  - api-auth
  - twitter
type: command
output: '{"token_type":"bearer","access_token":"████"}'
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:32:10.550Z'
verified: false
validated: true
submitted: true
---
# twitter-oauth2-client-credentials-grant

## Command

```bash
curl --user "██████:███" --data 'grant_type=client_credentials' 'https://api.twitter.com/oauth2/token'
```

## Description

This command requests an OAuth2 bearer token from Twitter's API using the client credentials grant type, authenticating with a consumer key and secret via basic auth. It is used to demonstrate exploitation of leaked app credentials for application-only API access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--user` | Basic auth string in format "consumer_key:consumer_secret" (redacted here) | Yes |
| `--data` | POST body specifying 'grant_type=client_credentials' for app-only auth | Yes |
| URL | Twitter OAuth2 token endpoint: https://api.twitter.com/oauth2/token | Yes |

## Examples

### Basic Usage

```bash
curl --user "key:secret" --data 'grant_type=client_credentials' 'https://api.twitter.com/oauth2/token'
```

### Advanced Usage

Add silent output or JSON parsing:

```bash
curl -s --user "key:secret" --data 'grant_type=client_credentials' 'https://api.twitter.com/oauth2/token' | jq '.access_token'
```

## Expected Output

JSON response indicating success: `{"token_type":"bearer","access_token":"a_long_token_string"}`. Errors include 401 Unauthorized if credentials are invalid.

## Related

- [[Related Procedure: Authenticate-to-Twitter-API-with-Stolen-Credentials]]
