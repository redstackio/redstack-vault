---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - xss
  - stored-xss
  - rails
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Create-Malicious-Skill-with-XSS-Payload]]'
  - '[[procedures/Enable-Pentester-Profile-for-Target-User]]'
  - '[[procedures/Assign-Malicious-Skill-to-User-Profile]]'
  - '[[procedures/Trigger-XSS-by-Viewing-Profile-in-Support-Backend]]'
step_count: 4
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:55.801Z'
description: >-
  A multi-stage attack demonstrating stored XSS exploitation in HackerOne's
  internal Support Backend by injecting malicious JavaScript into pentester
  skill names, leading to arbitrary code execution when profiles are viewed.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Stored XSS in HackerOne Support Backend via Unsanitized Skill Names

Multi-stage attack chain demonstrating a complete stored XSS workflow in HackerOne's internal Support Backend, where unsanitized skill names in pentester profiles allow injection of JavaScript payloads that execute when profiles are viewed by support staff.

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
    A[Create Malicious Skill] --> B[Enable Pentester Profile]
    B --> C[Assign Skill to Profile]
    C --> D[View Profile and Trigger XSS]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Rails console access (local development environment)

### Target Environment

- Ruby on Rails application (HackerOne Support Backend)
- Port 8080 open for local testing
- Web platform with authentication

### Initial Access Requirements

- Access to Rails console for setup
- Valid user credentials for the target application
- Authentication as a support user to view profiles

## Detailed Attack Procedures

### Step 1: Create Malicious Skill
procedure: [[procedures/Create-Malicious-Skill-with-XSS-Payload]]

**Objective**: Inject an XSS payload into a new skill record in the database to prepare for profile assignment.

**Instructions**: Access the Rails console and execute the command to create a skill with a script tag payload:

Using [[commands/rails-create-malicious-skill]]:

```ruby
Skill.create! name:'<script>alert(/XSS/);</script>'
```

**Expected Output**: A new Skill object is created and returned in the console, confirming the malicious name is stored.

**Success Indicators**:
- Skill record created without errors
- Payload visible in database query

### Step 2: Enable Pentester Profile
procedure: [[procedures/Enable-Pentester-Profile-for-Target-User]]

**Objective**: Update the target user's record to allow creation of a pentester profile.

**Instructions**: In the Rails console, locate the user and set the pentester flag:

Using [[commands/rails-enable-pentester-profile]]:

```ruby
User.find_by!(username:'hacker').update! h1_pentester:true
```

**Expected Output**: Updated User object displayed, with h1_pentester set to true.

**Success Indicators**:
- User record updated successfully
- Pentester flag enabled for profile creation

### Step 3: Assign Malicious Skill
procedure: [[procedures/Assign-Malicious-Skill-to-User-Profile]]

**Objective**: Authenticate as the target user and incorporate the malicious skill into their pentester profile.

**Instructions**: Enable the pentester-profile feature flag if needed, then log in as the 'hacker' user, navigate to the settings page, and select the malicious skill during profile setup at http://localhost:8080/settings/pentests.

No console commands required; perform via web interface.

**Expected Output**: Profile created with the skill assigned, payload stored in user data.

**Success Indicators**:
- Profile saved without validation errors
- Skill appears in profile preview

### Step 4: Trigger XSS Execution
procedure: [[procedures/Trigger-XSS-by-Viewing-Profile-in-Support-Backend]]

**Objective**: Authenticate to the Support Backend and view the profile to execute the injected JavaScript.

**Instructions**: Sign in to the Support Backend at http://localhost:8080/support, then navigate to the user's profile at http://localhost:8080/support/users/hacker. The payload executes in the rendered HTML (title attribute or span content).

**Expected Output**: Alert box pops up with 'XSS' or arbitrary JavaScript runs in the backend context.

**Success Indicators**:
- JavaScript alert or console log triggers
- Potential session hijacking indicators if payload is modified

## Attack Chain Summary

### Key Achievements

1. Successful injection of stored XSS payload into skill names
2. Profile creation and assignment without sanitization
3. Execution of JavaScript in Support Backend context upon viewing
4. Demonstration of potential for data theft or session hijacking

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2023-10-01T12:00:00Z*
