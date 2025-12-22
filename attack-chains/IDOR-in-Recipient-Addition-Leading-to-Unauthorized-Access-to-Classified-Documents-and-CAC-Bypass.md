---
tags:
  - idor
  - auth-bypass
  - dod
  - file-sharing
  - classified-access
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-and-Verify-Test-Package]]'
  - '[[procedures/Exploit-IDOR-for-Arbitrary-Recipient-Addition]]'
  - '[[procedures/Bypass-CAC-Authentication-via-IDOR]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:30.788Z'
description: >-
  Multi-stage attack exploiting Insecure Direct Object Reference (IDOR) in a DoD
  secure file sharing platform to gain unauthorized access to sensitive
  documents and bypass CAC authentication.
skill_level: intermediate
impact_level: high
id: 9d5f1b2a-8377-4b6a-b892-8b622deced69
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
---
# IDOR in Recipient Addition Leading to Unauthorized Access to Classified Documents and CAC Bypass

Multi-stage attack chain demonstrating exploitation of an Insecure Direct Object Reference (IDOR) vulnerability in the ██████████ secure file sharing platform used by the U.S. Department of Defense. The attack allows unauthenticated users to add themselves as recipients to any package, gaining download links to over 500,000 documents including classified FOUO materials and PII/PHI, as well as bypassing Common Access Card (CAC) authentication for protected files.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Test Package] --> B[Exploit IDOR for Recipient Addition]
    B --> C[Access Documents and Bypass CAC]
    C --> D[Exfiltrate Sensitive Data]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web-based secure file sharing platform (█████████ on ASP.NET)
- No specific ports required; standard HTTPS access
- Internet access to the platform's public endpoints

### Initial Access Requirements

- No credentials needed initially; unauthenticated access
- Ability to receive emails for verification
- Network position: External attacker with web access

## Detailed Attack Procedures

### Step 1: Create and Verify Test Package
procedure: [[procedures/Create-and-Verify-Test-Package]]

**Objective**: Establish a baseline package to understand the platform's workflow and prepare for interception.

**Instructions**: Visit the upload page at ████/Default.aspx, select a test file, and upload it to create a new package. Check your email for the verification link and click it to confirm. Then, log in to the status page using the provided password from the email, accessing ███/StatusLogIn.aspx?PackageID=x.

**Expected Output**: Successful package creation with a verifiable PackageID and access to the status page.

**Success Indicators**:
- Verification email received and package confirmed
- Status page accessible with the test PackageID

### Step 2: Exploit IDOR for Arbitrary Recipient Addition
procedure: [[procedures/Exploit-IDOR-for-Arbitrary-Recipient-Addition]]

**Objective**: Intercept and modify requests to add the attacker's email as a recipient to any target package, bypassing ownership checks.

**Instructions**: On the status page, enter your email in the 'Add New Recipient' section. Use Burp Suite to intercept the POST request to /████████/Status.aspx?ID=x. Modify the 'ID' parameter to a target package ID (e.g., 15743188). Forward the request to add yourself to the package. Repeat for multiple IDs to access numerous files.

**Expected Output**: Response indicating successful invitation; email received with download link and password for the targeted package.

**Success Indicators**:
- Modified request succeeds without errors
- Download email arrives for unauthorized package
- Ability to download files from targeted packages

### Step 3: Bypass CAC Authentication via IDOR
procedure: [[procedures/Bypass-CAC-Authentication-via-IDOR]]

**Objective**: Use a mismatched password from a non-CAC file to access CAC-protected files by swapping IDs in the download form.

**Instructions**: Visit a download page like █████/███?id=15745307 with an arbitrary ID. Enter a password from a regular non-CAC file email into the form. Intercept the POST submission with Burp Suite and replace the 'id' parameter with a CAC-protected file's ID. Forward to download the file.

**Expected Output**: File information displays, allowing download without CAC; access to protected content.

**Success Indicators**:
- Download succeeds for CAC-protected file
- No CAC prompt or authentication failure
- File contents retrieved

## Attack Chain Summary

### Key Achievements

1. Unauthorized addition to over 500,000 packages, accessing classified FOUO, PII/PHI documents
2. Metadata exfiltration from 15 million historical documents
3. Complete bypass of CAC authentication for protected files

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Valid Accounts]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
