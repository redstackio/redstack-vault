---
tags:
  - idor
  - web
  - disclosure
  - mavenlink
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
created_at: '2024-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Mavenlink-IDOR-for-Workspace-Disclosure]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:30.027Z'
description: >-
  A single-stage attack exploiting an Insecure Direct Object Reference (IDOR)
  vulnerability in Mavenlink's web application to disclose sensitive workspace
  titles via verbose error messages.
skill_level: intermediate
impact_level: high
id: d3ac3ae0-a579-48b9-b81a-23d5977cad48
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# IDOR in Mavenlink Workspace Access Leading to Sensitive Information Disclosure

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via IDOR] --> B[Information Disclosure]

    style A fill:#e74c3c
    style B fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser (e.g., Chrome Developer Tools for URL manipulation)
- [[tools/curl]]

### Target Environment

- Web platform
- Access to Mavenlink application at app.mavenlink.com
- Valid user account with partial permissions

### Initial Access Requirements

- Authenticated session in Mavenlink
- Knowledge of workspace ID format (sequential integers)
- No elevated privileges needed

## Detailed Attack Procedures

### Step 1: Exploit IDOR for Unauthorized Access
procedure: [[procedures/Exploit-Mavenlink-IDOR-for-Workspace-Disclosure]]

**Objective**: Attempt access to a workspace ID outside the user's permissions to trigger a verbose error message disclosing the restricted workspace title.

**Instructions**: Authenticate into the Mavenlink application at app.mavenlink.com. Identify a base URL for workspace access, such as `/workspaces/{id}`. Replace `{id}` with an unauthorized workspace ID (e.g., increment from a known authorized ID). Use browser developer tools or [[commands/curl-get-workspace]] to send the request:

```bash
curl -H "Cookie: session=your_session_cookie" "https://app.mavenlink.com/workspaces/12345"
```

Observe the response for verbose error details revealing the workspace title.

**Expected Output**: HTTP 403 or similar error with body containing the sensitive workspace title, e.g., "Access denied to workspace 'Project Alpha - Confidential'".

**Success Indicators**:
- Error message includes unauthorized workspace title
- Confirmation of disclosure without full access

## Attack Chain Summary

### Key Achievements

1. Unauthorized disclosure of sensitive workspace titles
2. Exploitation of improper authorization checks in web endpoint
3. Demonstration of IDOR impact on data confidentiality

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Discovery]]

---
*Last updated: 2024-10-01T00:00:00Z*
