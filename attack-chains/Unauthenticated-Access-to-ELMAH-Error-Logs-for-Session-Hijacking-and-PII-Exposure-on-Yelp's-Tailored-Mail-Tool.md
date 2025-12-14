---
tags:
  - access-control
  - elmah
  - session-hijacking
  - pii-exposure
  - information-disclosure
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-access-url]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Verify-Subdomain-Redirect]]'
  - '[[procedures/Access-Tailored-Mail-Login]]'
  - '[[procedures/Retrieve-ELMAH-Error-Log-List]]'
  - '[[procedures/View-ELMAH-Log-Details-via-UI]]'
  - '[[procedures/Directly-Access-Specific-ELMAH-Log]]'
  - '[[procedures/Retrieve-Older-ELMAH-Logs]]'
step_count: 6
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Steal Web Session Cookie]]'
  - '[[Data from Information Repositories]]'
updated_at: '2025-12-14T17:30:47.152Z'
description: >-
  Multi-stage attack exploiting improper access control on an exposed ELMAH
  endpoint in Yelp's internal Tailored Mail admin tool, allowing unauthenticated
  retrieval of error logs containing sensitive session data, cookies, and PII
  for potential account takeover.
skill_level: beginner
impact_level: high
id: fd21e908-1331-4889-aeae-e57c69ed6ca5
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Steal Web Session Cookie]]'
  - '[[Data from Information Repositories]]'
---
# Unauthenticated Access to ELMAH Error Logs for Session Hijacking and PII Exposure on Yelp's Tailored Mail Tool

Multi-stage attack chain demonstrating exploitation of improper object-level access control on Yelp's internal Tailored Mail administration tool, hosted on proze.yelp.com. The chain reveals an unprotected ELMAH error logging endpoint, enabling unauthenticated attackers to retrieve over 75,000 error logs containing full HTTP requests, user sessions, cookies, PII (e.g., AUTH_PASSWORD, AUTH_USER, IP addresses), and internal error messages. This can lead to session hijacking, account takeover (ATO), and further internal reconnaissance.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 6 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Recon: Verify Subdomain] --> B[Access Internal Tool: Login Endpoint]
    B --> C[Exploit Endpoint: Retrieve Log List]
    C --> D[Extract Details: View Log UI]
    D --> E[Deep Dive: Direct Log Access]
    E --> F[Expand Scope: Older Logs]
    F --> G[Objective: Session Hijack & PII Exfil]

    style A fill:#e74c3c
    style B fill:#e74c3c
    style C fill:#f39c12
    style D fill:#f39c12
    style E fill:#3498db
    style F fill:#3498db
    style G fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome, Firefox)
- [[commands/curl-access-url]] (for scripted access)

### Target Environment

- Web platform
- Services: Tailored Mail internal admin tool, ELMAH error logging
- Tech stack: ASP.NET
- No specific ports required (HTTPS on 443)

### Initial Access Requirements

- Internet access to proze.yelp.com
- No credentials needed (unauthenticated)
- No prior access; public-facing subdomain

## Detailed Attack Procedures

### Step 1: Verify Subdomain Redirect
procedure: [[procedures/Verify-Subdomain-Redirect]]

**Objective**: Confirm the subdomain exists and redirects, indicating restricted external access to the internal tool.

**Instructions**: Use a web browser or [[commands/curl-access-url]] to access the base subdomain URL.

```bash
curl -i https://proze.yelp.com/
```

**Expected Output**: HTTP 302 redirect to https://www.yelp.com/, with no direct content served.

**Success Indicators**:
- Redirect response observed
- Confirms subdomain is active but protected

### Step 2: Access Tailored Mail Login
procedure: [[procedures/Access-Tailored-Mail-Login]]

**Objective**: Bypass redirect by directly accessing the internal admin login endpoint to confirm the tool's presence.

**Instructions**: Navigate directly to the login path using a browser or [[commands/curl-access-url]].

```bash
curl -i https://proze.yelp.com/app/login
```

**Expected Output**: Login page for Tailored Mail admin tool loads without authentication prompt.

**Success Indicators**:
- Internal application interface visible
- No redirect or access denial

### Step 3: Retrieve ELMAH Error Log List
procedure: [[procedures/Retrieve-ELMAH-Error-Log-List]]

**Objective**: Access the unprotected ELMAH endpoint to list recent error logs without authentication, exposing API errors.

**Instructions**: Visit the ELMAH listing endpoint with pagination parameters using a browser or [[commands/curl-access-url]].

```bash
curl https://proze.yelp.com/tmwebapi/elmah.axd?page=1&size=100
```

**Expected Output**: XML or HTML list of the last 100 error logs, including timestamps and error types.

**Success Indicators**:
- Log entries returned unauthenticated
- Over 75,000 total logs accessible via pagination

### Step 4: View ELMAH Log Details via UI
procedure: [[procedures/View-ELMAH-Log-Details-via-UI]]

**Objective**: Interact with the log list interface to retrieve detailed error information, including HTTP requests and sessions.

**Instructions**: From the log list page, click 'Details' on an entry using the browser.

**Expected Output**: Full error details page showing HTTP request headers, body, cookies, and session data.

**Success Indicators**:
- Sensitive data like cookies and AUTH_USER exposed
- No authentication required for details

### Step 5: Directly Access Specific ELMAH Log
procedure: [[procedures/Directly-Access-Specific-ELMAH-Log]]

**Objective**: Bypass UI interaction by directly requesting a specific log's details to extract secrets and PII.

**Instructions**: Use the log ID from the list to construct and access the detail endpoint with [[commands/curl-access-url]].

```bash
curl https://proze.yelp.com/tmwebapi/elmah.axd/detail?id=5A4E7ED8-28E8-4E39-9017-F55E2C9F5371
```

**Expected Output**: Detailed log including full requests, user cookies, AUTH_PASSWORD, and IP addresses.

**Success Indicators**:
- Session tokens and credentials retrieved
- Potential for immediate session hijacking

### Step 6: Retrieve Older ELMAH Logs
procedure: [[procedures/Retrieve-Older-ELMAH-Logs]]

**Objective**: Paginate to access historical logs for broader data exposure, including logs from early December.

**Instructions**: Adjust pagination parameters to fetch older entries using a browser or [[commands/curl-access-url]].

```bash
curl https://proze.yelp.com/tmwebapi/elmah.axd?page=100&size=100
```

**Expected Output**: List of older error logs with similar sensitive details.

**Success Indicators**:
- Logs dating back to December retrieved
- Expanded dataset for ATO or reconnaissance

## Attack Chain Summary

### Key Achievements

1. Unauthenticated access to internal admin tool endpoint
2. Retrieval of 75,000+ error logs with session and PII data
3. Enablement of account takeover via session hijacking

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Steal Web Session Cookie]]
- [[Data from Information Repositories]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Collection]]

---

*Last updated: 2023-10-01T00:00:00Z*
