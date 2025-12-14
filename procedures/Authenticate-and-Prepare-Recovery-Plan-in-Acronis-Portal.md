---
id: acronis-auth-prepare-001
tags:
  - authentication
  - backup
  - cloud
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:28:28.703Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Authenticate-and-Prepare-Recovery-Plan-in-Acronis-Portal

## Summary

This procedure outlines logging into the Acronis cloud portal, navigating to device management, and configuring a recovery plan within the attacker's own tenant to generate the necessary API parameters for later exploitation.

## Description

In the context of exploiting an IDOR in Acronis backup recovery, this step establishes a legitimate session and creates a recovery plan draft. It requires valid credentials and at least two registered devices. The outcome is a set of API parameters (e.g., machineId, planId) that can be reused in cross-tenant attacks. This is a prerequisite for intercepting and replaying requests to unauthorized machines.

## Requirements

1. Valid Acronis account credentials with access to multiple devices
2. Web browser with proxy support (e.g., configured for Burp Suite)
3. Devices registered in the account with existing backups

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) for portal access
- Monitor login attempts and session creations for anomalous patterns
- Rate-limit recovery plan creations per user/session

## Objectives

1. Establish authenticated session to Acronis API
2. Generate recovery plan parameters for exploitation
3. Verify intra-tenant recovery functionality as a baseline

## Instructions

### Step 1: Login to Portal

**Context**: Authenticate to gain access to the devices section.

Navigate to https://mc-beta-cloud.acronis.com/ and enter credentials.

> Successful login redirects to the dashboard.

### Step 2: Navigate to Devices

**Context**: Access the management interface for registered machines.

Click on the "DEVICES" section in the sidebar.

> Devices list loads, requiring at least two entries.

### Step 3: Select Source Device and Initiate Recovery

**Context**: Choose a backed-up device to start plan creation.

Click on device_1 with backups, then select "Recovery".

> Backup selection UI appears.

### Step 4: Configure Target and Options

**Context**: Set up the plan to trigger API calls.

Select backup source, choose device_2 as target, enable overwrite options, and save draft.

> API calls to /bc/api/ams/recovery/plan_drafts complete successfully.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- authentication
- backup
- cloud
