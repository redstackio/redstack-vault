---
id: ac-ssrf-mixmax-webhook-aws-metadata
tags:
  - ssrf
  - aws
  - ec2
  - metadata
  - webhook
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
verified: false
platforms:
  - Web
  - AWS
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-SSRF-in-Mixmax-Webhook]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:08:48.575Z'
description: >-
  A multi-step attack exploiting SSRF in Mixmax's webhook feature to access and
  enumerate AWS EC2 instance metadata, including network interfaces and MAC
  addresses.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# SSRF via Mixmax Webhook to Access AWS EC2 Metadata

Multi-stage attack chain demonstrating exploitation of SSRF in Mixmax's account webhook feature to force server-side requests to internal AWS EC2 metadata endpoints, enabling verification of accessibility and enumeration of sensitive instance details like MAC addresses.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~120 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Malicious Webhook] --> B[Trigger Webhook via Email]
    B --> C[Observe Response for Accessibility]
    C --> D[Enumerate Internal Metadata]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (manual browser and email interaction)

### Target Environment

- Mixmax web application (https://app.mixmax.com)
- AWS-hosted backend with EC2 instances
- Required services/ports: Web dashboard access (HTTPS/443)
- Network access requirements: Authenticated user account in Mixmax

### Initial Access Requirements

- Valid Mixmax user credentials
- Network position: External internet access
- Prior access needed: Logged-in session to dashboard

## Detailed Attack Procedures

### Step 1: Create Webhook with AWS Metadata URL
procedure: [[procedures/Exploit-SSRF-in-Mixmax-Webhook]]

**Objective**: Configure a webhook in the Mixmax dashboard to point to the AWS EC2 metadata service, bypassing URL validation.

**Instructions**: Log in to the Mixmax dashboard and navigate to the webhook settings. Set the webhook URL to the metadata endpoint.

**Expected Output**: Webhook successfully created without errors.

**Success Indicators**:
- Webhook URL saved in dashboard
- No immediate validation errors

### Step 2: Trigger the Webhook
procedure: [[procedures/Exploit-SSRF-in-Mixmax-Webhook]]

**Objective**: Activate the webhook by simulating an email event to force the server to make the SSRF request.

**Instructions**: Send or receive an email that triggers the webhook processing. Wait for backend handling, which may take hours.

**Expected Output**: Email processed without explicit errors in user interface.

**Success Indicators**:
- Email sent/received successfully
- No user-facing failure notifications

### Step 3: Observe Response Behavior
procedure: [[procedures/Exploit-SSRF-in-Mixmax-Webhook]]

**Objective**: Monitor for failure notifications to confirm the internal endpoint is reachable via SSRF.

**Instructions**: Check email notifications after processing. Compare with tests using blocked URLs like localhost.

**Expected Output**: Absence of failure email for metadata URL, unlike for localhost.

**Success Indicators**:
- No failure notification for http://169.254.169.254/latest/meta-data/
- Failure notification present for http://localhost

### Step 4: Enumerate Additional Endpoints
procedure: [[procedures/Exploit-SSRF-in-Mixmax-Webhook]]

**Objective**: Probe further metadata paths to extract sensitive information like network interfaces and MAC addresses.

**Instructions**: Create additional webhooks with targeted metadata URLs and trigger them similarly. Observe behaviors for successful access.

**Expected Output**: Successful access indicated by lack of failures, allowing enumeration of resources.

**Success Indicators**:
- Access to paths like /latest/meta-data/network/interfaces/macs/
- Enumeration of MAC addresses without errors

## Attack Chain Summary

### Key Achievements

1. Verified SSRF vulnerability allowing access to AWS metadata service
2. Confirmed internal endpoint reachability without blacklisting
3. Enumerated EC2 instance details including network interfaces and MAC addresses

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Reconnaissance]]

---
*Last updated: 2023-10-01T00:00:00Z*
