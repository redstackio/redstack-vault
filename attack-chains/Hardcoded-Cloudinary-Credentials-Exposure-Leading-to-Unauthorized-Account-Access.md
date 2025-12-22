---
tags:
  - hardcoded-credentials
  - cloudinary
  - android
  - api-exposure
  - credential-access
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/cloudinary-usage-api-call]]'
platforms:
  - Android
  - Cloud
complexity: medium
procedures:
  - '[[procedures/Extract-Hardcoded-Credentials-from-Android-App]]'
  - '[[procedures/Authenticate-to-Cloudinary-Using-Extracted-Credentials]]'
  - '[[procedures/Access-Uploaded-Resources-in-Cloudinary]]'
  - '[[procedures/Retrieve-Cloudinary-Account-Usage-Statistics]]'
step_count: 4
techniques:
  - '[[Cloud Instance Metadata API]]'
  - '[[File and Directory Discovery]]'
  - '[[Valid Accounts]]'
description: >-
  Attack chain exploiting hardcoded Cloudinary API credentials in the Reverb.com
  Android app to gain unauthorized access to the associated Cloudinary account,
  enabling full control over uploaded files and account data.
skill_level: intermediate
impact_level: high
id: a98bcbfb-c722-4eae-aa71-45265079af45
created_at: '2025-12-14T17:32:48.330Z'
updated_at: '2025-12-14T17:32:48.330Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Cloud Instance Metadata API]]'
  - '[[File and Directory Discovery]]'
  - '[[Valid Accounts]]'
---
# Hardcoded Cloudinary Credentials Exposure Leading to Unauthorized Account Access

Multi-stage attack chain demonstrating the exploitation of hardcoded Cloudinary API credentials in the Reverb.com Android app, allowing unauthorized access to sensitive user-uploaded media and account statistics.

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
    A[Extract Credentials from App] --> B[Authenticate to Cloudinary]
    B --> C[Access Uploaded Resources]
    C --> D[Retrieve Account Usage]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Android decompiler (e.g., APKTool or Jadx)
- Web browser or API client (e.g., curl, Postman)

### Target Environment

- Reverb.com Android app (APK file)
- Internet access to Cloudinary API
- No specific ports required beyond standard HTTPS (443)

### Initial Access Requirements

- Download the Reverb.com Android APK
- Basic authentication knowledge for API endpoints
- No prior network position needed; client-side analysis

## Detailed Attack Procedures

### Step 1: Extract Credentials from App
procedure: [[procedures/Extract-Hardcoded-Credentials-from-Android-App]]

**Objective**: Decompile the Android app to locate and extract the hardcoded Cloudinary credentials.

**Instructions**: Obtain the Reverb.com APK and use a decompiler like Jadx to inspect the source code. Search for Cloudinary configuration in files such as CloudinaryFacade.java.

**Expected Output**: Configuration string revealing cloud_name ('reverb'), api_key ('434762629765715'), and api_secret (partially redacted).

**Success Indicators**:
- Credentials string found: 'cloudinary://434762629765715:█████@reverb'
- All components (cloud_name, api_key, api_secret) extracted

### Step 2: Authenticate to Cloudinary
procedure: [[procedures/Authenticate-to-Cloudinary-Using-Extracted-Credentials]]

**Objective**: Use the extracted credentials to authenticate and gain access to the Cloudinary account dashboard.

**Instructions**: Input the api_key and api_secret into an API client or browser for basic authentication against the Cloudinary API.

**Expected Output**: Successful login to the Reverb Cloudinary account dashboard.

**Success Indicators**:
- Dashboard access granted without errors
- Account details visible for 'reverb' cloud_name

### Step 3: Access Uploaded Resources
procedure: [[procedures/Access-Uploaded-Resources-in-Cloudinary]]

**Objective**: List, view, and manipulate (replace/delete) all uploaded files in the Cloudinary account.

**Instructions**: Once authenticated, navigate to the resources section in the dashboard or use API endpoints to query uploads.

**Expected Output**: List of all uploads associated with 'reverb', including sensitive user media from Reverb.com.

**Success Indicators**:
- Full list of resources retrievable
- Ability to view or download individual files
- Permissions to replace or delete uploads confirmed

### Step 4: Retrieve Account Usage Statistics
procedure: [[procedures/Retrieve-Cloudinary-Account-Usage-Statistics]]

**Objective**: Query the Cloudinary API to obtain account usage metrics, demonstrating data exfiltration.

**Instructions**: Execute the usage API call using the authenticated credentials via [[commands/cloudinary-usage-api-call]]:

```bash
curl -u '434762629765715:█████' https://api.cloudinary.com/v1_1/reverb/usage
```

**Expected Output**: JSON response with usage data, e.g., {"requests":1894689201,"resources":36029794,"derived_resources":256178843}.

**Success Indicators**:
- API returns valid JSON without authentication errors
- Usage statistics match expected account activity

## Attack Chain Summary

### Key Achievements

1. Exposed hardcoded credentials in client-side Android code, violating secure practices.
2. Gained full unauthorized access to Cloudinary account, compromising user-uploaded media.
3. Demonstrated potential for data exfiltration and account manipulation.
4. Highlighted risks of including API secrets in mobile apps.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Cloud Instance Metadata API]]
- [[File and Directory Discovery]]
- [[Valid Accounts]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---

*Last updated: 2023-10-01T00:00:00Z*
