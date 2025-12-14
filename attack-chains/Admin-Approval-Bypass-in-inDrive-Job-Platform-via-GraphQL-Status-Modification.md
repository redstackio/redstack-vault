---
id: ac-001
tags:
  - auth-bypass
  - graphql
  - web-vulnerability
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2024-01-01T00:00:00Z'
procedures:
  - '[[procedures/Bypass-Admin-Approval-for-Job-Publication]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:47.371Z'
description: >-
  Bypasses mandatory admin approval for publishing job offers on inDrive Job
  platform by intercepting and modifying the GraphQL mutation request to set
  status to ACTIVE instead of MODERATION.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Admin Approval Bypass in inDrive Job Platform via GraphQL Status Modification

Multi-stage attack chain demonstrating a complete attack workflow to bypass admin approval and publish unauthorized job offers on the inDrive Job platform.

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
    A[Create Job Offer in Employer Mode] --> B[Fill Job Details]
    B --> C[Submit for Moderation]
    C --> D[Intercept and Modify GraphQL Request]
    D --> E[Publish Active Job Offer]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web platform: https://injob.indriver.com/
- Required services/ports: HTTPS (443)
- Network access requirements: Direct internet access to the platform

### Initial Access Requirements

- Employer account credentials on inDrive Job platform
- Network position: External attacker with valid session
- Prior access needed: Logged in as employer

## Detailed Attack Procedures

### Step 1: Switch to Employer Mode and Create New Job Offer
procedure: [[procedures/Bypass-Admin-Approval-for-Job-Publication]]

**Objective**: Access the job creation interface to initiate the offer setup.

**Instructions**: Log in to the inDrive Job platform at https://injob.indriver.com/ and switch to employer mode. Navigate to the job creation feature.

**Expected Output**: Job creation form is loaded and ready for input.

**Success Indicators**:
- Employer dashboard accessible
- New job offer creation page opened

### Step 2: Fill in Required Fields for Job Offer
procedure: [[procedures/Bypass-Admin-Approval-for-Job-Publication]]

**Objective**: Complete the job details to trigger the creation process.

**Instructions**: Enter all necessary details such as job title, description, location, and salary into the form. This will prepare the POST request to /api/graphql.

**Expected Output**: Form validation passes, and submission is enabled.

**Success Indicators**:
- All fields populated without errors
- Submission button active

### Step 3: Submit the Job Offer for Pending Approval
procedure: [[procedures/Bypass-Admin-Approval-for-Job-Publication]]

**Objective**: Send the initial request that sets the status to MODERATION.

**Instructions**: Submit the form, which sends a POST request to /api/graphql with the vacancy status set to 'MODERATION'. The offer should now appear as 'Pending Approval'.

**Expected Output**: Confirmation of submission with pending status.

**Success Indicators**:
- Job offer listed as pending
- No immediate publication

### Step 4: Intercept and Modify the UpdateVacancyStatus Request
procedure: [[procedures/Bypass-Admin-Approval-for-Job-Publication]]

**Objective**: Use Burp Proxy to alter the status parameter in the GraphQL mutation.

**Instructions**: Configure Burp Suite to intercept traffic from the browser. Replay the intercepted POST request to /api/graphql in Burp Repeater. Modify the JSON payload by changing the 'status' variable from {'status':'MODERATION'} to {'status':'ACTIVE'}.

**Expected Output**: Modified request ready for resending.

**Success Indicators**:
- Payload updated successfully in Repeater
- No syntax errors in JSON

### Step 5: Resend Modified Request to Publish Job Offer
procedure: [[procedures/Bypass-Admin-Approval-for-Job-Publication]]

**Objective**: Bypass approval and make the job offer visible to all users.

**Instructions**: Forward the modified request from Burp Repeater. The server processes it without validation, changing the status to 'ACTIVE'.

**Expected Output**: Job offer published and visible on the platform.

**Success Indicators**:
- Status updated to Active
- Offer appears in public listings without admin review

## Attack Chain Summary

### Key Achievements

1. Successful creation of a job offer in pending status
2. Interception and modification of GraphQL request to bypass authorization
3. Immediate publication of potentially malicious content, enabling scams or platform disruption

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2024-01-01T00:00:00Z*
