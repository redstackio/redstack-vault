---
id: p-csrf-identify-federalist
tags:
  - csrf
  - recon
  - api
type: procedure
tools:
  - '[[tools/swf-json-csrf]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:20.815Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify CSRF Lack of Protection in API

## Summary

This procedure involves inspecting the Federalist API to identify missing CSRF protections on POST endpoints, confirming vulnerability to forgery attacks by testing Content-Type handling without tokens.

## Description

In the Federalist API (e.g., https://federalist.fr.cloud.gov/v0/build/), POST endpoints lack CSRF tokens, allowing state-changing actions if requests can be forged. Initial tests reveal JSON-only acceptance but no token enforcement, setting up for advanced bypasses like Flash-based forgery. This reconnaissance step is crucial for validating the attack surface in web APIs.

## Requirements

1. Access to Federalist API documentation and endpoints
2. Browser developer tools or proxy like Burp Suite for inspection
3. Knowledge of target site IDs for testing

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all state-changing endpoints
- Enforce strict Content-Type validation with additional headers like Origin
- Monitor for anomalous POST requests from unexpected sources

## Objectives

1. Confirm absence of anti-CSRF mechanisms
2. Identify Content-Type enforcement as the only barrier
3. Gather endpoint details for payload crafting

## Instructions

### Step 1: Inspect API Endpoints

**Context**: Review API docs and responses to check for CSRF tokens.

Use browser dev tools to examine POST requests to /v0/build/ or /v0/sites/. Send a sample JSON POST without tokens.

**Expected Output**: Request succeeds if authenticated but may fail on Content-Type if not JSON.

### Step 2: Test Initial POC

**Context**: Attempt a basic CSRF POC to confirm token absence.

Craft a simple HTML form POST to the endpoint with JSON data; observe acceptance without tokens but rejection on non-JSON types.

**Expected Output**: Error on Content-Type mismatch, no token error.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/swf-json-csrf]]

## Tags

- [[csrf]]
- [[recon]]
