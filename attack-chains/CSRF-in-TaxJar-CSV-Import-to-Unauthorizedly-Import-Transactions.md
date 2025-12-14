---
id: ac-uuid-12345
tags:
  - csrf
  - web-vulnerability
  - aws-s3
  - data-import
  - taxjar
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
  - AWS
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-Attacker-and-Victim-Accounts]]'
  - '[[procedures/Upload-CSV-and-Intercept-S3-Request]]'
  - '[[procedures/Drop-S3-Upload-Response]]'
  - '[[procedures/Craft-CSRF-Payload-Form]]'
  - '[[procedures/Deliver-and-Execute-CSRF-Payload]]'
  - '[[procedures/Verify-Unauthorized-CSV-Import]]'
step_count: 6
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:43.203Z'
description: >-
  A multi-stage CSRF attack exploiting the lack of protection on TaxJar's CSV
  import completion endpoint to import arbitrary transaction data into a
  victim's account via an intercepted S3 upload.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# CSRF in TaxJar CSV Import to Unauthorizedly Import Transactions

Multi-stage attack chain demonstrating a complete CSRF workflow on Stripe's TaxJar service, allowing unauthorized CSV transaction imports that can disrupt tax data.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 6 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Account Setup] --> B[Upload and Intercept]
    B --> C[Drop Response]
    C --> D[Craft Payload]
    D --> E[Deliver CSRF]
    E --> F[Verify Import]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#9b59b6
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web application: app.taxjar.com
- Cloud services: AWS S3 (taxjar-prod-bucket)
- Required services/ports: HTTPS (443)
- Network access requirements: Internet access to TaxJar and ability to host a malicious page

### Initial Access Requirements

- No prior credentials needed beyond creating free TaxJar accounts
- Attacker must be able to intercept traffic (e.g., via proxy)
- Victim must be authenticated in TaxJar

## Detailed Attack Procedures

### Step 1: Account Setup
procedure: [[procedures/Create-Attacker-and-Victim-Accounts]]

**Objective**: Establish attacker and victim personas to simulate the attack scenario.

**Instructions**: Register two separate accounts on app.taxjar.com, one for the attacker and one for the victim (e.g., named Alex).

**Expected Output**: Two active TaxJar accounts ready for testing.

**Success Indicators**:
- Attacker account logged in successfully
- Victim account created and accessible

### Step 2: Upload and Intercept
procedure: [[procedures/Upload-CSV-and-Intercept-S3-Request]]

**Objective**: Initiate a CSV upload from the attacker's account to capture S3 upload details.

**Instructions**: Log in as attacker, navigate to the CSV import feature, select a malicious CSV file with transaction data, and submit the form while intercepting the request using Burp Suite.

**Expected Output**: Intercepted POST request to taxjar-prod-bucket.s3.amazonaws.com with multipart/form-data including key, policy, and file content.

**Success Indicators**:
- Request intercepted showing S3 parameters
- CSV file prepared with arbitrary transaction data

### Step 3: Drop Response
procedure: [[procedures/Drop-S3-Upload-Response]]

**Objective**: Prevent the upload from completing in the attacker's account to reuse the file for CSRF.

**Instructions**: In Burp Suite, drop the HTTP response to the S3 upload request, which would normally be a 303 redirect to the upload_complete endpoint.

**Expected Output**: No import occurs in attacker's account; redirect URL parameters (bucket, key, etag) captured manually.

**Success Indicators**:
- Response dropped successfully
- Parameters like bucket=taxjar-prod-bucket, key=uploads/{uuid}/{filename}, etag="{etag}" extracted

### Step 4: Craft Payload
procedure: [[procedures/Craft-CSRF-Payload-Form]]

**Objective**: Build a malicious HTML form that submits the captured parameters to the vulnerable endpoint.

**Instructions**: Create an HTML page with a form using GET method targeting https://app.taxjar.com/csv_imports/upload_complete, including hidden inputs for bucket, key, and etag from the intercepted response. Auto-submit the form using JavaScript.

**Expected Output**: Malicious HTML file ready to host.

**Success Indicators**:
- Form HTML validates and submits correctly when tested
- Parameters correctly embedded

### Step 5: Deliver and Execute
procedure: [[procedures/Deliver-and-Execute-CSRF-Payload]]

**Objective**: Trick the victim into loading and submitting the CSRF form while authenticated.

**Instructions**: Host the malicious HTML page on a server accessible to the victim (e.g., via ngrok or local server). Have the victim (logged in as Alex) visit the page, triggering automatic form submission.

**Expected Output**: GET request sent to upload_complete endpoint, processing the S3 file import.

**Success Indicators**:
- Victim's browser submits the form
- No user interaction required beyond visiting the page

### Step 6: Verify Import
procedure: [[procedures/Verify-Unauthorized-CSV-Import]]

**Objective**: Confirm the malicious CSV data has been imported into the victim's account.

**Instructions**: Log in to the victim's TaxJar account and check the transaction imports section for the attacker's CSV data.

**Expected Output**: Unauthorized transactions from the CSV visible in the victim's dashboard.

**Success Indicators**:
- CSV transactions imported without victim consent
- Potential data disruption observed

## Attack Chain Summary

### Key Achievements

1. Exploited CSRF on GET-based upload completion to bypass authentication checks
2. Reused S3-uploaded file across accounts via intercepted parameters
3. Demonstrated data pollution in tax calculation service

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
