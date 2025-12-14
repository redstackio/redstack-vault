---
tags:
  - dos-trigger
  - graphql-exception
  - post-completion
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:25:59.797Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: b89da9a4-1232-497c-b8f0-d34ea7913838
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Forward-Request-and-Post-to-Trigger-DoS

## Summary

This procedure releases the modified request, completes the post, and verifies the DoS impact through unhandled 'None' type in GraphQL responses, causing frontend crashes.

## Description

After modification, forwarding the request results in a 201 Created response, storing the invalid image URL as 'None'. Posting propagates this to viewers, where NodeJS frontend fails to handle the null type during rendering, leading to exceptions and page DoS. Persistent across sessions; affects followers and subreddit viewers. Requires completion of prior steps; outcome is widespread disruption without further interaction.

## Requirements

1. Modified request ready in Burp Suite
2. Second browser or incognito session for verification
3. Attacker's Reddit account to post from
4. Target accounts (e.g., followers) to test impact

## Defense

Defensive measures and detection strategies:

- Handle null/None values gracefully in GraphQL resolvers with type guards
- Add error boundaries in NodeJS frontend to catch and log type exceptions
- Monitor for high error rates in GraphQL logs correlated with recent uploads

## Objectives

1. Successfully upload and store the corrupted image
2. Publish the post to expose the vulnerability
3. Confirm DoS on affected pages via exceptions

## Instructions

### Step 1: Forward Modified Request

**Context**: Send the altered upload to the server.

No command; Burp UI:

- Click 'Forward' in Burp's Intercept tab.
- Observe response in Proxy > HTTP history.

> Expected: 201 Created with JSON indicating upload success, but no valid URL.

### Step 2: Complete and Post

**Context**: Finalize the media post.

No command; Reddit UI:

- Return to the post editor (request should auto-complete).
- Click 'Post' to publish.

> Expected: Post appears in profile/subreddit with 'processing image...' status.

### Step 3: Verify DoS Impact

**Context**: Test from another account to confirm crash.

No command; view in browser:

- Log in as a follower or visit the post URL.
- Observe homepage/profile load failure.

> Expected: Infinite loading, console errors like 'TypeError: Cannot read property of None', blank pages.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- dos-trigger
- graphql-exception
- post-completion
