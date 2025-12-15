---
tags:
  - graphql
  - access-control-bypass
  - proxy-intercept
type: procedure
tools:
  - '[[tools/HTTP-Proxy-Tool]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:35.702Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: a4ff29f3-db07-4cb8-a7fc-3d2d934ad43b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-and-Modify-Like-Request

## Summary

This procedure intercepts a legitimate Twitter like request using a proxy tool, modifies the tweet_id parameter to target a private Twitter Circle tweet, and resends it to exploit improper access controls on the FavoriteTweet GraphQL endpoint, allowing unauthorized liking.

## Description

In a Twitter Circle, posts are visible only to approved members, but the FavoriteTweet GraphQL mutation fails to validate Circle membership for like actions. An authenticated attacker can manipulate the request to like private tweets, succeeding with a 200 OK response. This is discovered by proxying normal traffic and altering parameters. The target environment is Twitter's web platform with an active authenticated session. Prerequisites include a Twitter account and knowledge of a target Circle tweet ID (e.g., from URL inspection).

## Requirements

1. Authenticated Twitter session
2. HTTP proxy tool installed and configured (e.g., Burp Suite with browser proxy settings)
3. Target private tweet ID
4. No membership in the target Twitter Circle

## Defense

Defensive measures and detection strategies:

- Implement server-side validation for Circle membership on all like/unlike mutations
- Rate-limit GraphQL requests and monitor for anomalous tweet_id patterns
- Log and alert on likes to private resources from non-members

## Objectives

1. Bypass access controls to like unauthorized private tweets
2. Confirm successful exploitation via API response
3. Prepare for data exfiltration in subsequent steps

## Instructions

### Step 1: Configure Proxy and Intercept Request

**Context**: Set up the proxy to capture HTTPS traffic from your Twitter session and trigger a like on a public tweet to obtain a baseline request.

No specific command; use the proxy tool's interface to turn on interception. Like a public tweet in the browser to capture the POST to https://twitter.com/i/api/graphql/.../FavoriteTweet.

> The intercepted request will be a JSON payload with variables: {"tweetId":"public_tweet_id","favorite":true}, along with authorization headers.

### Step 2: Modify and Forward Request

**Context**: Edit the tweet_id to a private Circle tweet and resend to test bypass.

No specific command; in the proxy tool, modify the JSON variables section to change "tweetId" to the target Circle tweet ID, then forward the request.

> Expected output: GraphQL response with "data" object containing success for the mutation, no errors for permissions.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/HTTP-Proxy-Tool]]

## Tags

- graphql
- access-control-bypass
- proxy-intercept
