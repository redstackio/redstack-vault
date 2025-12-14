---
tags:
  - siem
  - kibana
  - rule-import
type: procedure
tools:
  - '[[tools/Kibana]]'
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
updated_at: '2025-12-14T17:23:35.968Z'
sub_techniques: []
id: 8eea230d-92f1-4842-81d8-0df07cf76904
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
---

# Import-Malicious-SIEM-Detection-Rule

## Summary

This procedure imports a custom SIEM detection rule into Kibana that references a machine learning job, setting up the environment for prototype pollution exploitation during anomaly processing.

## Description

In Kibana 7.7.0, the SIEM feature allows importing detection rules via JSON exports. This procedure uses a rule configured for ML anomaly detection on the 'linux_anomalous_network_activity_ecs' job, looking back 30 hours. The rule lacks sanitization in bulk_create_ml_signals.ts, enabling subsequent pollution. Requires authenticated access to Kibana SIEM. Expected outcome: Rule ready for enabling, priming the server for RCE.

## Requirements

1. Authenticated session in Kibana with SIEM write permissions
2. Access to Kibana UI on port 5601
3. Pre-prepared JSON rule file referencing the ML job

## Defense

Defensive measures and detection strategies:

- Restrict rule imports to trusted admins
- Validate ML job references and anomaly processing inputs
- Monitor for unusual rule configurations in SIEM logs

## Objectives

1. Deploy a rule that processes unsanitized ML influencers
2. Position for prototype pollution via anomaly evaluation
3. Prepare for RCE without alerting standard defenses

## Instructions

### Step 1: Prepare and Import Rule

**Context**: Create or obtain the JSON rule export and import it via Kibana interface to configure ML-based detection.

**Command** (Kibana UI/API):

Use Kibana SIEM > Rules > Import to upload the JSON, or POST to /api/siem/detection_engine/rules via API.

> The rule JSON includes type: 'machine learning', job ID: 'linux_anomalous_network_activity_ecs', and timeline: 30 hours. Expected output: Success message with rule ID.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Kibana]]

## Tags

- siem
- kibana
- rule-import

