---
id: proc-decode-extract-2380084
tags:
  - information-disclosure
  - decoding
  - api-keys
type: procedure
tools:
  - '[[tools/beautifier-io]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/url-decode]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Local System]]'
updated_at: '2025-12-14T17:32:29.084Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Local System]]'
---
# Decode and Extract API Keys from JSON

## Summary

This procedure decodes URL-encoded JSON from archived web entries and extracts sensitive API keys, such as PayPal client_id, Stripe API key, and Sentry DSN, for disclosure analysis.

## Description

Archived JavaScript often embeds configurations as URL-encoded JSON in paths. Decoding reveals plain objects with secrets. In the Mozilla report, this exposed keys like PayPal's 'Adb5V3A0jC394H-2nZL9JRBzcre0bNjxm_tqzezZDTTSheL4ANKqvG79uyDw1lwtxuXbDPK7Kdp6pMbr'. Beautification aids readability. Outcomes include credential documentation and risk assessment.

## Requirements

1. Encoded JSON string from prior step
2. URL decoder tool or command-line utility
3. JSON beautifier for formatting

## Defense

Defensive measures and detection strategies:

- Rotate exposed keys immediately
- Use environment variables or server-side secrets management
- Exclude sensitive domains from web crawlers via robots.txt

## Objectives

1. Decode encoded configurations to plain text
2. Identify and document API keys and DSNs
3. Assess potential misuse risks

## Instructions

### Step 1: Decode URL-Encoded JSON

**Context**: Extract and decode the encoded portion of the archived URL.

**Command** ([[commands/url-decode]]):
```bash
echo 'ENCODED_JSON_HERE' | python3 -c "import urllib.parse; print(urllib.parse.unquote(input()))"
```

> Replace ENCODED_JSON_HERE with the actual string (e.g., from https://subscriptions.firefox.com/{encoded}). This Python one-liner decodes URL percent-encoding. Expected output: Plain JSON object.

### Step 2: Beautify and Extract Keys

**Context**: Format the decoded JSON and review for sensitive fields.

Paste the decoded JSON into [[tools/beautifier-io]] to format it. Manually extract sections like:
- PayPal: clientId = 'Adb5V3A0jC394H-2nZL9JRBzcre0bNjxm_tqzezZDTTSheL4ANKqvG79uyDw1lwtxuXbDPK7Kdp6pMbr'
- Stripe: apiKey = 'pk_live_HgtiWdwlc5Uq8ZRsPAXIAyRY00CA51o613'
- Sentry: DSN = 'https://bd67bbdfad9b46a7a2f0faf4aa02c122@o1069899.ingest.sentry.io/6231072'

**Expected Output**: Readable JSON with highlighted configurations.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Local System]] Data from Local System

### Sub-Techniques

-

## Commands Used

- [[commands/url-decode]]

## Tools Used

- [[tools/beautifier-io]]

## Tags

- [[information-disclosure]]
- [[decoding]]
- [[api-keys]]
