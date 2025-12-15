---
tags:
  - request-tampering
  - device-update
  - idor
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:36.375Z'
sub_techniques: []
id: 139fc216-0bf9-4603-8dae-7b07ccd98f74
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Tamper-Device-Name-Update-Request-with-Org-ID

## Summary

This procedure intercepts a device name update request from the read-only account, injects the admin's organization ID, and forwards it to bypass authorization and modify a device in the target organization.

## Description

From the read-only session (B), add a new device or select an existing one, then trigger a name update via the web UI. Intercept the resulting POST or PUT request (e.g., to /api/v1/devices/{device_id}) using a proxy. Modify the request body to include the extracted organization ID (e.g., change "organization_id" from B's to A's). The server fails to validate the ID against the user's permissions, allowing the update. Prerequisites: Extracted org ID and proxy setup. Expected outcome: Device name altered in A's organization.

## Requirements

1. Read-only session with device management visibility
2. Extracted organization ID from prior step
3. Proxy tool intercepting traffic

## Defense

Defensive measures and detection strategies:

- Validate user permissions against provided object IDs on every endpoint
- Implement request signing or CSRF tokens to detect tampering
- Audit logs for mismatched org-user pairs in update requests

## Objectives

1. Initiate legitimate device name update in B's context
2. Tamper request with target org ID
3. Successfully update device in admin's organization

## Instructions

### Step 1: Add or Select Device in B's Session

**Context**: Prepare a device for name update to generate the request.

Log in as B, navigate to devices in the invited organization, and add a new device or edit an existing one. Enter a temporary name and prepare to save/update.

> Expected: UI form for device name input.

### Step 2: Intercept Update Request

**Context**: Capture the HTTP request during the update action.

With Burp Suite intercepting, click the update button in the UI. In Burp Interceptor, pause the POST/PUT request (e.g., {"device_id": "dev_456", "name": "New Name", "organization_id": "b_org"}).

> Expected Output: Request body visible for modification.

### Step 3: Inject Organization ID

**Context**: Modify the request to target A's organization.

Edit the request body in Burp Repeater or Inspector: Replace "organization_id" with the extracted value (e.g., "organization_id": "org_123abc"). Ensure other fields remain intact.

> Example modified body: {"device_id": "dev_456", "name": "Tampered Name", "organization_id": "org_123abc"}

### Step 4: Forward Tampered Request

**Context**: Submit the altered request to the server.

Click Forward in Burp; observe the 200 OK response indicating success.

> Expected Output: No permission error; update applied silently.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- request-tampering
- device-update
- idor
