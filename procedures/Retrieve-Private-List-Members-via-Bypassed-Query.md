---
id: proc-885539-retrieve-members
tags:
  - data-disclosure
  - access-bypass
  - graphql
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
  - GraphQL
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:26:00.357Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Steal Web Session Cookie]]'
---
# Retrieve Private List Members via Bypassed Query

## Summary

This procedure uses a valid private list ID to query ListMembers without authentication checks, disclosing user IDs, names, and details.

## Description

Once a list ID is obtained, POST to https://api.twitter.com/graphql/iUmNRKLdkKVH4WyBNw9x2A/ListMembers with variables {"listId": "valid-id", "count":20, "cursor": null}. The lack of privacy validation returns full member data, enabling unauthorized enumeration of sensitive groupings.

## Requirements

1. Valid private list ID from prior steps.
2. Authenticated session (though bypass works without full access).
3. HTTP client for POST requests.

## Defense

Defensive measures and detection strategies:

- Validate requester access to list privacy settings in every query.
- Audit logs for unauthorized ListMembers calls.
- Encrypt or limit sensitive user data in responses.

## Objectives

1. Fetch unauthorized member details.
2. Enumerate private user groupings.
3. Achieve data disclosure.

## Instructions

### Step 1: Craft Retrieval Request

**Context**: Prepare payload with known listId.

POST to the endpoint with JSON body including listId and count.

**Expected Output**: JSON array of users {"users": [{ "id": "user123", "name": "User" }]}.

### Step 2: Paginate if Needed

**Context**: Use cursor for more members.

Include "cursor": "next-value" in subsequent requests.

**Expected Output**: Complete list of members.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Steal Web Session Cookie]] Data from Waste Repositories (adapted for API leak)

### Sub-Techniques

- None

## Commands Used

- None specific

## Tools Used

- None

## Tags

- [[data-disclosure]]
- [[access-bypass]]
