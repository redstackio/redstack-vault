---
id: proc-setup-grafana-aiven
tags:
  - setup
  - aiven
  - grafana
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:27.788Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Setup-Test-Grafana-Instance-on-Aiven

## Summary

This procedure provisions a test Grafana 8.x instance on the Aiven platform to reproduce the path traversal vulnerability in a controlled environment.

## Description

Access the Aiven console to create and activate a Grafana service. This step is essential for testing the unauthenticated file read exploit in the /public/plugins endpoint. The instance will be publicly accessible, mimicking production setups vulnerable to the issue. Expected outcome is a running Grafana URL ready for exploitation.

## Requirements

1. Aiven account with console access
2. Authentication credentials for Aiven
3. Basic knowledge of cloud service provisioning

## Defense

Defensive measures and detection strategies:

- Monitor Aiven console for unauthorized instance creation
- Use Aiven's access controls and audit logs to restrict service provisioning

## Objectives

1. Create a vulnerable Grafana instance for testing
2. Obtain the public endpoint URL
3. Verify instance readiness

## Instructions

### Step 1: Access Aiven Console

**Context**: Log in to provision the service.

No command needed; navigate to https://console.aiven.io/ and authenticate.

> Successful login grants access to service creation.

### Step 2: Create Grafana Instance

**Context**: Provision a new Grafana 8.x service.

Use the console UI to select Grafana, configure basic settings (e.g., project, region), and create.

> Instance creation initiates; note the service name for URL generation.

### Step 3: Wait for Activation

**Context**: Monitor status until ready.

Refresh the Aiven dashboard to check service status.

> Status changes to 'Running'; copy the Grafana URL for next steps.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- setup
- aiven
- grafana
