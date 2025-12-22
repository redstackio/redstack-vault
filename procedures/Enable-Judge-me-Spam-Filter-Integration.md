---
tags:
  - judge.me
  - spam-filter
  - integration
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
updated_at: '2025-12-14T17:23:42.554Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 77e74621-7012-4411-acbe-be31f6fe4908
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Enable-Judge-me-Spam-Filter-Integration

## Summary

This procedure activates the Web Reviews Spam Filter in Judge.me, integrating a third-party spam detection service vulnerable to Log4Shell, setting the stage for payload injection via review submissions.

## Description

In the context of exploiting CVE-2021-44228, enabling the spam filter ensures that user-submitted review content is forwarded to the partner's logging system, where Log4j processes it without sanitization, allowing JNDI lookups. This is a prerequisite for attacks targeting supply chain dependencies in e-commerce platforms like Judge.me. Expected outcome is the feature toggle, with no direct compromise but enabling downstream exploitation.

## Requirements

1. Valid administrator access to a Judge.me-integrated shop
2. Network connectivity to https://judge.me
3. No additional tools required for this step

## Defense

Defensive measures and detection strategies:

- Disable unnecessary third-party integrations and audit vendors for vulnerabilities like Log4Shell
- Monitor admin settings changes via audit logs
- Use web application firewalls (WAF) to detect anomalous feature enables

## Objectives

1. Activate vulnerable spam detection to route reviews through Log4j-affected service
2. Confirm integration without triggering alerts
3. Prepare for payload submission

## Instructions

### Step 1: Access Admin Settings

**Context**: Log in to the Judge.me dashboard to reach configuration options.

Navigate to https://judge.me/settings?jump_to=web+reviews+spam+filter in your browser.

> This loads the specific settings page for spam filtering.

### Step 2: Enable the Feature

**Context**: Toggle the integration to activate the third-party service.

Locate the "Web Reviews Spam Filter" toggle and switch it to enabled. Save the changes.

> Successful enablement updates the UI to show the feature as active, and reviews will now be processed externally.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[judge.me]]
- [[spam-filter]]
- [[integration]]
