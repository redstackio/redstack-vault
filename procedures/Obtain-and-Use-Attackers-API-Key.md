---
tags:
  - api-key
  - impersonation
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:28:44.452Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 090ce3ad-c994-49dc-98e2-f746855d5149
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Obtain-and-Use-Attackers-API-Key

## Summary

This procedure describes generating an API key for the hijacked WakaTime account, allowing the attacker to integrate it with coding platforms for activity submission.

## Description

Post-registration, the attacker logs into the dashboard and requests an API key, which is issued without further identity validation. This key enables API calls to log coding heartbeats. The procedure assumes access to a supported IDE like VS Code, where the key is pasted into the WakaTime extension settings. Outcomes include seamless activity logging, exploiting the lack of key revocation mechanisms.

## Requirements

1. Active session in the hijacked account
2. Installed coding platform with WakaTime plugin (e.g., VS Code extension)
3. Internet access for key generation

## Defense

Defensive measures and detection strategies:

- Tie API key issuance to verified email or multi-factor authentication
- Implement key rotation on password resets
- Monitor for anomalous API key usage patterns

## Objectives

1. Secure a functional API key for unauthorized activity submission
2. Integrate key into attacker's development environment
3. Prepare for parallel session exploitation

## Instructions

### Step 1: Generate API Key

**Context**: Access the API key generation feature in the account dashboard.

Log in to https://waketime.com and navigate to Settings > API Keys. Click to generate a new key.

> The key is displayed as a string (e.g., starting with 'waka_'), copy it without any validation prompts.

### Step 2: Integrate into Coding Platform

**Context**: Configure the platform to use the key for automatic logging.

Install the WakaTime extension in VS Code, paste the API key when prompted, and restart the IDE.

> The extension authenticates successfully, ready for activity tracking.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[api-key]]
- [[impersonation]]
