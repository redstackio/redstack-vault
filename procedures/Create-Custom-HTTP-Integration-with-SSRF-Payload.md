---
tags:
  - ssrf
  - integration
  - http-endpoint
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:09.129Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 9528ca77-f0c5-41f8-83fb-e62308cf4f92
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create Custom HTTP Integration with SSRF Payload

## Summary

This procedure exploits the lack of URL validation in Helium Console's custom integration feature by configuring an HTTP endpoint to target the AWS instance metadata service, setting up a persistent SSRF vector for internal resource access.

## Description

The 'Add a custom Integration' form on console.helium.com allows users to specify arbitrary HTTP endpoints without validation, permitting internal IPs like 169.254.169.254 (AWS metadata). This configuration associates with device packets, causing the server to proxy requests to private resources upon transmission. The procedure requires admin access and results in a saved integration that can be triggered later, potentially exposing EC2 metadata including IAM roles and user data.

## Requirements

1. Active admin session in Helium Console
2. Access to 'Integrations' tab
3. Knowledge of target internal endpoint (e.g., AWS metadata URL)
4. Unique label for the integration

## Defense

Defensive measures and detection strategies:

- Implement URL allowlisting or regex validation to restrict endpoints to external/public domains
- Log and monitor all integration creations for internal IP references using WAF rules
- Use network segmentation to isolate backend servers from metadata services

## Objectives

1. Create a custom integration pointing to internal AWS metadata
2. Save without validation errors
3. Enable association with devices for triggering

## Instructions

### Step 1: Navigate to Integrations

**Context**: Access the integrations management section from the authenticated dashboard.

Click on the 'Integrations' tab in the organization dashboard.

> The integrations list loads; look for the 'Add Integration' or 'Add Custom HTTP Integration' button.

### Step 2: Configure Endpoint

**Context**: Set the malicious payload in the integration form to target internal resources.

Select 'Add a custom HTTP integration', enter the endpoint URL as `http://169.254.169.254/latest/meta-data`, and choose GET as the method.

> No validation occurs, allowing the internal link; this will proxy requests to AWS metadata when triggered.

### Step 3: Label and Save

**Context**: Finalize the integration for later use.

Assign a label like 'ssrf-test' and submit the form.

> Success: Integration saved and listed; verify the endpoint in the details.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- ssrf
- integration
- http-endpoint
