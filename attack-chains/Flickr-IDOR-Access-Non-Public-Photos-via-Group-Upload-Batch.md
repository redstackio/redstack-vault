---
tags:
  - idor
  - flickr
  - unauthorized-access
  - photo-exposure
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Discover-Non-Public-Photo-ID]]'
  - '[[procedures/Add-Photo-to-Group-via-Upload-Batch]]'
  - '[[procedures/Access-Photo-through-Group-Membership]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:34.223Z'
description: >-
  An Insecure Direct Object Reference (IDOR) vulnerability in Flickr's photo
  handling allows unauthorized access to non-public photos by exploiting group
  upload batches to add third-party photos without owner consent.
skill_level: intermediate
impact_level: high
id: eea251f5-a0c3-4657-a70d-c3c59142512b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Flickr IDOR: Access Non-Public Photos via Group Upload Batch

Multi-stage attack chain demonstrating a complete attack workflow exploiting an IDOR in Flickr's photo system to access private photos through group manipulation.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Discover Photo ID] --> B[Add to Group Batch]
    B --> C[Access via Group]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser with developer tools
- Flickr account with group admin privileges

### Target Environment

- Flickr web platform
- Access to group upload features
- No specific ports required (HTTPS/443 implied)

### Initial Access Requirements

- Valid Flickr user account
- Membership or admin rights in a Flickr group
- Knowledge of target user's photo IDs from public sources or prior reconnaissance

## Detailed Attack Procedures

### Step 1: Discover Photo ID
procedure: [[procedures/Discover-Non-Public-Photo-ID]]

**Objective**: Identify the unique ID of a non-public photo uploaded by another user to enable direct referencing.

**Instructions**: Obtain photo IDs from public Flickr sources, such as shared links, API responses, or group discussions where IDs may be exposed incidentally. Use browser developer tools to inspect network requests during photo views or searches to extract IDs without authentication barriers.

**Expected Output**: A valid photo ID (numeric string) for a non-public photo.

**Success Indicators**:
- Photo ID retrieved successfully
- ID can be tested in subsequent steps without errors

### Step 2: Add Photo to Group via Upload Batch
procedure: [[procedures/Add-Photo-to-Group-via-Upload-Batch]]

**Objective**: Exploit the upload batch feature to include the third-party non-public photo ID in a group without owner approval.

**Instructions**: Log in to Flickr, navigate to the group upload interface, and initiate a batch upload. Manually input or edit the batch file to include the discovered photo ID as if it were part of your upload set. Submit the batch, leveraging the lack of ownership checks to associate the photo with the group.

**Expected Output**: Confirmation that the photo has been added to the group, visible in the group pool.

**Success Indicators**:
- Batch upload completes without rejection
- Photo appears in group listings

### Step 3: Access Photo through Group Membership
procedure: [[procedures/Access-Photo-through-Group-Membership]]

**Objective**: View the non-public photo by leveraging group visibility rules that expose added content to members.

**Instructions**: As a group member, navigate to the group's photo pool or search for the added photo using its ID. The photo renders fully due to group-granted permissions overriding the original privacy settings.

**Expected Output**: Full access to the photo's content, including metadata and images.

**Success Indicators**:
- Photo loads without access denied errors
- Unauthorized private content is visible

## Attack Chain Summary

### Key Achievements

1. Bypassed photo privacy controls via IDOR
2. Added third-party photos to groups without consent
3. Gained unauthorized viewing access through group membership

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Discovery]]

---
*Last updated: 2023-10-01T00:00:00Z*
