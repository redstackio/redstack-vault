---
id: acronis-idor-recovery-overwrite-001
tags:
  - idor
  - backup
  - cloud
  - data-destruction
  - cross-tenant
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Privilege Escalation]]'
  - '[[Impact]]'
verified: false
platforms:
  - Web
  - Cloud
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Authenticate-and-Prepare-Recovery-Plan-in-Acronis-Portal]]'
  - '[[procedures/Intercept-Recovery-Plan-API-Requests-with-Burp-Suite]]'
  - '[[procedures/Replay-Recovery-Request-with-Cross-Tenant-Session-Cookie]]'
step_count: 7
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:28.708Z'
description: >-
  An authenticated attacker exploits an IDOR vulnerability in Acronis backup
  recovery to execute recovery plans across tenants, enabling data overwrite and
  deletion on unauthorized machines.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Privilege Escalation]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Cross-Tenant Backup Recovery Overwrite via IDOR in Acronis Cloud

Multi-stage attack chain demonstrating exploitation of an Insecure Direct Object Reference (IDOR) in the Acronis cloud backup recovery functionality. An authenticated user can access and execute recovery plans for machines in other organizations by manipulating API parameters like machine UUID, backup ID, and plan ID without authorization checks, leading to potential data takeover and deletion via overwriting target machines.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 7 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access: Authenticate to Portal] --> B[Discovery: Prepare Recovery Plan]
    B --> C[Execution: Intercept API Requests]
    C --> D[Privilege Escalation: Replay Cross-Tenant Request]
    D --> E[Impact: Execute Overwrite Recovery]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Acronis Backup Cloud portal (https://mc-beta-cloud.acronis.com/ or production equivalent)
- At least two devices registered in the attacker's account with backups available
- Access to a valid session cookie from a target organization/tenant
- Network access to the Acronis API endpoints

### Initial Access Requirements

- Valid credentials for an authenticated Acronis account
- Burp Suite configured as a proxy for intercepting HTTPS traffic
- No prior access to target tenant needed beyond obtaining a session cookie (e.g., via phishing or shared credentials)

## Detailed Attack Procedures

### Step 1: Authenticate to Acronis Portal
procedure: [[procedures/Authenticate-and-Prepare-Recovery-Plan-in-Acronis-Portal]]

**Objective**: Gain authenticated access to the Acronis cloud portal and navigate to device management to prepare for recovery plan creation.

**Instructions**: Open a web browser and navigate to the Acronis portal. Enter valid credentials to log in. Once authenticated, proceed to the devices section to ensure multiple devices are available.

**Expected Output**: Successful login with access to the devices dashboard showing registered machines.

**Success Indicators**:
- Dashboard loads with device list
- No authentication errors

### Step 2: Navigate to Devices and Select Source Device
procedure: [[procedures/Authenticate-and-Prepare-Recovery-Plan-in-Acronis-Portal]]

**Objective**: Identify and select a device with existing backups to use as the source for the recovery plan.

**Instructions**: In the portal, click on the "DEVICES" section. Select a device (device_1) that has backups available by clicking on it.

**Expected Output**: Device details page opens, showing backup history.

**Success Indicators**:
- Device selected with visible backups
- Backup list populated

### Step 3: Initiate Recovery Process
procedure: [[procedures/Authenticate-and-Prepare-Recovery-Plan-in-Acronis-Portal]]

**Objective**: Start the recovery configuration process to trigger API calls for plan creation.

**Instructions**: From the device details, select the recovery option. Choose a backup from device_1 as the source and select another device (device_2) in the same account as the target. Proceed through the UI to configure the recovery plan, including options for overwrite.

**Expected Output**: Recovery configuration wizard advances, generating draft plans via API.

**Success Indicators**:
- UI allows target selection
- Plan draft created without errors

### Step 4: Configure and Finalize Recovery Plan
procedure: [[procedures/Authenticate-and-Prepare-Recovery-Plan-in-Acronis-Portal]]

**Objective**: Complete the recovery setup to capture the necessary API interactions.

**Instructions**: Follow the UI steps to set target location, recovery options (e.g., overwrite existing data), and finalize the plan draft. This triggers API calls to endpoints like /bc/api/ams/recovery/plan_drafts.

**Expected Output**: Plan draft saved, ready for execution.

**Success Indicators**:
- Plan configuration completes
- API responses indicate success (200 OK)

### Step 5: Intercept Recovery Plan Run Request
procedure: [[procedures/Intercept-Recovery-Plan-API-Requests-with-Burp-Suite]]

**Objective**: Capture the critical API request for executing the recovery plan using a proxy tool.

**Instructions**: With Burp Suite proxy active, trigger the run action in the UI. Intercept the POST request to /bc/api/ams/recovery/plan_operations/run?machineId=<uuid> containing planId, machineId, subscriptionId, and operationId in the body.

**Expected Output**: Burp Suite displays the intercepted request with all parameters visible.

**Success Indicators**:
- Request captured in Burp
- Parameters include UUIDs and IDs from own tenant

### Step 6: Modify and Prepare for Replay
procedure: [[procedures/Replay-Recovery-Request-with-Cross-Tenant-Session-Cookie]]

**Objective**: Adjust the request to target a different tenant by swapping session credentials.

**Instructions**: In Burp, copy the intercepted request. Replace the X-Apigw-Session cookie with one obtained from a different organization's session. Ensure machineId and other parameters point to the victim's machine.

**Expected Output**: Modified request ready in Burp Repeater.

**Success Indicators**:
- Cookie updated without syntax errors
- Request parses correctly

### Step 7: Replay and Execute Cross-Tenant Recovery
procedure: [[procedures/Replay-Recovery-Request-with-Cross-Tenant-Session-Cookie]]

**Objective**: Send the modified request to execute the recovery on an unauthorized machine, overwriting data.

**Instructions**: In Burp Repeater, send the modified POST request. Monitor the response for successful execution.

**Expected Output**: API response (200 OK) indicating recovery plan started on target machine.

**Success Indicators**:
- Recovery initiates without authorization denial
- Target machine data begins overwriting (verifiable in Acronis logs or machine state)

## Attack Chain Summary

### Key Achievements

1. Authenticated access to Acronis recovery features
2. Interception and manipulation of API requests bypassing tenant boundaries
3. Execution of destructive recovery plans across organizations, enabling data deletion

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Privilege Escalation]] Privilege Escalation
- [[Impact]] Impact

---
*Last updated: 2023-10-01T00:00:00Z*
