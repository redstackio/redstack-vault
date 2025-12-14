---
tags:
  - submission
  - non-2fa
  - hackerone
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T12:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:24:47.983Z'
skill_level: basic
impact_level: low
sub_techniques: []
id: b95aaef5-9310-48f6-bed5-9f890e2ee0ad
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Submit-Report-from-Non-2FA-Account

## Summary

This procedure submits a test vulnerability report to a non-restricted HackerOne program using an account without 2FA enabled, creating the artifact for the subsequent transfer bypass.

## Description

Using a standard HackerOne user account lacking 2FA setup, this step targets the 'h1R' program, which has no submission restrictions. The report can be a simple, non-malicious test finding to avoid policy violations. This establishes a valid report that can be transferred, exploiting the lack of retroactive 2FA checks.

## Requirements

1. Non-2FA enabled HackerOne account
2. Access to the 'h1R' program page
3. Basic report details (title, description)

## Defense

Defensive measures and detection strategies:

- Require 2FA for all user accounts upon registration
- Log and review submission patterns from low-security accounts

## Objectives

1. Generate a report in the non-restricted program
2. Confirm submission succeeds without 2FA
3. Obtain report ID for transfer

## Instructions

### Step 1: Log In to Non-2FA Account

**Context**: Switch to the tester account without security setup.

Log in to hackerone.com using the non-2FA account credentials.

### Step 2: Submit Test Report

**Context**: Create and send the report to 'h1R'.

Navigate to the 'h1R' program, click 'Submit Report', fill in details (e.g., title: "Test Vulnerability", description: "Benign test for 2FA bypass research"), and submit.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[submission]]
- [[non-2fa]]
- [[hackerone]]
