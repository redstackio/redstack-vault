---
tags:
  - information-disclosure
  - api
  - pii
  - unauthenticated-access
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Access-Unprotected-API-to-Retrieve-User-PII]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:20.915Z'
description: >-
  An attack chain exploiting an information disclosure vulnerability in an
  unauthenticated API endpoint on Uber's campus-vtc.com, leading to the exposure
  of PII for 83 Uber France contest participants.
skill_level: beginner
impact_level: high
id: dddbab9c-fea3-4d2f-857e-09b0db9a10d8
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Information Disclosure via Unauthenticated API Endpoint on Uber Campus-VTC

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via API Exploration] --> B[Data Exfiltration]

    style A fill:#e74c3c
    style B fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard HTTP client like curl or browser)

### Target Environment

- Web platform
- API endpoint on campus-vtc.com
- No specific ports or services required beyond HTTP/HTTPS

### Initial Access Requirements

- Internet access to the public-facing site
- No credentials needed due to lack of authentication
- Basic knowledge of API interaction

## Detailed Attack Procedures

### Step 1: API Endpoint Access and Data Retrieval
procedure: [[procedures/Access-Unprotected-API-to-Retrieve-User-PII]]

**Objective**: Gain unauthorized access to the API endpoint to retrieve sensitive PII of contest participants, including full names, emails, and phone numbers.

**Instructions**: Explore the site's API through bug bounty hunting or direct interaction. Use a tool like curl to send a request to the vulnerable endpoint without authentication. For example, identify the endpoint handling contest entries (e.g., via JavaScript analysis or trial-and-error) and issue a GET request:

```bash
curl -X GET "https://campus-vtc.com/api/contest-entries" -H "User-Agent: Mozilla/5.0"
```

This retrieves a JSON response containing the PII of approximately 83 users.

**Expected Output**: JSON array with user data, e.g., {"users": [{"name": "John Doe", "email": "john@example.com", "phone": "+1234567890"}, ...]}.

**Success Indicators**:
- Response contains full names, personal emails, and phone numbers without requiring login
- No error messages indicating authentication failure
- Data for 83+ users exposed

## Attack Chain Summary

### Key Achievements

1. Unauthorized retrieval of PII for 83 Uber France users
2. Demonstration of missing access controls on API endpoint
3. Potential for privacy breaches and further social engineering

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
