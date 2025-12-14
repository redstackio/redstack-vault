---
id: ac-uuid-001
tags:
  - authorization-bypass
  - idor
  - pii-leakage
  - web-vulnerability
  - military-pii
type: attack_chain
tools:
  - '[[tools/Curl-HTTP-Client]]'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Discover-Exposed-Administrative-JavaScript-File]]'
  - '[[procedures/Identify-Vulnerable-Endpoint-for-Application-Data]]'
  - '[[procedures/Exploit-Endpoint-to-Retrieve-Specific-Application-Data]]'
  - '[[procedures/Exploit-IDOR-by-Modifying-Parameter-for-Multiple-Access]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:28:59.109Z'
description: >-
  Multi-stage attack exploiting an exposed administrative JavaScript file to
  bypass authorization, identify a vulnerable endpoint, and leverage IDOR to
  access sensitive PII from approximately 50,000 military personnel application
  records.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
  - '[[Account Discovery]]'
---
# Authorization Bypass via Exposed Admin JS Leading to IDOR PII Leakage

Multi-stage attack chain demonstrating a complete workflow from discovering an exposed admin file to exploiting IDOR for mass PII exfiltration in a U.S. Department of Defense application.

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
    A[Discover Exposed Admin JS] --> B[Identify Vulnerable Endpoint]
    B --> C[Exploit Specific Access]
    C --> D[Mass IDOR Exploitation]
    D --> E[PII Leakage]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Curl-HTTP-Client]]

### Target Environment

- Web application platform
- Exposed administrative endpoints without authentication
- Network access to the target URL (e.g., https://target.example.com)

### Initial Access Requirements

- No credentials required due to bypass
- Direct internet access to the public-facing web app
- Basic knowledge of HTTP requests and URL encoding

## Detailed Attack Procedures

### Step 1: Discover Exposed Administrative JavaScript File
procedure: [[procedures/Discover-Exposed-Administrative-JavaScript-File]]

**Objective**: Identify and access the exposed admin.js file to reveal administrative functionality and endpoints.

**Instructions**: Manually test for common administrative file paths or use directory enumeration to locate admin.js. Access the file directly via browser or curl to inspect its contents for endpoint details.

**Expected Output**: JavaScript code exposing an endpoint that returns user application data without auth checks.

**Success Indicators**:
- File accessible at https://████/█████████ without login
- Code reveals POST endpoint for application data

### Step 2: Identify Vulnerable Endpoint for Application Data
procedure: [[procedures/Identify-Vulnerable-Endpoint-for-Application-Data]]

**Objective**: Analyze the exposed JS to pinpoint the exact endpoint and parameter vulnerable to unauthorized access.

**Instructions**: Review the admin.js source for POST request patterns, focusing on the 'url' parameter that specifies application IDs. Confirm no auth headers or checks are present.

**Expected Output**: Endpoint URL (e.g., https://███/███) and parameter details for data retrieval.

**Success Indicators**:
- Endpoint identified with 'url' param accepting application paths
- No authorization validation in code

### Step 3: Exploit Endpoint to Retrieve Specific Application Data
procedure: [[procedures/Exploit-Endpoint-to-Retrieve-Specific-Application-Data]]

**Objective**: Send a targeted POST request to fetch data for a single application, verifying the bypass.

**Instructions**: Use [[commands/curl-post-to-admin-endpoint-for-specific-app]] to send a POST request with a specific 'url' parameter:

```bash
curl https://███/███ -X POST -data="url=%2F████████" -k
```

Validate the response contains PII like names and emails.

**Expected Output**: JSON response with PII for the targeted application.

**Success Indicators**:
- Unauthorized access to specific record
- PII elements (name, phone, email) returned

### Step 4: Exploit IDOR by Modifying Parameter for Multiple Access
procedure: [[procedures/Exploit-IDOR-by-Modifying-Parameter-for-Multiple-Access]]

**Objective**: Iterate over application IDs via the 'url' parameter to exfiltrate data from ~50,000 records.

**Instructions**: Modify the 'url' parameter in successive requests using [[commands/curl-post-to-admin-endpoint-for-idor-exploitation]], e.g., changing to %2F█████ for different IDs up to 60000. Script a loop if needed to automate.

```bash
curl https://███████/███ -X POST -data="url=%2F████████" -k
```

Collect and store responses for analysis.

**Expected Output**: Data for valid IDs (~50,000 accessible); empty or error for invalid like 60000.

**Success Indicators**:
- Access to multiple unrelated applications
- Mass PII collection confirming IDOR

## Attack Chain Summary

### Key Achievements

1. Bypassed authorization via exposed admin.js to access admin endpoints
2. Identified and exploited a POST endpoint lacking auth checks
3. Leveraged IDOR to retrieve PII from 50,000 military personnel records
4. Demonstrated high-impact data leakage without credentials

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Valid Accounts]]
- [[Account Discovery]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Discovery]]
- [[Collection]]

---

*Last updated: 2023-10-01T00:00:00Z*
