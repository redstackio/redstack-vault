---
tags:
  - access-control
  - auth-bypass
  - email-disavowal
  - web-vulnerability
type: attack_chain
tools:
  - '[[tools/waybackurls]]'
  - '[[tools/grep]]'
tactics:
  - '[[Reconnaissance]]'
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Discover-Disavow-Endpoints-Using-Waybackurls]]'
  - '[[procedures/Exploit-Liberapay-Disavow-Endpoint]]'
step_count: 2
techniques:
  - '[[Gather Victim Host Information]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:30.756Z'
description: >-
  An attack chain exploiting improper access control on Liberapay's disavow
  endpoints, allowing unauthorized users to disassociate emails from accounts
  without authentication, discovered through reconnaissance on archived URLs.
skill_level: intermediate
impact_level: high
id: 8de9909e-5b04-49cb-bc87-1eb648d95eef
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
  - '[[Exploit Public-Facing Application]]'
---
# Unauthorized Email Disavowal on Liberapay via Unprotected Endpoints

Multi-stage attack chain demonstrating reconnaissance and exploitation of improper access control on Liberapay's disavow endpoints. Attackers can disassociate legitimate email addresses from user accounts without authentication, potentially locking out account owners and disrupting access to donation platforms.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance: Discover Endpoints] --> B[Exploitation: Disavow Email]
    B --> C[Impact: Account Lockout]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/waybackurls]]
- [[tools/grep]]

### Target Environment

- Web platform (liberapay.com)
- No specific ports or services required beyond HTTP/HTTPS access
- Internet access to Wayback Machine

### Initial Access Requirements

- No credentials needed
- Public network access to liberapay.com
- No prior access required

## Detailed Attack Procedures

### Step 1: Discover Disavow Endpoints
procedure: [[procedures/Discover-Disavow-Endpoints-Using-Waybackurls]]

**Objective**: Identify unprotected disavow endpoints on liberapay.com using archived URLs from the Wayback Machine.

**Instructions**: Use [[commands/waybackurls-grep-disavow]] to fetch and filter URLs containing 'disavow':

```bash
waybackurls liberapay.com | grep disavow
```

**Expected Output**: A list of URLs like https://liberapay.com/account/disavow/email/example@email.com that include the 'disavow' keyword.

**Success Indicators**:
- URLs containing 'disavow' are returned
- Endpoints appear unprotected based on URL structure

### Step 2: Exploit Disavow Endpoint
procedure: [[procedures/Exploit-Liberapay-Disavow-Endpoint]]

**Objective**: Access a discovered disavow URL to unauthorizedly disassociate an email from a Liberapay account.

**Instructions**: Open the discovered URL in a browser or send an HTTP request to trigger the disavowal without authentication.

For example, using curl:

```bash
curl -X GET "https://liberapay.com/account/disavow/email/target@example.com"
```

**Expected Output**: The server processes the request, disassociating the email without prompting for login, confirming the vulnerability.

**Success Indicators**:
- Email is disavowed successfully
- No authentication challenge is presented
- Account owner is notified or locked out upon attempting login

## Attack Chain Summary

### Key Achievements

1. Discovered hidden disavow endpoints through archival reconnaissance
2. Exploited lack of authentication to manipulate user accounts
3. Demonstrated potential for account disruption on a donation platform

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Reconnaissance]] Reconnaissance
- [[Initial Access]] Initial Access

---
*Last updated: 2023-10-01T00:00:00Z*
