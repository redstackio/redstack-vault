---
tags:
  - idor
  - improper-authorization
  - data-exposure
  - pii-leak
  - api-vulnerability
type: attack_chain
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Verify-Unuthenticated-Access-to-Target-Site]]'
  - '[[procedures/Access-User-Data-via-ID]]'
  - '[[procedures/Brute-Force-User-Enumeration-via-Incremental-IDs]]'
  - '[[procedures/Fetch-User-Data-via-Curl-with-ID]]'
  - '[[procedures/Access-User-Data-via-Email-Lookup]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:29:19.879Z'
description: >-
  Multi-stage attack exploiting improper authorization and IDOR in the
  tmss.gsa.gov API to unauthenticatedly access and enumerate sensitive PII of
  all 4800 registered users via incremental IDs or emails.
skill_level: beginner
impact_level: high
id: e3783672-347e-4d6d-9d9b-29db70e48d3d
validated: true
mitre_tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
---
# Unauthenticated IDOR in Customer Registration API Leading to Full User Data Exposure

Multi-stage attack chain demonstrating exploitation of improper authorization and insecure direct object references (IDOR) in the /tmssserver/api/public/customerregistration endpoint on tmss.gsa.gov, allowing unauthenticated access to sensitive user registration data including emails, phone numbers, full names, addresses, and secret questions for approximately 4800 users.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Verify Unauthenticated Access] --> B[Access Specific User by ID]
    B --> C[Fetch via Curl for Verification]
    C --> D[Brute-Force All IDs]
    D --> E[Access via Email Lookup]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]

### Target Environment

- Web platform
- Accessible via public internet (https://tmss.gsa.gov)
- No specific ports beyond standard HTTPS (443)

### Initial Access Requirements

- No credentials required
- Direct network access to the target domain
- No prior access needed; fully unauthenticated

## Detailed Attack Procedures

### Step 1: Verify Unauthenticated Access
procedure: [[procedures/Verify-Unauthenticated-Access-to-Target-Site]]

**Objective**: Confirm the target site allows unauthenticated browsing to establish baseline access without login.

**Instructions**: Navigate to the main site using a browser or tool, ensuring no authentication cookies or tokens are present.

**Expected Output**: Successful page load without redirects to login or authentication prompts.

**Success Indicators**:
- Site loads without requiring credentials
- No authentication headers in requests

### Step 2: Access User Data via ID
procedure: [[procedures/Access-User-Data-via-ID]]

**Objective**: Directly access the vulnerable API endpoint using a specific user ID to retrieve sensitive data.

**Instructions**: Browse to the endpoint with an arbitrary ID, such as https://tmss.gsa.gov/tmssserver/api/public/customerregistration/4750/userId/.

**Expected Output**: JSON response containing user details like email, full name, and phone number.

**Success Indicators**:
- JSON data returned without authentication
- Sensitive fields (e.g., email, phone) visible

### Step 3: Fetch User Data via Curl with ID
procedure: [[procedures/Fetch-User-Data-via-Curl-with-ID]]

**Objective**: Use curl to programmatically fetch and verify user data for a specific ID, simulating automated access.

**Instructions**: Execute [[commands/curl-fetch-user-by-id]] to GET the endpoint:

```bash
curl "https://tmss.gsa.gov/tmssserver/api/public/customerregistration/4750/userId/"
```

**Expected Output**: JSON with user registration details.

**Success Indicators**:
- Response status 200
- PII fields populated in output

### Step 4: Brute-Force User Enumeration via Incremental IDs
procedure: [[procedures/Brute-Force-User-Enumeration-via-Incremental-IDs]]

**Objective**: Enumerate all user data by iterating through sequential IDs from 0 to 4800.

**Instructions**: Script or manually loop through IDs in the endpoint https://tmss.gsa.gov/tmssserver/api/public/customerregistration/:id/userId/, collecting responses.

**Expected Output**: Comprehensive dataset of all 4800 users' PII.

**Success Indicators**:
- Successful responses for most IDs
- Full enumeration without rate limits blocking

### Step 5: Access User Data via Email Lookup
procedure: [[procedures/Access-User-Data-via-Email-Lookup]]

**Objective**: Demonstrate alternative access using email as identifier, confirming broad exposure including pending registrations.

**Instructions**: Use [[commands/curl-fetch-user-by-email]] to query by email:

```bash
curl "https://tmss.gsa.gov/tmssserver/api/public/customerregistration/alexandrio+1@wearehackerone.com/emailId/"
```

**Expected Output**: JSON with full user details including registration status.

**Success Indicators**:
- Data returned for specified email
- Includes unapproved/pending user info

## Attack Chain Summary

### Key Achievements

1. Confirmed unauthenticated access to sensitive API
2. Retrieved individual user PII via ID and email
3. Enabled full enumeration of 4800 users' data

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Account Discovery]]

### MITRE ATT&CK Tactics

- [[Discovery]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
