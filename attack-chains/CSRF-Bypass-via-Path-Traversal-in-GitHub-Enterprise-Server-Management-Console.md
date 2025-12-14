---
tags:
  - csrf
  - path-traversal
  - privilege-escalation
  - github-enterprise
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/CSRF-Bypass-via-Path-Traversal-in-GitHub-Enterprise]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:27:57.876Z'
description: >-
  Attack chain exploiting a path traversal vulnerability in the GitHub
  Enterprise Server management console to bypass CSRF protections, enabling
  privilege escalation against logged-in administrators.
skill_level: intermediate
impact_level: high
id: 4b903479-76c2-4105-9f6f-30f527e5b4c5
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
---
# CSRF Bypass via Path Traversal in GitHub Enterprise Server Management Console

Multi-stage attack chain demonstrating a complete attack workflow targeting the GitHub Enterprise Server management console. This vulnerability, discovered by researcher bitquark and reported on March 2, 2022 (CVE-2022-23732), allows attackers to use path traversal to bypass CSRF protections, potentially escalating privileges by tricking logged-in administrators into performing unauthorized actions. Affected versions are all prior to 3.5, with fixes in 3.1.19, 3.2.11, 3.3.6, and 3.4.1.

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
    A[Target Logged-in Admin] --> B[Exploit Path Traversal for CSRF Bypass]
    B --> C[Privilege Escalation]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools or proxy like Burp Suite for crafting requests

### Target Environment

- GitHub Enterprise Server versions prior to 3.5
- Web platform with management console accessible
- Required services/ports: HTTPS on port 443 for management console
- Network access requirements: Ability to send requests to the target's management console endpoint

### Initial Access Requirements

- No prior credentials needed for attacker, but targets a logged-in admin session
- Network position: External or internal, depending on console exposure
- Prior access needed: Social engineering to get admin to interact with malicious payload (e.g., click link)

## Detailed Attack Procedures

### Step 1: Exploit CSRF Bypass
procedure: [[procedures/CSRF-Bypass-via-Path-Traversal-in-GitHub-Enterprise]]

**Objective**: Use path traversal in a crafted request to bypass CSRF protections in the management console, allowing unauthorized actions that escalate privileges using the victim's session.

**Instructions**: Identify the management console endpoint (typically at https://<ghes-host>/manage). Craft a malicious request that includes a path traversal payload to manipulate the CSRF token validation path. For example, use a tool like curl to send a POST request targeting a sensitive action, such as modifying settings or adding users, while traversing to bypass the token check:

```bash
curl -X POST 'https://<ghes-host>/manage/settings' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'action=update&path=../../../bypass/csrf/token&value=malicious'
```

This payload attempts to traverse out of the expected directory to a location where CSRF checks are not enforced. Deliver this via a phishing link or malicious webpage that the admin visits while logged in.

**Expected Output**: Successful response indicating the action was performed (e.g., 200 OK with updated settings confirmation), without triggering CSRF errors.

**Success Indicators**:
- No CSRF validation error in response
- Privileged action completes (e.g., new user added or settings changed)
- Attacker gains elevated access or data exfiltration

## Attack Chain Summary

### Key Achievements

1. Bypassed CSRF protections using path traversal
2. Achieved privilege escalation against logged-in management console users
3. Demonstrated impact on GitHub Enterprise Server confidentiality and integrity

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[File and Directory Discovery]] File and Directory Discovery

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Privilege Escalation]] Privilege Escalation

---
*Last updated: 2023-10-01T00:00:00Z*
