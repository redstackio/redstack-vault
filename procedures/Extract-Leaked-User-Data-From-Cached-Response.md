---
id: proc-wcd-extract-data-001
tags:
  - data-extraction
  - information-disclosure
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-fetch-cached-wcd-page]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Local System]]'
updated_at: '2025-12-14T17:27:57.249Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Local System]]'
---
# Extract-Leaked-User-Data-From-Cached-Response

## Summary

This procedure parses the retrieved cached HTML response to extract sensitive victim data such as first/last name, username, email, profile picture URL, and CSRF token, enabling further attacks like account takeover or request forgery.

## Description

The cached 404 page embeds user info in HTML/JS (e.g., meta tags, JSON objects). Inspect source for patterns like <script> with user object or CSRF input fields. For Shopify, data appears in error page personalization. Outcomes: Usable PII and tokens. Prerequisites: Cached response obtained; text parsing skills.

## Requirements

1. Cached HTML response from prior retrieval
2. Text editor or grep/sed for parsing
3. Knowledge of target site's data embedding (e.g., Shopify's user JSON)

## Defense

Defensive measures and detection strategies:

- Strip sensitive data from error pages (e.g., no user info in 404s)
- Use Content-Security-Policy to limit script injection in errors
- Audit cached responses for PII leakage via proxy logs

## Objectives

1. Identify and pull out PII elements
2. Validate CSRF token usability
3. Document for chain exploitation

## Instructions

### Step 1: Inspect Response Source

**Context**: Review the full HTML for embedded user data.

Use the output from [[commands/curl-fetch-cached-wcd-page]] or open saved file.

> Search for strings like "user.email" or "csrf_token"; e.g., find {"first_name": "John", "email": "john@ex.com", "profile_picture": "url", "csrf_token": "xyz"}.

### Step 2: Extract Specific Fields

**Context**: Use tools to pull key values.

Run `grep -o 'email.*@.*' cached_page.html` or similar for targeted extraction.

> Expected: Isolated data points ready for use, confirming leak success.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Local System]] Data from Local System (adapted to web response parsing)

### Sub-Techniques


## Commands Used

- [[commands/curl-fetch-cached-wcd-page]]

## Tools Used

- [[tools/curl]]

## Tags

- pii-extraction
- token-leak
