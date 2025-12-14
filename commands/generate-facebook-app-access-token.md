---
data: >-
  curl
  "https://graph.facebook.com/oauth/access_token?client_id=660471650708388&client_secret=71a2d003a5ecfab4f4ad86dfb70b74e0&redirect_uri=&grant_type=client_credentials"
tags:
  - oauth
  - api
  - verification
type: command
output: >-
  {"access_token":"660471650708388|jboBZgqj64W1JXIAKIbtVz24FlQ","token_type":"bearer"}
executor: bash
platforms:
  - Windows
  - Linux
  - macOS
id: 30410bc4-6304-47ec-942a-830e0aba34d4
created_at: '2025-12-14T17:32:20.714Z'
updated_at: '2025-12-14T17:32:20.714Z'
verified: false
validated: true
submitted: true
---
# generate-facebook-app-access-token

## Command

```bash
curl "https://graph.facebook.com/oauth/access_token?client_id=660471650708388&client_secret=71a2d003a5ecfab4f4ad86dfb70b74e0&redirect_uri=&grant_type=client_credentials"
```

## Description

This command requests an app access token from the Facebook Graph API using the client credentials OAuth grant type, verifying hardcoded app credentials by generating a bearer token for further API interactions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| client_id | Facebook App ID (e.g., 660471650708388) | Yes |
| client_secret | Facebook App Secret (e.g., 71a2d003a5ecfab4f4ad86dfb70b74e0) | Yes |
| redirect_uri | Redirect URI (empty for client_credentials) | No |
| grant_type | OAuth grant type (client_credentials) | Yes |

## Examples

### Basic Usage

```bash
curl "https://graph.facebook.com/oauth/access_token?client_id=660471650708388&client_secret=71a2d003a5ecfab4f4ad86dfb70b74e0&redirect_uri=&grant_type=client_credentials"
```

### Advanced Usage

For scripting, pipe to jq for parsing:

```bash
curl "https://graph.facebook.com/oauth/access_token?client_id=660471650708388&client_secret=71a2d003a5ecfab4f4ad86dfb70b74e0&redirect_uri=&grant_type=client_credentials" | jq '.access_token'
```

## Expected Output

JSON object containing the access_token and token_type upon success, indicating valid credentials. Errors return HTTP 400 with details like invalid client.

## Related

- [[Related Procedure: Verify-Facebook-Credentials-with-Graph-API]]
