---
id: proc-capture-oauth-code
tags:
  - exfiltration
  - analytics
  - code-theft
type: procedure
tools:
  - '[[tools/Google-Analytics]]'
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Application Access Token]]'
  - '[[Network Sniffing]]'
updated_at: '2025-12-14T17:30:58.418Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Steal Application Access Token]]'
  - '[[Network Sniffing]]'
---
# Capture Leaked OAuth Code via Google Analytics

## Summary

This procedure uses Google Analytics on the attacker-controlled Booth.pm page to monitor and capture the OAuth authorization code leaked in the query string after victim redirection.

## Description

Post-victim authentication, the path traversal causes a redirect to the product page (e.g., https://booth.pm/ja/items/4503924?code=leaked_auth_code), where the unused code is exposed in the URL. Google Analytics tracks this query string in real-time reports, allowing the attacker to extract the code for token exchange and account takeover. This is passive and requires no custom server setup. Prerequisites: Analytics configured on the page and victim interaction.

## Requirements

1. Google Analytics tracking ID active on the product page
2. Access to Google Analytics dashboard
3. Recent victim redirect (within real-time window)

## Defense

Defensive measures and detection strategies:

- Avoid exposing sensitive tokens in query strings; use POST or fragments
- Audit third-party analytics for query parameter logging
- Detect anomalous traffic to product pages from OAuth domains

## Objectives

1. Intercept the leaked authorization code
2. Enable further exploitation like token exchange
3. Achieve credential access without direct interception

## Instructions

### Step 1: Access Real-Time Reports

**Context**: Navigate to Google Analytics to view live traffic.

Log in to Google Analytics dashboard:

- Select the property linked to Booth.pm.
- Go to Reports > Realtime > Overview.

> This shows active users and page details in near real-time.

### Step 2: Filter for Query Parameters

**Context**: Identify incoming requests with OAuth codes.

In Realtime:

- Look for events from booth.pm/ja/items/[id] with query strings.
- Check Event details or Custom Dimensions for URL parameters (code=...).

> The code appears as part of the full URL tracked by analytics.

### Step 3: Extract and Validate Code

**Context**: Copy the code for use in token requests.

No command; manually note the code value:

- Verify format (typically a long alphanumeric string).
- Use it promptly as codes expire (e.g., 10 minutes).

> Exchange via Pixiv token endpoint: POST /v2/auth/token with code for access/refresh tokens.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Steal Application Access Token]] Steal Application Access Token
- [[Network Sniffing]] Network Sniffing (adapted for analytics tracking)

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Google-Analytics]]

## Tags

- [[Exfiltration]]
- [[analytics]]
- [[code-theft]]
