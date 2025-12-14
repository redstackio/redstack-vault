---
tags:
  - phabricator
  - conduit-api
  - phid-spoofing
  - auth-bypass
  - idor
  - feed-spoofing
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Identify-Phabricator-Feed-Publish-API-Endpoint]]'
  - '[[procedures/Obtain-PHIDs-for-Spoofing-in-Phabricator]]'
  - '[[procedures/Manipulate-JSON-Payload-for-Feed-Spoofing]]'
  - '[[procedures/Submit-Spoofed-Payload-to-Phabricator-Feed-API]]'
  - '[[procedures/Exploit-Phabricator-Feed-for-Spamming-or-Errors]]'
step_count: 5
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:11.080Z'
description: >-
  Authenticated exploitation of Phabricator's Conduit feed.publish API to spoof
  feed stories, impersonate users, imply access to restricted objects, spam
  feeds, or trigger database errors.
id: bb80e254-9a0d-4e4f-b026-a070d5e8324b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Phabricator Conduit Feed.Publish API Spoofing for User Impersonation and Restricted Object Access

Multi-stage attack chain demonstrating exploitation of Phabricator's Conduit API vulnerability to publish spoofed feed stories. This allows authenticated users to impersonate others by manipulating PHIDs in the 'data' JSON payload, imply unauthorized access to restricted objects, spam the news feed, or cause database errors requiring manual intervention. The vulnerability stems from insufficient validation in the feed.publish endpoint, predating Phabricator's policy system.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Identify API Endpoint] --> B[Obtain PHIDs]
    B --> C[Manipulate Payload]
    C --> D[Submit Spoofed Feed Story]
    D --> E[Spam or Trigger Errors]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard HTTP clients like curl)

### Target Environment

- Phabricator instance with Conduit API enabled
- Web platform (PHP-based)
- Access to database (phabricator_feed.feed_storydata table for cleanup)

### Initial Access Requirements

- Valid authenticated session or API token for Conduit
- Ability to view user pages and some object references (e.g., tasks)
- No elevated privileges needed beyond basic authentication

## Detailed Attack Procedures

### Step 1: Identify Phabricator Feed.Publish API Endpoint
procedure: [[procedures/Identify-Phabricator-Feed-Publish-API-Endpoint]]

**Objective**: Understand the structure and parameters of the feed.publish API to prepare for exploitation.

**Instructions**: Review Phabricator documentation or test the endpoint to confirm it accepts 'type' as 'PhabricatorTokenGivenFeedStory' and a 'data' JSON with 'authorPHID', 'tokenPHID', and 'objectPHID'.

**Expected Output**: Confirmation of API acceptance of manipulable parameters.

**Success Indicators**:
- API responds without errors to basic calls
- Parameters like 'type' and 'data' are parsable in responses

### Step 2: Obtain PHIDs for Spoofing
procedure: [[procedures/Obtain-PHIDs-for-Spoofing-in-Phabricator]]

**Objective**: Gather PHIDs of target users and restricted objects to use in spoofing.

**Instructions**: Navigate to the target user's profile page to extract their PHID from the HTML or API response. For objects, inspect HTML of accessible pages referencing restricted items (e.g., subtasks).

**Expected Output**: Valid PHID strings, e.g., 'PHID-USER-abc123' for author and 'PHID-PROJ-def456' for object.

**Success Indicators**:
- PHIDs retrieved without authentication errors
- PHIDs match expected format (PHID-TYPE-id)

### Step 3: Manipulate JSON Payload for Feed Spoofing
procedure: [[procedures/Manipulate-JSON-Payload-for-Feed-Spoofing]]

**Objective**: Craft a spoofed JSON payload to impersonate a user or reference restricted objects.

**Instructions**: Replace 'authorPHID' with the target's PHID, set 'objectPHID' to a restricted object's PHID, and use a valid 'tokenPHID' like 'PHID-TOKN-medal-4'.

**Expected Output**: Valid JSON structure ready for API submission.

**Success Indicators**:
- JSON validates without syntax errors
- Fields match required API format

### Step 4: Submit Spoofed Payload to Phabricator Feed API
procedure: [[procedures/Submit-Spoofed-Payload-to-Phabricator-Feed-API]]

**Objective**: Publish the spoofed feed story to create misleading content in the news feed.

**Instructions**: Use [[commands/curl-submit-phabricator-feed]] to POST the payload to the Conduit API endpoint.

```bash
curl -X POST 'https://phabricator.example.com/api/feed.publish' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'output=json&__conduit__={"token":"api-token-here"}&type=PhabricatorTokenGivenFeedStory&data={"authorPHID":"PHID-USER-spoofed","tokenPHID":"PHID-TOKN-medal-4","objectPHID":"PHID-PROJ-restricted"}'
```

**Expected Output**: API response with story ID, confirming publication.

**Success Indicators**:
- Feed story appears in the news feed attributed to spoofed user
- No immediate validation errors

### Step 5: Exploit for Spamming or Database Errors
procedure: [[procedures/Exploit-Phabricator-Feed-for-Spamming-or-Errors]]

**Objective**: Escalate impact by spamming the feed or inducing errors for denial of service.

**Instructions**: Repeat submissions with [[commands/curl-submit-phabricator-feed]] using varied or invalid data (e.g., empty lists) to flood the feed or crash storydata table processing.

**Expected Output**: Multiple erroneous feed stories or database exceptions.

**Success Indicators**:
- Feed overwhelmed with spam entries
- Admin intervention required for cleanup in phabricator_feed.feed_storydata

## Attack Chain Summary

### Key Achievements

1. Successful impersonation of users via spoofed feed stories
2. Implied access to restricted objects, misleading permission views
3. Potential for feed spamming or database errors forcing manual remediation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
