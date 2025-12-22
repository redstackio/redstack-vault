---
id: d0d406b2-c7be-43e9-b60b-20bfbccd4f8d
name: curl-hockeyapp-api-app-info
type: command
executor: bash
data: >-
  curl -H "X-HockeyAppToken: $_API_TOKEN"
  https://rink.hockeyapp.net/api/2/apps/$_APP_ID
output: null
created_at: '2023-04-06T03:55:52.468230+00:00'
updated_at: '2023-04-06T03:55:52.477079+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - api
  - exploit
verified: true
validated: true
---

# curl-hockeyapp-api-app-info

## Command

```bash
curl -H "X-HockeyAppToken: $_API_TOKEN" https://rink.hockeyapp.net/api/2/apps/$_APP_ID
```

## Description

This command sends a GET request to the HockeyApp API to retrieve information about a specific app using a provided API token. It is used to test leaked tokens and access app metadata during exploitation of exposed credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_API_TOKEN | The leaked HockeyApp API token (32-character hex string) | Yes |
| $_APP_ID | The target app ID (GUID, e.g., 2021bdf2671ab09174c1de5ad147ea2ba4) | Yes |
| -H | HTTP header flag to set the authentication token | Built-in |

## Examples

### Basic Usage

```bash
curl -H "X-HockeyAppToken: ad136912c642076b0d1f32ba161f1846b2c" https://rink.hockeyapp.net/api/2/apps/2021bdf2671ab09174c1de5ad147ea2ba4
```

### Advanced Usage

Add verbose output and save to file:
```bash
curl -v -H "X-HockeyAppToken: $_API_TOKEN" https://rink.hockeyapp.net/api/2/apps/$_APP_ID -o app_info.json
```

## Expected Output

Successful response is JSON containing app details:
```json
{
  "app": {
    "id": "2021bdf2671ab09174c1de5ad147ea2ba4",
    "title": "Sample App",
    "platform": "iOS",
    "devices": 100,
    "crash_groups": 5
  }
}
```
Error responses include 401 (invalid token) or 404 (app not found).

## Related

- [[procedures/Exploit-Leaked-HockeyApp-API-Token]]
