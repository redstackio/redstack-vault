---
tags:
  - setup
  - configuration
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 50e7c219-1569-43ce-834a-9ad1a418ecf7
created_at: '2025-12-14T17:28:28.728Z'
updated_at: '2025-12-14T17:28:28.728Z'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Setup-IntenseDebate-Site-and-Enable-Reporting

## Summary

This procedure outlines the steps to create a test site on IntenseDebate.com and configure the comment reporting feature with a low threshold, setting up the environment for exploiting the lack of rate limiting to enable comment deletion via spam reports.

## Description

IntenseDebate is a commenting platform integrated into websites. The vulnerability stems from no rate limits on report submissions, allowing quick threshold achievement. This procedure involves logging in, installing a site, and enabling the report button with a configurable deletion threshold (e.g., 10 reports). Prerequisites include a valid account; the process targets the web interface and prepares for subsequent abuse steps. Expected outcome: A configured site ready for comment posting and reporting.

## Requirements

1. Valid IntenseDebate account with login credentials
2. Web browser with JavaScript enabled
3. Internet access to https://intensedebate.com

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on report endpoints (e.g., max 5 reports per IP/account per hour)
- Require CAPTCHA or multi-factor for repeated reports
- Monitor for anomalous report volumes from single sources
- Audit moderation logs for spam patterns

## Objectives

1. Establish a controlled test environment mimicking a vulnerable site
2. Activate the report feature to expose the rate limiting flaw
3. Prepare for demonstration of unauthorized deletion

## Instructions

### Step 1: Login to IntenseDebate

**Context**: Gain access to the platform dashboard to initiate site creation.

Navigate to https://intensedebate.com and enter credentials to log in.

> Successful login redirects to the user dashboard.

### Step 2: Create New Site

**Context**: Set up a test site to apply moderation settings.

Go to https://intensedebate.com/install, follow installation prompts (e.g., enter site URL, name), and complete setup.

> Site creation confirmation appears, with integration code provided.

### Step 3: Access Moderation Settings

**Context**: Navigate to configure comment reporting.

From the dashboard at https://www.intensedebate.com/user-dashboard, click 'Moderate', then 'Comments'.

> Moderation interface loads with settings options.

### Step 4: Enable Report Feature and Set Threshold

**Context**: Activate vulnerability by enabling reports with low threshold.

Check 'Enable "Report this comment" button', set deletion threshold to 10, and save.

> Settings saved message confirms changes; report button now active on site.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[setup]]
- [[configuration]]
- [[web]]
