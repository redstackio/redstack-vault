---
id: ac-rghost-idor-comments
tags:
  - idor
  - information-disclosure
  - web-vulnerability
  - enumeration
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Burp-Intruder]]'
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Tamper-with-Comment-ID-in-Requests]]'
  - '[[procedures/Attempt-Delete-on-Victims-Comment]]'
  - '[[procedures/Attempt-Edit-on-Victims-Comment]]'
  - '[[procedures/Enumerate-All-Comments-with-Burp-Intruder]]'
step_count: 4
techniques:
  - '[[Account Discovery]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:33.671Z'
description: >-
  Multi-stage attack exploiting Insecure Direct Object Reference (IDOR) in
  RGhost web app's comment endpoints to disclose other users' comment contents,
  enumerate all comments, and potentially disrupt victim editing capabilities.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
  - '[[Exploit Public-Facing Application]]'
---
# IDOR in RGhost Comment System for Unauthorized Comment Disclosure and Enumeration

Multi-stage attack chain demonstrating exploitation of an Insecure Direct Object Reference (IDOR) vulnerability in the RGhost web application's comment system. The attack allows an authenticated user to view other users' private comment contents by manipulating sequential integer comment IDs on the DELETE /comments/ and edit /comments/ endpoints. Without proper ownership validation, attackers can enumerate all comments across threads, disclose sensitive information, and potentially harass users by disabling their edit options, though modifications do not persist due to server-side checks like captchas.

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
    A[Authenticate as Attacker] --> B[Tamper with Comment ID]
    B --> C[Attempt Delete to Reveal Content]
    C --> D[Attempt Edit to View and Disrupt]
    D --> E[Enumerate All Comments]
    E --> F[Disclose and Harvest Data]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#f39c12
    style E fill:#3498db
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]
- [[tools/Burp-Intruder]]

### Target Environment

- Web application (RGhost platform)
- Authenticated session required
- No specific ports; standard HTTPS (443)

### Initial Access Requirements

- Valid user credentials for authentication
- Network access to the RGhost web app
- Burp Suite proxy configured to intercept traffic

## Detailed Attack Procedures

### Step 1: Tamper with Comment ID in Requests
procedure: [[procedures/Tamper-with-Comment-ID-in-Requests]]

**Objective**: Manipulate the comment ID parameter to access another user's comment for edit or delete operations, bypassing ownership checks.

**Instructions**: Configure Burp Suite to intercept requests to the /comments/ endpoint. Identify a victim's comment ID (e.g., via sequential enumeration or observation). Replace the attacker's comment ID with the victim's in the request path or body.

For example, intercept a DELETE request and modify it as follows (using Burp Repeater for testing):

```http
DELETE /comments/12345 HTTP/1.1
Host: rghost.net
Authorization: Bearer [attacker_token]
```

Where 12345 is the victim's comment ID.

**Expected Output**: Response reveals the victim's comment content in the body, even if the delete fails due to captcha.

**Success Indicators**:
- Victim's comment text visible in response
- No ownership error; request processes

### Step 2: Attempt Delete on Victim's Comment
procedure: [[procedures/Attempt-Delete-on-Victims-Comment]]

**Objective**: Trigger a delete operation on a non-owned comment to force disclosure of its content in the error response.

**Instructions**: Using Burp Suite, send a modified DELETE request to /comments/{victim_id}. The server may prompt a captcha, but the response includes the full comment details.

Example request in Burp Repeater:

```http
DELETE /comments/67890 HTTP/1.1
Host: rghost.net
Content-Type: application/json
Authorization: Bearer [attacker_token]

{}
```

**Expected Output**: JSON response with victim's comment data, e.g., {"comment": "Victim's private text", "error": "Captcha required"}.

**Success Indicators**:
- Comment content leaked in response
- Captcha triggered but data still exposed

### Step 3: Attempt Edit on Victim's Comment
procedure: [[procedures/Attempt-Edit-on-Victims-Comment]]

**Objective**: Attempt to edit a victim's comment to view its original content and potentially disable the victim's edit UI, enabling harassment.

**Instructions**: Intercept an edit request in Burp Suite and alter the comment ID to the victim's. Modify the content payload slightly (e.g., change a character) and submit. The response shows the original content, but saves fail due to validation.

Example PUT request:

```http
PUT /comments/11111 HTTP/1.1
Host: rghost.net
Content-Type: application/json
Authorization: Bearer [attacker_token]

{"content": "Victim's text changed to X"}
```

**Expected Output**: Response echoes original content, e.g., {"original": "Victim's text", "error": "Ownership mismatch"}; victim's edit option may be disabled client-side.

**Success Indicators**:
- Original comment visible in response
- Victim's edit functionality disrupted (UI change)

### Step 4: Enumerate All Comments with Burp Intruder
procedure: [[procedures/Enumerate-All-Comments-with-Burp-Intruder]]

**Objective**: Systematically enumerate and harvest contents of all comments across threads by iterating over sequential IDs, exploiting lack of rate limiting.

**Instructions**: In Burp Intruder, capture a base request to /comments/{id} (e.g., GET or PUT). Mark the ID position as a payload position. Load a payload list of sequential integers (e.g., 1-10000). Attack with no rate limits to fetch responses.

Configure Intruder positions and payloads:

- Position: §id§ in /comments/§id§
- Payloads: Numbers from 1 to max expected comments

**Expected Output**: Batch of responses containing comment contents for valid IDs; grep for non-empty bodies.

**Success Indicators**:
- Multiple valid comments retrieved
- Full thread contents disclosed

## Attack Chain Summary

### Key Achievements

1. Unauthorized disclosure of private comment contents via IDOR manipulation
2. Complete enumeration of all comments without detection
3. Potential denial of edit service for victims through UI disruption

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Account Discovery]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Discovery]]

---
*Last updated: 2023-10-01T00:00:00Z*
