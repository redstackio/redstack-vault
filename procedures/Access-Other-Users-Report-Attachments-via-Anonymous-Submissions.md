---
id: ddb09130-41b8-4d7d-bc3c-b229924695fd
name: Access Other Users Report Attachments via Anonymous Submissions
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T03:47:39.297Z'
updated_at: '2025-12-11T03:47:39.297Z'
tactics:
  - '[[Privilege Escalation]]'
techniques:
  - '[[Cloud Service Dashboard]]'
sub_techniques: []
tags:
  - idor
  - access-control
  - hackerone
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[TA0004]]'
mitre_techniques:
  - '[[T1538]]'
---

# Access Other Users Report Attachments via Anonymous Submissions

## Summary

This procedure exploits an IDOR vulnerability in HackerOne's report drafting system to access and steal attachments from other users' drafts via anonymous submissions.

## Description

When submitting anonymously with the tracer parameter omitted, the system falls back to nil and loads drafts from authenticated users in the same program, allowing improper access. This occurs in the Interactors::Reports::Create module on the Ruby on Rails backend. Successful execution enables theft of sensitive attachments.

## Requirements

1. Access to the HackerOne submission endpoint
2. Ability to perform anonymous submissions
3. Web browser or HTTP client

## Defense

Defensive measures and detection strategies:

- Enforce proper tracer validation and access controls
- Log and alert on anonymous accesses to draft data

## Objectives

1. Access unauthorized report drafts
2. Retrieve attachments from other users
3. Demonstrate data exposure

## Instructions

### Step 1: Prepare Anonymous Submission

**Context**: Set up a submission without authentication or tracer.

Omit the tracer parameter in the request to the embedded submission endpoint.

### Step 2: Trigger Draft Loading

**Context**: Cause the system to load incorrect drafts due to nil fallback.

Submit the form anonymously, observing the loading of other users' drafts for the program.

### Step 3: Access Attachments

**Context**: Retrieve and download the exposed attachments.

Navigate or request the attachments from the loaded drafts.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Cloud Service Dashboard]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- #idor
- #access-control
