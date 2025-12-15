---
tags:
  - dos-verification
  - impact-assessment
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Endpoint Denial of Service]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 5782147b-8ca1-4269-bdbc-5eff49d0c14a
created_at: '2025-12-14T17:32:01.646Z'
updated_at: '2025-12-14T17:32:01.646Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Observe-and-Verify-DoS-Impact

## Summary

This procedure monitors the Semmle platform's response during the API flood to confirm DoS effects, such as slowdowns or errors, via screencasts or direct observation.

## Description

As the Python script runs, the server experiences increased load from unrestricted calls. Observation through videos or real-time checks reveals unresponsiveness, high latency, or error pages, validating the vulnerability's exploitability for DoS or buffer overflow risks.

## Requirements

1. Running API flood script from previous step
2. Access to platform UI or monitoring tools
3. Video recording software for proof-of-concept

## Defense

Defensive measures and detection strategies:

- Deploy monitoring tools like Prometheus to alert on API load spikes
- Auto-scale resources or implement circuit breakers
- Log and analyze request patterns for abuse

## Objectives

1. Confirm server degradation
2. Document impact for reporting
3. Validate attack success

## Instructions

### Step 1: Monitor Platform Response

**Context**: Check the platform's functionality while the script runs.

Attempt to load pages or make manual API calls; note delays or failures.

> Expected output: Timeouts, 500 errors, or unresponsive endpoints.

### Step 2: Record Proof-of-Concept

**Context**: Capture the impact visually.

Use screen recording software to demonstrate script execution and server effects.

> Expected output: Video showing requests firing and platform crashing.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[impact-observation]]
- [[poc-recording]]
