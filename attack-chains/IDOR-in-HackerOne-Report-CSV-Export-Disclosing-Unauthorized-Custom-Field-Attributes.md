---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - idor
  - hackerone
  - csv-export
  - custom-fields
  - disclosure
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Exploit-IDOR-in-HackerOne-Report-CSV-Export]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:34.529Z'
description: >-
  An Insecure Direct Object Reference vulnerability in the HackerOne platform's
  Report CSV export feature that discloses custom field attribute IDs from
  unauthorized programs by mixing authorized and unauthorized report IDs in the
  export request.
skill_level: intermediate
impact_level: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# IDOR in HackerOne Report CSV Export Disclosing Unauthorized Custom Field Attributes

Multi-stage attack chain demonstrating a complete attack workflow targeting the HackerOne platform's report export feature.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~2 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Submit Mixed Report IDs to CSV Export] --> B[Analyze CSV Header for Disclosed Attributes]

    style A fill:#e74c3c
    style B fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]

### Target Environment

- HackerOne platform (web application)
- Required services/ports: HTTPS on port 443
- Network access requirements: Authenticated access to HackerOne with at least one authorized program

### Initial Access Requirements

- Valid HackerOne user credentials with access to at least one program
- Network position: Direct internet access to hackerone.com
- Prior access needed: Logged-in session (cookies or API token)

## Detailed Attack Procedures

### Step 1: Submit Export Request with Mixed Report IDs
procedure: [[procedures/Exploit-IDOR-in-HackerOne-Report-CSV-Export]]

**Objective**: Trigger the IDOR by sending a POST request to the /reports/export endpoint with a mix of authorized and unauthorized report IDs, causing the CSV header to include custom field attributes from the unauthorized program.

**Instructions**: Authenticate to HackerOne and identify an authorized report ID (e.g., 17 from your program) and an unauthorized one (e.g., 118 from another program). Use [[commands/curl-hackerone-csv-export-idor]] to submit the request:

```bash
curl -X POST 'https://hackerone.com/reports/export' \
  -H 'Cookie: your_session_cookie' \
  -F 'report_ids[] = 17' \
  -F 'report_ids[] = 118' \
  --output exported.csv
```

Download and inspect the generated CSV file for headers like custom_field_1 through custom_field_6, noting any attributes (e.g., custom_field_5) that belong to the unauthorized program.

**Expected Output**: A CSV file with headers revealing custom field IDs from unauthorized programs, such as "custom_field_5" indicating attributes not accessible via normal means.

**Success Indicators**:
- CSV headers include unexpected custom field names
- Attribute IDs from unauthorized programs are present, allowing inference of report structures

## Attack Chain Summary

### Key Achievements

1. Successful disclosure of custom field attribute IDs for unauthorized HackerOne programs
2. Demonstration of IDOR bypassing authorization checks in the CSV export process
3. Potential for inferring report counts and structures without direct access

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T12:00:00Z*
