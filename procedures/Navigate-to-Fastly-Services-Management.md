---
id: p-navigate-fastly-services
tags:
  - domain-takeover
  - dashboard-access
type: procedure
tools:
  - '[[tools/Fastly-Management-Dashboard]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:51:10.678Z'
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
# Navigate-to-Fastly-Services-Management

## Summary

This procedure describes logging into Fastly and accessing the services management interface to prepare for creating a service that can claim vulnerable subdomains.

## Description

After account registration, users must log in to reach the core management features. The services page at https://manage.fastly.com/services/all lists all configured services and provides the entry point for new ones. This step is crucial for domain takeover as it positions the attacker to add and control subdomains. No technical commands are needed; it's purely navigational. Expected outcome: Access to the service creation tools.

## Requirements

1. Active Fastly account
2. Web browser session
3. Login credentials from registration

## Defense

Defensive measures and detection strategies:

- Enforce multi-factor authentication on CDN provider accounts
- Log and monitor dashboard access patterns for unusual activity
- Use API rate limiting to prevent rapid service creations

## Objectives

1. Authenticate and enter the management dashboard
2. Locate the services interface
3. Prepare for service and domain configuration

## Instructions

### Step 1: Log In to Fastly

**Context**: Authenticate to gain dashboard access.

Go to https://manage.fastly.com and enter your email and password to log in.

### Step 2: Direct Navigation

**Context**: Reach the services management area.

Once logged in, append /services/all to the URL or click the 'Services' menu to load https://manage.fastly.com/services/all.

**Expected Output**: Page showing service list with a 'Create Service' button.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Fastly-Management-Dashboard]]

## Tags

- [[domain-takeover]]
- [[dashboard-access]]
