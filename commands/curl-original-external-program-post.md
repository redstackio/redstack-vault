---
id: cmd-curl-original-post
data: >-
  curl -X POST https://hackerone.com/external_programs -H "X-CSRF-Token:
  QPxj69iMMHCtU+KrbEgKN4V2FvpgMfLSNdxMqAHlGiYc67nzsqEof33U+7Ot4b0tlyER++xPuvlP8SsyzvHg8Q=="
  -H "Cookie: __Host-session=..." -F
  "authenticity_token=QPxj69iMMHCtU+KrbEgKN4V2FvpgMfLSNdxMqAHlGiYc67nzsqEof33U+7Ot4b0tlyER++xPuvlP8SsyzvHg8Q=="
  -F "name=test" -F "handle=edmodotest" -F "about=" -F "website=edmodo.com" -F
  "twitter_handle=" -F "policy=Exclusions\\n\\nWhile researching, we'd like to
  ask you to refrain from:\\n\\n Denial of service\\n Spamming\\n Social
  engineering (including phishing) of edmodo staff or contractors\\n Any
  physical attempts against edmodo property or data centers\\n" -F "policy_url="
  -F "scopes[]=" -F "scopes[]=" -F "offers_rewards=true" -F "thanks_url=" -F
  "disclosure_url=" -F "disclosure_method=email" -F
  "disclosure_email=policy@edmodo.com" -F "profile_picture=@/dev/null" -F
  "_ignore="
tags:
  - http
  - post
  - csrf
type: command
output: HTTP/1.1 200 OK ... (successful creation response)
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:35.816Z'
verified: false
validated: true
submitted: true
---
# curl-original-external-program-post

## Command

```bash
curl -X POST https://hackerone.com/external_programs \
  -H "X-CSRF-Token: QPxj69iMMHCtU+KrbEgKN4V2FvpgMfLSNdxMqAHlGiYc67nzsqEof33U+7Ot4b0tlyER++xPuvlP8SsyzvHg8Q==" \
  -H "Cookie: __Host-session=..." \
  -F "authenticity_token=QPxj69iMMHCtU+KrbEgKN4V2FvpgMfLSNdxMqAHlGiYc67nzsqEof33U+7Ot4b0tlyER++xPuvlP8SsyzvHg8Q==" \
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

Sends the original HTTP POST request to create an external program on HackerOne, including both CSRF tokens, to capture the legitimate flow.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-H "X-CSRF-Token: ..."` | Header CSRF token | Yes |
| `-H "Cookie: ..."` | Session cookie | Yes |
| `-F "authenticity_token=..."` | Form CSRF token | Yes (for original) |
| `-F "name=test"` | Program name | Yes |
| `-F "handle=edmodotest"` | Unique handle | Yes |
| `-F "policy=..."` | Policy text | Yes |
| Other `-F` fields | Additional form data | Conditional |

## Examples

### Basic Usage

```bash
curl -X POST https://hackerone.com/external_programs -H "Cookie: ..." -F "name=test" ...
```

### Advanced Usage

Include full policy and empty fields as shown.

## Expected Output

HTTP 200 OK with JSON {"handle":"edmodotest"} or similar success response.

## Related

- [[commands/curl-modified-external-program-post]]
