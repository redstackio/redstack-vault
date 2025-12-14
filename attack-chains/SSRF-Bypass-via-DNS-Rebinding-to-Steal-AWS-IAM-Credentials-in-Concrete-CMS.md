---
tags:
  - ssrf
  - dns-rebinding
  - aws
  - iam
  - concrete-cms
type: attack_chain
tools:
  - '[[tools/1u-ms]]'
tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
verified: false
platforms:
  - Web
  - AWS
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Identify-Remote-File-Upload-in-Concrete-CMS]]'
  - '[[procedures/Test-SSRF-Mitigations-on-AWS-Metadata]]'
  - '[[procedures/Setup-DNS-Rebinding-Domain]]'
  - '[[procedures/Exploit-SSRF-with-Rebinding-to-Fetch-AWS-Metadata]]'
  - '[[procedures/Retrieve-IAM-Credentials-via-Bypassed-SSRF]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Steal Application Access Token]]'
updated_at: '2025-12-14T04:39:09.907Z'
description: >-
  Multi-stage attack exploiting SSRF in Concrete CMS file upload to bypass IP
  mitigations using DNS rebinding and retrieve AWS IAM credentials.
skill_level: intermediate
impact_level: high
id: 7efbce11-e783-41b0-8bf0-485b58a50331
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Steal Application Access Token]]'
---
# SSRF Bypass via DNS Rebinding to Steal AWS IAM Credentials in Concrete CMS

Multi-stage attack chain demonstrating exploitation of SSRF in Concrete CMS file upload functionality, bypassing IP-based mitigations using DNS rebinding to access AWS Instance Metadata Service and steal IAM credentials.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Identify Upload Feature] --> B[Test Mitigations]
    B --> C[Setup DNS Rebinding]
    C --> D[Exploit SSRF]
    D --> E[Retrieve Credentials]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/1u-ms]]

### Target Environment

- Concrete CMS on AWS EC2 instance
- PHP-based web application
- AWS IAM roles attached to EC2
- Network access to the upload endpoint

### Initial Access Requirements

- Valid user session or public access to file upload feature
- No special credentials needed for initial testing
- Ability to control DNS resolution timing

## Detailed Attack Procedures

### Step 1: Identify Remote File Upload Functionality
procedure: [[procedures/Identify-Remote-File-Upload-in-Concrete-CMS]]

**Objective**: Locate and understand the remote URL fetching capability in the file upload feature.

**Instructions**: Examine the Concrete CMS dashboard or API endpoints for file upload options that support remote URLs. Test by providing an external image URL to confirm the server fetches and processes it.

**Expected Output**: Successful upload of a remote file, confirming SSRF potential.

**Success Indicators**:
- File from external URL is uploaded and displayed
- No immediate blocks on external fetches

### Step 2: Test Direct SSRF Attempts on AWS Metadata
procedure: [[procedures/Test-SSRF-Mitigations-on-AWS-Metadata]]

**Objective**: Verify if direct access to internal AWS endpoints is blocked by mitigations.

**Instructions**: Use the upload feature to attempt fetching from the AWS Instance Metadata Service endpoint, such as `http://169.254.169.254/latest/meta-data/`. Monitor for errors indicating IP verification blocks in backend/file.php.

**Expected Output**: Request blocked with IP validation error.

**Success Indicators**:
- Access denied due to IP checks (lines 794-804 in backend/file.php)
- Confirmation of SSRF mitigation in place

### Step 3: Set Up DNS Rebinding Attack
procedure: [[procedures/Setup-DNS-Rebinding-Domain]]

**Objective**: Create a domain that initially resolves to an external IP and rebinds to the internal AWS metadata IP.

**Instructions**: Register a domain via [[tools/1u-ms]] and configure it to resolve first to a public IP (e.g., 8.8.8.8) for 1 second, then rebind to 169.254.169.254. Test the rebinding locally using `dig` or `nslookup` with timing.

**Expected Output**: Domain resolves to external IP initially, then to internal IP after rebinding period.

**Success Indicators**:
- Successful DNS rebinding confirmed via repeated queries
- No static IP resolution

### Step 4: Exploit SSRF Using Rebinding Domain
procedure: [[procedures/Exploit-SSRF-with-Rebinding-to-Fetch-AWS-Metadata]]

**Objective**: Bypass IP checks by using the rebinding domain in the upload URL to fetch internal metadata.

**Instructions**: Submit the rebinding domain (e.g., `http://rebind-domain.1u.ms/latest/meta-data/`) as the remote URL in the file upload. The server performs initial IP check (passes), then fetches after rebinding (accesses internal endpoint).

**Expected Output**: Server-side fetch of AWS metadata content.

**Success Indicators**:
- Internal content retrieved despite mitigations
- No IP block errors

### Step 5: Retrieve AWS IAM Role and Credentials
procedure: [[procedures/Retrieve-IAM-Credentials-via-Bypassed-SSRF]]

**Objective**: Extract IAM role details and temporary credentials for further compromise.

**Instructions**: Target specific metadata paths like `/latest/meta-data/iam/security-credentials/` using the rebinding URL. Capture the response containing access keys and role ARN.

**Expected Output**: JSON or text with IAM role name, access key ID, secret key, and session token.

**Success Indicators**:
- IAM credentials obtained
- Potential for AWS API enumeration

## Attack Chain Summary

### Key Achievements

1. Identified SSRF in Concrete CMS upload
2. Bypassed IP mitigations with DNS rebinding
3. Accessed AWS metadata to steal IAM credentials
4. Enabled cloud environment compromise

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Steal Application Access Token]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Credential Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
