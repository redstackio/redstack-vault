---
tags:
  - insider-threat
  - valid-accounts
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: low
impact_level: medium
detection_risk: low
sub_techniques: []
id: f0de744d-5de8-4236-b2e7-aca3e147902a
created_at: '2025-12-11T06:10:15.707Z'
updated_at: '2025-12-11T06:10:15.707Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1078]]'
---
# Gain Authorized Access via Employment

## Summary

This procedure involves securing a legitimate job role that provides authorized access to sensitive data, such as vulnerability reports, enabling further misuse without initial suspicion.

## Description

In this insider threat scenario, the attacker gains employment in a triage position at a bug bounty platform, receiving permissions to handle customer disclosures. This access is exploited between specific dates for personal gain. The approach relies on passing hiring processes and using granted credentials.

## Requirements

1. Relevant qualifications for the job role
2. Successful application and hiring process
3. Access to internal platform systems

## Defense

Defensive measures and detection strategies:

- Enhanced background checks and monitoring during hiring
- Role-based access controls with auditing

## Objectives

1. Obtain legitimate access to sensitive data
2. Establish a trusted position within the organization
3. Prepare for data misuse without detection

## Instructions

### Step 1: Apply for Triage Role

**Context**: Submit application for a position involving vulnerability intake and triage.

> Focus on roles with access to customer programs.

### Step 2: Pass Screening and Onboarding

**Context**: Complete interviews, background checks, and training to gain system access.

> Access granted for dates like April 4th to June 23rd, 2022.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[insider-threat]]
- [[valid-accounts]]
