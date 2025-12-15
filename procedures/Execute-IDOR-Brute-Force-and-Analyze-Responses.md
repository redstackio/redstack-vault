---
id: proc-execute-idor-brute-analyze
tags:
  - brute-force
  - pii-disclosure
  - response-analysis
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:34.965Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Execute-IDOR-Brute-Force-and-Analyze-Responses

## Summary

This procedure launches a Burp Intruder attack to brute-force the IDOR parameter in the DoD portal, identifies successful responses via grep matching, and analyzes disclosed PII, extending the exploitation across multiple tabs for comprehensive data leakage.

## Description

With the parameter marked, payloads (numeric 1-9) are injected to test access to other soldiers' records. Grep extraction searches for indicators like 'Primary MOS' to flag hits. The attack targets endpoints like Personnel, ATRRS, and Education/Training by adjusting numerics (e.g., 61, 444, 2001). Outcomes include exposed PII such as SSN fragments, MOS, and training history, confirming critical information disclosure.

## Requirements

1. Configured Intruder from previous procedure
2. Authenticated session active
3. Target URLs for multiple tabs identified
4. Burp Suite with Grep Extract rules set

## Defense

Defensive measures and detection strategies:

- Implement indirect object references (e.g., UUIDs) instead of sequential numerics
- Deploy anomaly detection for repeated requests to dynamicdata endpoints
- Encrypt PII in transit and enforce least-privilege access

## Objectives

1. Brute-force parameter to access unauthorized records
2. Extract and validate PII from responses
3. Scale exploitation to additional data tabs

## Instructions

### Step 1: Configure Payloads and Grep

**Context**: Set numeric payloads and extraction rules for efficient analysis.

In Payloads tab, choose 'Numbers' type: From 1, To 9, Step 1. In Options > Grep - Extract, add 'Primary MOS' as a match string with refetch enabled.

> Payloads generate 9 variations; grep will highlight PII indicators in results.

### Step 2: Launch the Attack

**Context**: Execute brute-force to probe for IDOR successes.

Click 'Start Attack' in Intruder.

> Results table populates with responses; longer ones or grep matches indicate disclosure.

### Step 3: Analyze and Repeat for Tabs

**Context**: Review hits and adapt for other endpoints.

Sort results by length or grep column. For Personnel (61), ATRRS (444), Education (2001), recapture and reconfigure as needed.

> Successful hits show unauthorized PII; repeat yields multi-tab leakage.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[brute-force]]
- [[grep-extract]]
- [[multi-tab-exploitation]]
