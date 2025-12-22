---
data: >-
  curl -X POST https://public-api.periscope.tv/v1/oauth/token -d
  "client_id=█████████" -d "client_secret=█████████" -d "code=abcde" -d
  "grant_type=authorization_code" -d
  "redirect_uri=https://getmevo.com/oauth/periscope"
tags:
  - oauth
  - curl
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:35.115Z'
id: a9b7dc6c-b7b0-4404-97a1-b06145dce13a
verified: false
validated: true
submitted: true
---
# curl-exchange-oauth-code

## Command

```bash
curl -X POST https://public-api.periscope.tv/v1/oauth/token -d "client_id=█████████" -d "client_secret=█████████" -d "code=abcde" -d "grant_type=authorization_code" -d "redirect_uri=https://getmevo.com/oauth/periscope"
```

## Description

Exchanges an OAuth authorization code for an access token in Periscope API. Used after CSRF to obtain persistent access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method | Yes |
| `-d "client_id=..."` | App client ID | Yes |
| `-d "client_secret=..."` | App secret | Yes |
| `-d "code=..."` | Authorization code | Yes |
| `-d "grant_type=..."` | Grant type | Yes |
| `-d "redirect_uri=..."` | Registered redirect | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://public-api.periscope.tv/v1/oauth/token -d "client_id=█████████" -d "client_secret=█████████" -d "code=abcde" -d "grant_type=authorization_code" -d "redirect_uri=https://getmevo.com/oauth/periscope"
```

### Advanced Usage

Add verbose: ```bash
curl -v -X POST ... (same params)
```

## Expected Output

JSON: {"access_token": "eyJ...", "token_type": "bearer", "expires_in": 3600}

## Related

- [[Related Procedure: Exchange-Authorization-Code-for-Access-Token]]
