---
id: ac-uuid-001
tags:
  - idor
  - nextcloud
  - file-sharing
  - api
  - authorization-bypass
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Nextcloud-IDOR-to-Revoke-Shares]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:23.572Z'
description: >-
  An attack chain exploiting an Insecure Direct Object Reference (IDOR)
  vulnerability in Nextcloud's OCS API to allow a shared user or group member to
  revoke access to shared files or folders without owner permission, impacting
  group access.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# IDOR in Nextcloud File Sharing API Allowing Unauthorized Share Revocation

Multi-stage attack chain demonstrating a complete attack workflow exploiting an IDOR in Nextcloud's file sharing API. An administrator shares a file or folder with a user or group, but any recipient can use their own credentials to delete the share via the OCS API, revoking access for all recipients including the entire group, without the owner's knowledge. This disrupts legitimate access and demonstrates privilege escalation in share management.

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
    A[Share Creation by Admin] --> B[Recipient Authentication]
    B --> C[IDOR Exploitation via DELETE API]
    C --> D[Share Revocation Verification]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser or API client (e.g., curl)

### Target Environment

- Nextcloud instance (web platform)
- OCS API enabled
- File sharing service active

### Initial Access Requirements

- Valid shared user or group member credentials
- Access to the shared resource (to obtain share-id)
- Network access to the Nextcloud server

## Detailed Attack Procedures

### Step 1: Admin Shares Resource
procedure: [[procedures/Exploit-Nextcloud-IDOR-to-Revoke-Shares]]

**Objective**: Set up the shared file or folder that will be targeted for revocation.

**Instructions**: As the admin, create a share via the Nextcloud web interface for a file or folder to a specific user or group. This generates a unique share-id.

**Expected Output**: Share created successfully; share-id visible in the sharing interface or API response.

**Success Indicators**:
- Share active and accessible by recipients
- Share-id obtained (e.g., via API query)

### Step 2: Recipient Authenticates and Identifies Share-ID
procedure: [[procedures/Exploit-Nextcloud-IDOR-to-Revoke-Shares]]

**Objective**: Authenticate as the shared user or group member and locate the share-id of the target resource.

**Instructions**: Log in to Nextcloud using the recipient's credentials. Access the sharing interface or query the OCS API to list active shares and note the share-id.

**Expected Output**: List of shares including the target share-id.

**Success Indicators**:
- Successful authentication (valid session cookie and requesttoken)
- Share-id identified for the shared resource

### Step 3: Send DELETE Request to Revoke Share
procedure: [[procedures/Exploit-Nextcloud-IDOR-to-Revoke-Shares]]

**Objective**: Exploit the IDOR by issuing a DELETE request to the shares endpoint using the recipient's credentials, revoking the share without owner authorization.

**Instructions**: Use the recipient's session (cookie and requesttoken) to send a DELETE request to the OCS API endpoint. Execute [[commands/delete-nextcloud-share]] with the obtained share-id:

```bash
curl -X DELETE "https://[your-host]/nextcloud/ocs/v2.php/apps/files_sharing/api/v1/shares/[share-id]?format=json" \
  -H "requesttoken: [token-of-shared-user]" \
  -H "OCS-APIREQUEST: true" \
  -H "Cookie: [cookie-of-shared-user]" \
  -H "X-Requested-With: XMLHttpRequest"
```

**Expected Output**: HTTP 200 OK response with JSON indicating successful deletion of the share.

**Success Indicators**:
- API response confirms share deletion
- No authorization error (IDOR success)

### Step 4: Verify Share Revocation
procedure: [[procedures/Exploit-Nextcloud-IDOR-to-Revoke-Shares]]

**Objective**: Confirm that the share has been disabled for all recipients, including other group members.

**Instructions**: Attempt to access the shared file or folder using another recipient's credentials. Check the sharing interface or API for the resource's availability.

**Expected Output**: Access denied; resource no longer listed as shared.

**Success Indicators**:
- Original recipient and group members lose access
- Owner's storage unaffected, but sharing disrupted

## Attack Chain Summary

### Key Achievements

1. Unauthorized revocation of admin-created shares using recipient credentials
2. Denial of access to shared resources for entire groups
3. Demonstration of IDOR leading to privilege escalation in share management

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---

*Last updated: 2023-10-01T00:00:00Z*
