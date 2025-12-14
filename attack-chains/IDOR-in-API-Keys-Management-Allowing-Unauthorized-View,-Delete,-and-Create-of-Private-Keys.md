---
tags:
  - idor
  - api-keys
  - authorization-bypass
  - credential-access
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
commands:
  - '[[commands/curl-delete-api-key]]'
  - '[[commands/curl-create-api-key]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-Test-Accounts-and-Organization]]'
  - '[[procedures/Invite-Attacker-as-Member]]'
  - '[[procedures/Create-Private-API-Keys-as-Victim]]'
  - '[[procedures/Access-and-View-API-Keys-as-Attacker]]'
  - '[[procedures/Delete-API-Key-via-IDOR]]'
  - '[[procedures/Manipulate-Cookies-for-API-Key-Creation]]'
step_count: 8
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:25:23.068Z'
description: >-
  Multi-stage attack exploiting Insecure Direct Object Reference (IDOR) in an
  organization's API keys system, enabling a low-privilege member to view,
  delete, and create private API keys, leading to sensitive credential exposure
  and unauthorized actions.
skill_level: intermediate
impact_level: high
id: cb6eb677-889d-4e22-8c68-f00bf613480b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
---
# IDOR in API Keys Management Allowing Unauthorized View, Delete, and Create of Private Keys

Multi-stage attack chain demonstrating exploitation of an Insecure Direct Object Reference (IDOR) vulnerability in the API keys management system of a web platform, allowing a limited-privilege organization member to bypass authorization and manipulate private API keys owned by the organization.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 8 |
| Execution Time | ~30 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Accounts and Organization] --> B[Invite Attacker Member]
    B --> C[Create Victim API Keys]
    C --> D[Access Keys as Attacker]
    D --> E[Delete Key via IDOR]
    E --> F[Manipulate for Creation]
    F --> G[Exfiltrate or Abuse Keys]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#3498db
    style F fill:#3498db
    style G fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome with developer tools)
- Optional: Proxy tool like Burp Suite for request manipulation

### Target Environment

- Web platform at https://target-platform.com
- Organization management features enabled
- API keys endpoint accessible

### Initial Access Requirements

- Ability to register user accounts
- Valid email for invitations
- No prior organization access needed

## Detailed Attack Procedures

### Step 1: Create Test Accounts
procedure: [[procedures/Create-Test-Accounts-and-Organization]]

**Objective**: Establish victim and attacker accounts to simulate the attack scenario.

**Instructions**: Register two separate user accounts on the platform using distinct emails. Use the victim account credentials for organization ownership and the attacker account for limited member access.

**Expected Output**: Two active user sessions with login capabilities.

**Success Indicators**:
- Successful registration and login for both accounts
- No errors during account creation

### Step 2: Create Organization as Victim
procedure: [[procedures/Create-Test-Accounts-and-Organization]]

**Objective**: Set up an organization under the victim account to serve as the target for IDOR exploitation.

**Instructions**: Log in as the victim user, navigate to the organization creation page, and create a new organization. Note the generated organization UUID for later use.

**Expected Output**: New organization dashboard accessible.

**Success Indicators**:
- Organization created with unique ORG-UUID
- Victim listed as owner

### Step 3: Invite Attacker as Member
procedure: [[procedures/Invite-Attacker-as-Member]]

**Objective**: Add the attacker account to the organization with limited 'Member' permissions to test authorization bypass.

**Instructions**: From the victim session, access the members management page and send an invitation to the attacker email, assigning the 'Member' role.

**Expected Output**: Invitation sent and accepted by attacker.

**Success Indicators**:
- Attacker account joins organization as Member
- No elevated permissions granted

### Step 4: Create Private API Keys as Victim
procedure: [[procedures/Create-Private-API-Keys-as-Victim]]

**Objective**: Generate private API keys under the victim's organization for subsequent unauthorized access.

**Instructions**: Log in as victim, navigate to the API keys section, create multiple private keys, and save the creation request (e.g., via browser dev tools or proxy) as 'Create_Req' for cookie manipulation later.

**Expected Output**: List of private API keys visible to victim.

**Success Indicators**:
- API keys created with unique API-UUIDs
- Keys marked as private to organization

### Step 5: Access API Keys as Attacker
procedure: [[procedures/Access-and-View-API-Keys-as-Attacker]]

**Objective**: Use the attacker's session to view organization API keys, demonstrating IDOR read access.

**Instructions**: Log in as attacker, directly access the API keys endpoint using the ORG-UUID, and copy a target API key's UUID.

**Expected Output**: Full list of private API keys visible despite limited role.

**Success Indicators**:
- Unauthorized view of victim's API keys
- API-UUID copied successfully

### Step 6: Delete API Key via IDOR
procedure: [[procedures/Delete-API-Key-via-IDOR]]

**Objective**: Delete a private API key using the attacker's session, confirming IDOR manipulation.

**Instructions**: Using the copied API-UUID, send a DELETE request to the specific endpoint with attacker's authentication.

Execute [[commands/curl-delete-api-key]]:

```bash
curl -X DELETE https://target-platform.com/organization/ORG-UUID/apiKeys/API-UUID -H "Cookie: session=attacker_session_cookie"
```

**Expected Output**: 200 OK or success response indicating deletion.

**Success Indicators**:
- API key removed from organization
- No authorization error

### Step 7: Manipulate Cookies for Creation
procedure: [[procedures/Manipulate-Cookies-for-API-Key-Creation]]

**Objective**: Replay the creation request with attacker's cookies to create new unauthorized API keys.

**Instructions**: Copy the attacker's session cookies, replace them in the saved 'Create_Req' from step 4, and resubmit the request.

Execute [[commands/curl-create-api-key]] with modified cookies:

```bash
curl -X POST https://target-platform.com/organization/ORG-UUID/apiKeys -H "Cookie: session=attacker_session_cookie" -d '{"name":"Unauthorized Key","scopes":["read","write"] }'
```

**Expected Output**: New API key created under organization.

**Success Indicators**:
- Successful creation without ownership check
- New key usable for unauthorized actions

### Step 8: Validate Impact
procedure: [[procedures/Access-and-View-API-Keys-as-Attacker]]

**Objective**: Confirm the full impact by viewing the manipulated keys and assessing potential for data exposure or abuse.

**Instructions**: Re-access the API keys list as attacker to verify deletions and new creations, then test any exfiltrated keys against organization resources.

**Expected Output**: Altered API keys list reflecting unauthorized changes.

**Success Indicators**:
- Sensitive keys viewed or controlled
- Potential for broader compromise confirmed

## Attack Chain Summary

### Key Achievements

1. Bypassed authorization to view private API keys
2. Deleted organization-owned keys without permission
3. Created new keys as a limited member, enabling persistence or escalation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Valid Accounts]] Valid Accounts

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Discovery]] Discovery

---

*Last updated: 2023-10-01T00:00:00Z*
