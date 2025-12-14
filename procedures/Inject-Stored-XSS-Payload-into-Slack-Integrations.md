---
id: proc-uuid-001
tags:
  - xss
  - stored-xss
  - payload-injection
  - slack
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T03:15:36.180Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Inject-Stored-XSS-Payload-into-Slack-Integrations

## Summary

This procedure involves injecting a malicious payload into Slack's integrations feature on slack.com, exploiting insufficient input sanitization to store cross-site scripting (XSS) code server-side. It sets up the foundation for executing JavaScript in victims' browsers when they view the integration details, potentially leading to data theft or session hijacking.

## Description

In the context of Slack's web application, the integrations feature allows users to create or configure app integrations, including fields for URLs or descriptions. Due to a lack of proper input validation, an attacker can submit a crafted URL payload that includes encoded characters to bypass filters. This payload is stored in the database and later displayed without output encoding, enabling stored XSS. The attack targets authenticated users in the same workspace and requires the attacker to have integration creation permissions. Expected outcomes include persistent storage of the payload, verifiable by checking the integration configuration.

## Requirements

1. Valid Slack account with permissions to create or edit integrations in the target workspace
2. Web browser for accessing slack.com and crafting the payload
3. Knowledge of the vulnerable field (e.g., a URL input in integration setup)

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and validation for all user-supplied data in integrations
- Use output encoding (e.g., HTML entity encoding) when rendering stored data
- Monitor for anomalous integration creations with suspicious URLs
- Enable Content Security Policy (CSP) to restrict JavaScript execution sources

## Objectives

1. Store malicious JavaScript payload server-side without detection
2. Prepare for execution when victims access the integration
3. Enable subsequent data exfiltration or session manipulation

## Instructions

### Step 1: Access Integrations Setup

**Context**: Log in to the target Slack workspace and navigate to the integrations or apps section to begin creating a new integration.

No specific command required; use the web interface to go to https://slack.com/apps or the workspace's integrations menu.

> Upon successful navigation, you should see options to add or manage integrations.

### Step 2: Inject the Payload

**Context**: In the integration creation form, locate a text or URL field (e.g., callback URL or description) and insert the malicious payload to test for storage without sanitization.

Use the following payload in the vulnerable field:

```
http://jeroldcamacho.com/%5Ex1s1s/slack.com.txt
```

> This payload uses URL encoding (%5E for '^', etc.) to evade basic filters and is stored as-is. Submit the form to save the integration. Expected output: Integration created successfully with no validation errors.

### Step 3: Verify Storage

**Context**: Check the saved integration details to confirm the payload is stored unaltered.

Access the integration's configuration page and inspect the field; the payload should appear without modifications.

> If stored correctly, proceed to sharing or viewing to trigger execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
- [[slack]]
