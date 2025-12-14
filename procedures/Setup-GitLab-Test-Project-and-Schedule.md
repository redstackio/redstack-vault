---
id: proc-setup-gitlab-test-001
name: Setup-GitLab-Test-Project-and-Schedule
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:09.684Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Valid Accounts]]'
sub_techniques: []
tags:
  - gitlab
  - setup
  - pipeline
platforms:
  - Web
  - GitLab
commands: []
tools: []
skill_level: intermediate
impact_level: low
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---

# Setup-GitLab-Test-Project-and-Schedule

## Summary

This procedure sets up a test GitLab project and pipeline schedule with custom variables containing sensitive data, simulating a vulnerable environment for demonstrating information disclosure in the API.

## Description

In a GitLab instance, create a new project and configure a pipeline schedule that includes custom variables (e.g., secrets like API keys or deployment tokens). These variables are intended to be accessible only by project owners and maintainers, but the vulnerability allows broader exposure. This setup is essential for testing the API endpoint's access controls. Prerequisites include a GitLab account with create permissions.

## Requirements

1. GitLab account with developer or higher role
2. Access to GitLab UI (web browser)
3. No special tools required beyond standard web access

## Defense

Defensive measures and detection strategies:

- Restrict pipeline schedule creation to trusted roles only
- Monitor API access logs for anomalous requests to pipeline endpoints
- Use variable masking and encryption where possible

## Objectives

1. Establish a reproducible test environment with sensitive variables
2. Verify schedule configuration before exploitation
3. Prepare for API testing without alerting production systems

## Instructions

### Step 1: Create Test Project

**Context**: Log in to GitLab and create a new project to host the pipeline schedule.

No command required; use GitLab UI:

1. Navigate to https://gitlab.com/projects/new
2. Name the project 'trigg' and create it (note the project ID: 20618145)

> Expected output: Project dashboard loads with ID visible in URL or settings.

### Step 2: Configure Pipeline Schedule with Variables

**Context**: Add a pipeline schedule to the project and include custom variables that simulate secrets.

No command required; use GitLab UI:

1. Go to CI/CD > Schedules in the project
2. Click 'New schedule'
3. Set schedule details (e.g., cron: * * * * *) and ID (69918)
4. Add variables: Key=VAR1, Value=secretvalue (unmasked for testing)
5. Save the schedule

> Expected output: Schedule listed as active with variables attached.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[gitlab]]
- [[setup]]
- [[pipeline]]
