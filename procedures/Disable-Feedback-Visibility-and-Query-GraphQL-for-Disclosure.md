---
id: proc-001
tags:
  - information-disclosure
  - graphql
  - privacy-bypass
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
  - '[[tools/Incognito-Mode-Browser]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/graphql-user-profile-query]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:13.176Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Disable-Feedback-Visibility-and-Query-GraphQL-for-Disclosure

## Summary

This procedure exploits a misconfiguration in HackerOne's feedback privacy settings by disabling visibility in user preferences and then querying a GraphQL endpoint unauthenticated to disclose hidden feedback details, such as comments from specific programs like Legal Robot.

## Description

In HackerOne's system, users can control feedback visibility via settings, but the GraphQL backend for public profiles does not respect this setting, leading to information disclosure. The attack involves modifying settings to hide feedback, accessing the profile anonymously to capture the query, and replaying it to retrieve private data. This reveals user interactions intended to be private, potentially exposing sensitive comments. Prerequisites include a HackerOne account and browser access; the target is the web platform using GraphQL over HTTPS.

## Requirements

1. Valid HackerOne account with feedback to hide
2. Modern web browser with developer tools
3. Internet access to hackerone.com

## Defense

Defensive measures and detection strategies:

- Implement server-side checks in GraphQL resolvers to filter based on user privacy settings
- Monitor unauthenticated GraphQL queries for anomalous patterns, such as repeated UserProfilePage requests
- Rate-limit public API endpoints to prevent abuse

## Objectives

1. Bypass privacy controls to access hidden user feedback
2. Demonstrate impact of misconfigured API responses
3. Collect evidence of disclosed sensitive interactions

## Instructions

### Step 1: Configure Privacy Settings

**Context**: Hide the target feedback to test disclosure.

Log in to HackerOne and navigate to settings.

No specific command; use the web interface at https://hackerone.com/settings/feedback. Uncheck 'Show this blurb on my profile' for the feedback from 'Legal Robot'.

> This ensures the feedback is marked private on the frontend.

### Step 2: Capture GraphQL Request Unauthenticated

**Context**: Load the profile anonymously to identify the endpoint.

Use [[tools/Incognito-Mode-Browser]] to visit https://hackerone.com/brdoors3?type=user.

Open [[tools/Browser-Developer-Tools]], filter network for 'feedback', and capture the POST /graphql request with operationName 'UserProfilePage'.

> Expected: Request details including the full query and variables {'resourceIdentifier': 'brdoors3'}.

### Step 3: Replay the GraphQL Query

**Context**: Send the query without authentication to retrieve hidden data.

Execute [[commands/graphql-user-profile-query]] to replay the request.

```bash
curl -X POST https://hackerone.com/graphql -H "Content-Type: application/json" -d '{"operationName":"UserProfilePage","variables":{"resourceIdentifier":"brdoors3"},"query":"query UserProfilePage($resourceIdentifier: String!) { user(username: $resourceIdentifier) { public_reviews(first: 5) { edges { node { public_feedback team { name handle } } } } }"}'
```

> The response will include 'public_reviews' with the hidden 'public_feedback' field, e.g., 'Clear language & video proof - excellent report.' from team 'Legal Robot', confirming disclosure.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/graphql-user-profile-query]]

## Tools Used

- [[tools/Browser-Developer-Tools]]
- [[tools/Incognito-Mode-Browser]]

## Tags

- information-disclosure
- graphql
- privacy-bypass
