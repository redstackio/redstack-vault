---
id: ac-914331-idOR-html-injection
tags:
  - idor
  - xss
  - html-injection
  - api-vulnerability
  - web
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
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
  - '[[procedures/Create-Note-as-Owner-User]]'
  - '[[procedures/Login-as-Team-Member-User]]'
  - >-
    [[procedures/Exploit-IDOR-with-Burp-Suite-for-Note-Modification-and-HTML-Injection]]
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:25:29.476Z'
description: >-
  A multi-stage attack exploiting Insecure Direct Object Reference (IDOR) in the
  Outpost application's notes API to allow unauthorized editing of other users'
  notes, combined with HTML injection for potential stored XSS effects within a
  team context.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# IDOR in Notes API Leading to Unauthorized Note Editing and HTML Injection

Multi-stage attack chain demonstrating exploitation of an Insecure Direct Object Reference (IDOR) vulnerability in the Outpost application's notes API, allowing a team member with 'USER' role to edit any other team member's notes by manipulating the note UUID in a PUT request. This is chained with HTML injection into the note body, potentially causing stored XSS-like effects when the note is viewed by other users within the team.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Owner Note] --> B[Login as USER] --> C[Intercept and Modify Request]
    C --> D[Unauthorized Edit and HTML Injection]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web application (Outpost notes API)
- Required services/ports: HTTPS on standard web ports (e.g., 443)
- Network access requirements: Valid team credentials for owner and user roles

### Initial Access Requirements

- Owner role credentials for note creation
- USER role credentials for the same team
- Prior access needed: Ability to authenticate to the application

## Detailed Attack Procedures

### Step 1: Create Note as Owner
procedure: [[procedures/Create-Note-as-Owner-User]]

**Objective**: Create a target note as an owner user to obtain its UUID for later targeting.

**Instructions**: Authenticate to the Outpost application using owner credentials and create a new note via the interface. Note the generated UUID (e.g., b9db186a-c0af-462d-ad71-c30c2bfd7cf5) for use in subsequent steps.

**Expected Output**: A new note is created, and its UUID is visible or retrievable from the application or API response.

**Success Indicators**:
- Note successfully created
- UUID captured for targeting

### Step 2: Login as Team Member
procedure: [[procedures/Login-as-Team-Member-User]]

**Objective**: Authenticate as a team member with 'USER' role to gain access to the notes API within the same team context.

**Instructions**: Log in to the Outpost application using team member credentials with 'USER' role. Ensure the user is in the same team as the owner to maintain team-scoped access.

**Expected Output**: Successful authentication, allowing access to create or update personal notes.

**Success Indicators**:
- Login successful
- Ability to access notes interface confirmed

### Step 3: Intercept and Modify Update Request
procedure: [[procedures/Exploit-IDOR-with-Burp-Suite-for-Note-Modification-and-HTML-Injection]]

**Objective**: Exploit IDOR by intercepting a note update request, replacing the UUID with the target's, and injecting malicious HTML to demonstrate unauthorized editing and potential XSS.

**Instructions**: Attempt to update or create a note as the 'USER'. Use [[tools/Burp-Suite]] to intercept the PUT request to `/api/v1/note/{uuid}`. Modify the path parameter `{uuid}` to the owner's note UUID and inject an HTML payload into the 'body' field of the JSON, such as {"body":"<h1><a href=\"j&#97v&#97script&#x3A;&#97lert(1)\" >This is a test</a></h1>","mentionUuids":[]}. Forward the modified request.

**Expected Output**: The owner's note is updated with the injected HTML content.

**Success Indicators**:
- Request modification successful
- Owner's note altered with injected content
- Potential alert execution when note is viewed

## Attack Chain Summary

### Key Achievements

1. Unauthorized access to edit other team members' notes via IDOR
2. Successful injection of malicious HTML into notes
3. Demonstration of stored XSS-like impact within team visibility

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Discovery]]

---

*Last updated: 2023-10-01T00:00:00Z*
