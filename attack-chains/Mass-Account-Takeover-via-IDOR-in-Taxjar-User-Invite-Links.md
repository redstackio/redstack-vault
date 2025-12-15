---
tags:
  - idor
  - account-takeover
  - authentication-bypass
  - taxjar
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-IDOR-in-Taxjar-Invite-Deletion]]'
step_count: 3
techniques:
  - '[[Valid Accounts]]'
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:33:34.306Z'
description: >-
  An attack chain exploiting an Insecure Direct Object Reference (IDOR)
  vulnerability in Taxjar's user invitation system, where a leaked token allows
  unauthorized manipulation of invitations across organizations, leading to
  widespread account takeovers without user interaction.
skill_level: intermediate
impact_level: high
id: b8eb792f-400c-427d-b351-69c7b642ebc3
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Account Manipulation]]'
---
# Mass Account Takeover via IDOR in Taxjar User Invite Links

Multi-stage attack chain demonstrating a complete attack workflow exploiting an IDOR in Taxjar's invitation system to achieve mass account takeovers.

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
    A[Obtain Invite Token] --> B[Exploit IDOR in Invite Deletion]
    B --> C[Account Takeover and Manipulation]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools or [[commands/curl-delete-taxjar-invite]] for HTTP requests

### Target Environment

- Web platform
- Access to https://app.taxjar.com/
- No specific ports or services beyond standard HTTPS (443)

### Initial Access Requirements

- Valid invite link/token from any Taxjar user or organization (can be obtained via social engineering, leaks, or public sharing)
- Network access to the internet
- No prior credentials needed due to the bypass

## Detailed Attack Procedures

### Step 1: Obtain Invite Token

**Objective**: Acquire a valid invitation token from Taxjar's user invite system to use as the entry point for exploitation.

**Instructions**: Invitations in Taxjar are shared via links containing a unique token. These can be obtained by registering a test account and generating an invite, or sourced from leaked/public links. Extract the token from the invite URL, which typically follows the format `https://app.taxjar.com/invite?token=LEAKED_TOKEN_HERE`.

**Expected Output**: A raw token string that can be used in subsequent API requests.

**Success Indicators**:
- Token extracted successfully
- Token validates when tested against the invite endpoint

### Step 2: Exploit IDOR in Invite Deletion

procedure: [[procedures/Exploit-IDOR-in-Taxjar-Invite-Deletion]]

**Objective**: Use the leaked token to access and manipulate invitation records belonging to other users or organizations via the delete invitation endpoint, bypassing ownership validation.

**Instructions**: Send a request to the delete invitation endpoint using the token to look up and delete an invitation ID not owned by the requester. This exploits the lack of organization-level validation, allowing interference with other accounts.

Execute [[commands/curl-delete-taxjar-invite]] to test the deletion:

```bash
curl -X POST https://app.taxjar.com/api/invitations/FAKE_INVITE_ID/delete \
  -H "Authorization: Bearer LEAKED_TOKEN_HERE" \
  -H "Content-Type: application/json"
```

**Expected Output**: Successful deletion response (e.g., 200 OK) for an invitation not owned by the token's organization, confirming the IDOR.

**Success Indicators**:
- Invitation deleted without ownership error
- Ability to target arbitrary invitation IDs

### Step 3: Account Takeover and Manipulation

**Objective**: Leverage the IDOR to manipulate invitations, enabling acceptance or redirection to attacker-controlled accounts for full takeover.

**Instructions**: After deleting or altering invites, resend or accept manipulated invitations to gain access to victim accounts. Chain this with the IDOR to enumerate and takeover multiple accounts in the same organization by iterating over invitation IDs.

Use the same endpoint pattern to manipulate multiple IDs:

```bash
curl -X POST https://app.taxjar.com/api/invitations/ANOTHER_ID/manipulate \
  -H "Authorization: Bearer LEAKED_TOKEN_HERE" \
  -d '{"action": "accept", "email": "attacker@example.com"}'
```

**Expected Output**: Confirmation of manipulation, followed by login access to victim accounts.

**Success Indicators**:
- Access granted to unauthorized accounts
- Control over user data and organization settings

## Attack Chain Summary

### Key Achievements

1. Bypassed authentication using leaked invite tokens
2. Achieved mass account takeovers via IDOR manipulation
3. No user interaction required for exploitation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]
- [[Account Manipulation]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---

*Last updated: 2023-10-01T00:00:00Z*
