---
tags:
  - aws
  - datazone
  - cloudtrail
  - permission-enumeration
  - logging-bypass
type: attack_chain
tools:
  - '[[tools/AWS-CLI]]'
  - '[[tools/Certificate-Transparency-Monitoring]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/export-aws-profile]]'
  - '[[commands/aws-datazone-list-domains]]'
platforms:
  - AWS
  - Cloud
complexity: medium
procedures:
  - '[[procedures/Monitor-Certificate-Transparency-for-New-AWS-Endpoints]]'
  - '[[procedures/Test-Non-Production-Endpoint-with-Admin-Credentials]]'
  - '[[procedures/Test-Non-Production-Endpoint-with-Limited-Credentials]]'
  - '[[procedures/Scale-Permission-Enumeration-Across-Multiple-Endpoints]]'
step_count: 4
techniques:
  - '[[T1087.004]]'
description: >-
  Attack chain exploiting unlogged non-production API endpoints in AWS Datazone
  to silently enumerate permissions without CloudTrail detection.
skill_level: intermediate
impact_level: medium
id: 6bf5787d-f456-42ae-8440-d7cafb14f2af
created_at: '2025-12-14T17:32:39.252Z'
updated_at: '2025-12-14T17:32:39.252Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[T1087.004]]'
---
# Silent Permission Enumeration via AWS Datazone Non-Production Endpoints

## Overview

This attack chain demonstrates how adversaries can exploit non-production API endpoints for the AWS Datazone service, which fail to log calls to CloudTrail. By monitoring certificate transparency logs for new endpoints and using AWS CLI with varying credential profiles (admin vs. limited permissions), attackers can probe permissions silently, revealing access levels without triggering monitoring alerts. This enables stealthy reconnaissance of compromised credentials, facilitating further compromise in AWS environments. The vulnerability was identified through certificate monitoring and confirmed across multiple endpoints, with medium severity due to information disclosure risks.

## Attack Flow Visualization

```mermaid
graph LR
    A[Monitor Certificate Transparency] --> B[Test with Admin Credentials]
    B --> C[Test with Limited Credentials]
    C --> D[Scale Across Endpoints]
    D --> E[Permission Enumeration Complete]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/AWS-CLI]]
- [[tools/Certificate-Transparency-Monitoring]]

### Target Environment

- AWS Cloud environment with Datazone service
- Access to CloudTrail for verification (or lack thereof)
- Configured AWS credentials with admin and limited permission profiles

### Initial Access Requirements

- Compromised AWS credentials (at least limited permissions)
- Network access to AWS endpoints
- AWS CLI installed and configured

## Detailed Attack Procedures

### Step 1: Discover Non-Production Endpoints

procedure: [[procedures/Monitor-Certificate-Transparency-for-New-AWS-Endpoints]]

**Objective**: Identify newly created non-production API endpoints for AWS Datazone using certificate transparency monitoring to find potential unlogged entry points.

**Instructions**: Use certificate transparency monitoring tools to scan for new SSL/TLS certificates issued for AWS domains, focusing on Datazone-related subdomains created in the past 24 hours.

**Expected Output**: List of potential new endpoints, such as custom URLs for non-prod Datazone APIs.

**Success Indicators**:
- New endpoints detected via certificate logs
- Endpoints match Datazone service patterns

### Step 2: Test Endpoint Accessibility with Admin Credentials

procedure: [[procedures/Test-Non-Production-Endpoint-with-Admin-Credentials]]

**Objective**: Verify the non-production endpoint responds to admin-level calls without detailed logging, confirming basic accessibility.

**Instructions**: Set the AWS profile to admin using [[commands/export-aws-profile]]:

```bash
export AWS_PROFILE=admin
```

Then call the list-domains operation on the non-prod endpoint with [[commands/aws-datazone-list-domains]]:

```bash
aws datazone list-domains --endpoint-url [redacted]
```

**Expected Output**: Generic error like 'Invalid endpoint or operation type' without AccessDenied details.

**Success Indicators**:
- Generic error received
- No CloudTrail log entry for the API call

### Step 3: Enumerate Permissions with Limited Credentials

procedure: [[procedures/Test-Non-Production-Endpoint-with-Limited-Credentials]]

**Objective**: Probe the endpoint with limited credentials to elicit detailed permission denial responses, enabling silent enumeration of access levels.

**Instructions**: Switch to the noperm profile using [[commands/export-aws-profile]]:

```bash
export AWS_PROFILE=noperm
```

Execute the same API call with [[commands/aws-datazone-list-domains]]:

```bash
aws datazone list-domains --endpoint-url [redacted]
```

**Expected Output**: Detailed AccessDeniedException revealing user ARN and unauthorized action, e.g., 'User: arn:aws:sts::[redacted]:assumed-role/noperm/noperm is not authorized to perform: datazone:ListDomains on resource: arn:aws:datazone:us-east-1:[redacted]:domain/*'.

**Success Indicators**:
- Detailed permission denial exposed
- No corresponding CloudTrail log generated

### Step 4: Scale Enumeration Across Multiple Endpoints

procedure: [[procedures/Scale-Permission-Enumeration-Across-Multiple-Endpoints]]

**Objective**: Repeat testing on additional discovered endpoints to confirm consistent silent enumeration behavior and broaden reconnaissance.

**Instructions**: For each additional endpoint (e.g., redacted as ██████████, ████, █████, ████, ████████), alternate between admin and noperm profiles using [[commands/export-aws-profile]] and execute [[commands/aws-datazone-list-domains]] with the respective --endpoint-url.

**Expected Output**: Consistent generic errors for admin and detailed denials for noperm across all tested endpoints, with no CloudTrail logs.

**Success Indicators**:
- Enumeration successful on multiple endpoints
- Behavior uniform, indicating systemic logging gap

## Attack Chain Summary

### Key Achievements

1. Discovered unmonitored non-production endpoints via certificate transparency.
2. Demonstrated silent API calls with admin credentials yielding no logs.
3. Exposed detailed permission info with limited credentials without detection.
4. Scaled testing to confirm vulnerability persistence across endpoints.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[T1087.004]]

### MITRE ATT&CK Tactics

- [[Discovery]]

---

*Last updated: 2023-10-01*
