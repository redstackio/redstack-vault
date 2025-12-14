---
id: uuid-analyze-readapi
tags:
  - ssrf
  - recon
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T03:53:38.746Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Analyze-readapi-Variable-Functionality

## Summary

This procedure involves reviewing and testing the functionality of the 'readapi' variable in Streamlabs Cloudbot to understand how it handles URL fetches in chat commands, laying the groundwork for identifying SSRF vulnerabilities.

## Description

The readapi variable allows users to inject custom HTTPS URLs into chat commands, where the backend performs a fetch and inserts the response. By analyzing documentation and basic tests, attackers can confirm the request mechanism and prepare for exploitation. This targets web-based chat services like Streamlabs Cloudbot, expecting outcomes like successful content insertion for valid URLs.

## Requirements

1. Access to Streamlabs Cloudbot dashboard (https://streamlabs.com/dashboard#/cloudbot/commands/variables)
2. Ability to create and test custom chat commands
3. Basic web knowledge for URL testing

## Defense

Defensive measures and detection strategies:

- Implement strict URL whitelisting in backend request handlers
- Log all readapi fetches for anomaly detection (e.g., unusual domains)
- Rate-limit chat command executions to prevent abuse

## Objectives

1. Confirm readapi sends HTTPS requests and inserts responses
2. Document integration in custom chat commands
3. Identify potential for user-controlled fetches

## Instructions

### Step 1: Review Documentation

**Context**: Examine official docs to understand variable behavior.

No command needed; navigate to https://streamlabs.com/dashboard#/cloudbot/commands/variables and note that {readapi.<url>} fetches HTTPS content.

> Expected: Description of HTTPS request and response insertion.

### Step 2: Test Basic Functionality

**Context**: Verify fetch works with a simple HTTPS URL.

Create a test command with {readapi.https://example.com} and trigger in chat.

> Expected: Response from example.com inserted in chat.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[ssrf]]
- [[recon]]
