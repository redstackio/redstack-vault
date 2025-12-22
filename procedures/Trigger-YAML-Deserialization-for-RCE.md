---
tags:
  - deserialization
  - rce
  - yaml
  - ruby
type: procedure
tools:
  - '[[tools/paper_trail]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T03:46:25.914Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 30ac6f78-2338-4702-9871-174c1410aea9
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
---
# Trigger-YAML-Deserialization-for-RCE

## Summary

This procedure triggers the deserialization of the persisted YAML payload by querying the historic users feature with the crafted email, invoking the paper_trail gem's reify method to execute arbitrary Ruby code on the server.

## Description

The historic users page (/support/historic_users) queries UserVersion records by email and calls reify on matching objects, which deserializes the YAML in the object column without validation. The gadget chain exploits Ruby's YAML parser to invoke system commands via Kernel#system, demonstrating RCE with a sleep delay. This targets Rails apps using paper_trail for versioning.

## Requirements

1. Malicious record persisted in user_versions table
2. Access to /support/historic_users endpoint
3. Unique trigger email known

## Defense

Defensive measures and detection strategies:

- Enable YAML safe deserialization (YAML.safe_load)
- Validate and sanitize audit table data on write
- Implement WAF rules for anomalous historic_users queries
- Monitor for long-running requests or 500 errors post-delay

## Objectives

1. Query the vulnerable endpoint to load the payload
2. Execute the deserialization gadget chain
3. Confirm RCE via observable effects like delays or errors

## Instructions

### Step 1: Navigate to Historic Users

**Context**: Access the feature that triggers UserVersion queries.

Visit http://localhost:8080/support/historic_users.

> Page loads with input for historic_user_input.

### Step 2: Submit Trigger Email

**Context**: Input the email to match and reify the injected record.

Enter 'uniquekeywordtotriggercode@hackerone.com' in the historic_user_input field and submit.

> The app queries by email, deserializes the object YAML, executes sleep 600, causing 600s hang then 500 error.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/paper_trail]]

## Tags

- deserialization
- rce
- yaml
- ruby
