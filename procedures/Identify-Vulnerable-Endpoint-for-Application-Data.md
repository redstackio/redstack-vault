---
id: proc-uuid-002
tags:
  - endpoint-identification
  - discovery
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:28:59.102Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Identify-Vulnerable-Endpoint-for-Application-Data

## Summary

This procedure analyzes exposed administrative code to identify endpoints vulnerable to unauthorized data retrieval, focusing on parameters that allow direct object references without validation.

## Description

Once an admin JS file is accessed, this step involves parsing the code for endpoint definitions, request methods, and parameters. In the target scenario, the endpoint at https://███/███ accepts POST requests with a 'url' parameter for application IDs, returning PII without auth or ownership checks, setting up IDOR exploitation.

## Requirements

1. Access to the exposed JS file contents
2. Text editor or code analysis tool
3. Understanding of JavaScript and HTTP request structures

## Defense

Defensive measures and detection strategies:

- Obfuscate or remove sensitive endpoint details from client-side JS
- Enforce server-side authentication on all admin endpoints
- Log and alert on code inspection attempts

## Objectives

1. Extract endpoint URL and method from JS code
2. Identify key parameters like 'url' for data access
3. Verify absence of authorization logic

## Instructions

### Step 1: Parse JS Code for Endpoints

**Context**: Search the file for HTTP request patterns indicating data retrieval.

No command; manual review.

> Locate functions handling POST requests to paths like /███ with 'url' param.

### Step 2: Document Vulnerability Details

**Context**: Note the lack of auth checks to confirm exploitability.

No command.

> Confirm the endpoint returns sensitive data (e.g., PII) based on param input.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- endpoint-identification
- discovery
