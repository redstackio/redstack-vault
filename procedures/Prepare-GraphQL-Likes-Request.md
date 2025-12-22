---
id: proc-2140960-001
tags:
  - graphql
  - api-prep
  - request-copy
type: procedure
tools:
  - '[[tools/HTTP-Proxy]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:35.356Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Prepare-GraphQL-Likes-Request

## Summary

This procedure involves capturing or copying the raw HTTP GET request to the X GraphQL API endpoint for likes, setting up the foundation for modifying and exploiting it to access hidden data.

## Description

In the context of testing the X (Twitter) GraphQL API, this step prepares the request structure used to query user likes. The endpoint /i/api/graphql/lVf2NuhLoYVrpN4nO7uw0Q/Likes requires authentication and includes URL-encoded variables for userId, count, and features. This bypasses UI restrictions when modified, exposing hidden likes of Premium users. Prerequisites include an active X session.

## Requirements

1. Authenticated X session with valid cookies and CSRF token
2. Access to browser developer tools or a proxy for request capture
3. Knowledge of the target endpoint and variable format

## Defense

Defensive measures and detection strategies:

- Implement API-level privacy enforcement matching UI controls
- Monitor GraphQL queries for anomalous userId patterns from non-owner accounts
- Rate-limit like queries per authenticated user

## Objectives

1. Obtain a templated HTTP request for GraphQL likes query
2. Verify authentication headers are intact
3. Prepare for target-specific modifications

## Instructions

### Step 1: Capture or Copy Raw Request

**Context**: Use browser tools or a proxy to obtain the GET request while logged into X and navigating to a likes-related page.

No specific command; manually copy the request details:

- Endpoint: GET /i/api/graphql/lVf2NuhLoYVrpN4nO7uw0Q/Likes
- Variables: %7B%22userId%22%3A%22placeholder_id%22%2C%22count%22%3A20%2C%22includePromotedContent%22%3Atrue%2C%22withClientEventToken%22%3Atrue%2C%22withBirdwatchNotes%22%3Afalse%2C%22withVoice%22%3Atrue%2C%22withV2Timeline%22%3Atrue%7D (URL-encoded)
- Features: %7B%22rweb_tipjar_consumption_enabled%22%3Atrue%2C%22responsive_web_graphql_exclude_directive_enabled%22%3Atrue%2C%22verified_phone_label_enabled%22%3Afalse%2C%22creator_subscriptions_tweet_preview_api_enabled%22%3Atrue%2C%22responsive_web_graphql_timeline_navigation_enabled%22%3Atrue%2C%22responsive_web_graphql_skip_user_profile_image_extensions_enabled%22%3Afalse%2C%22subscriptions_verification_info_verified_since_abbr_enabled%22%3Atrue%2C%22highlights_tweets_tab_ui_enabled%22%3Atrue%2C%22responsive_web_edit_tweet_api_enabled%22%3Atrue%2C%22graphql_is_translatable_rweb_tweet_is_translatable_enabled%22%3Atrue%2C%22view_counts_everywhere_api_enabled%22%3Atrue%2C%22longform_notetweets_consumption_enabled%22%3Atrue%2C%22responsive_web_media_download_video_enabled%22%3Afalse%2C%22responsive_web_enhance_cards_enabled%22%3Afalse%2C%22hiddenLikesEnabled%22%3Atrue%7D
- Headers: Host: twitter.com, Cookie: (your session), User-Agent: Mozilla/5.0..., Authorization: Bearer ..., X-Twitter-Auth-Type: OAuth2Session, X-Csrf-Token: ...

> This captures the full request template. Expected output is the raw HTTP format ready for pasting into a proxy.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/HTTP-Proxy]]

## Tags

- [[graphql]]
- [[api-prep]]
