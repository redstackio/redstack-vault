---
id: cmd-normal-vote-95555
data: >-
  curl -X POST
  "https://twitter.com/i/cards/api/v1.json?tweet_id=657629231309041664&card_name=poll2choice_text_only&forward=false&capi_uri=capi%3A%2F%2Fpassthrough%2F1"
  -H "Content-Type: application/json" -d
  '{"twitter:string:card_uri":"card://657629230759415808","twitter:long:original_tweet_id":"657629231309041664","twitter:string:selected_choice":"2"}'
tags:
  - csrf
  - twitter
  - api
type: command
output: HTTP 403 Forbidden (without token)
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:28.991Z'
verified: false
validated: true
submitted: true
---
# Normal Vote Submission to Twitter Cards API

## Command

```bash
curl -X POST "https://twitter.com/i/cards/api/v1.json?tweet_id=657629231309041664&card_name=poll2choice_text_only&forward=false&capi_uri=capi%3A%2F%2Fpassthrough%2F1" \
  -H "Content-Type: application/json" \
  -d '{"twitter:string:card_uri":"card://657629230759415808","twitter:long:original_tweet_id":"657629231309041664","twitter:string:selected_choice":"2"}'
```

## Description

This command simulates a standard poll vote submission to Twitter's protected cards API endpoint, which requires a CSRF token (_authenticity_token) for authentication. Use it to analyze the request format and confirm enforcement.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| tweet_id | ID of the tweet containing the poll (e.g., 657629231309041664) | Yes |
| card_name | Type of poll card (e.g., poll2choice_text_only) | Yes |
| forward | Flag to disable forwarding (false) | Yes |
| capi_uri | Encoded passthrough URI (capi://passthrough/1) | Yes |
| twitter:string:card_uri | URI of the poll card (e.g., card://657629230759415808) | Yes |
| twitter:long:original_tweet_id | Original tweet ID | Yes |
| twitter:string:selected_choice | Index of the selected poll option (e.g., 2) | Yes |

## Examples

### Basic Usage

```bash
curl -X POST "https://twitter.com/i/cards/api/v1.json?tweet_id=EXAMPLE_ID&card_name=poll2choice_text_only&forward=false&capi_uri=capi%3A%2F%2Fpassthrough%2F1" -H "Content-Type: application/json" -d '{"twitter:string:card_uri":"card://EXAMPLE","twitter:long:original_tweet_id":"EXAMPLE_ID","twitter:string:selected_choice":"1"}'
```

### Advanced Usage

Include cookies and _authenticity_token for successful vote:

```bash
curl -X POST "https://twitter.com/i/cards/api/v1.json?..." -H "Cookie: auth_token=..." -H "X-CSRF-Token: ..." ...
```

## Expected Output

Without token: HTTP 403 Forbidden. With token and session: HTTP 200 OK, vote recorded.

## Related

- [[commands/bypassed-vote-submission-without-json-extension]]
- [[procedures/Analyze-Normal-Vote-Request-to-Twitter-Cards-API]]
