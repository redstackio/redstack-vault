---
id: proc-1147949-csrf-confirm
tags:
  - csrf
  - web
  - anti-csrf
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:27:35.749Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
---
# Confirm-Absence-of-CSRF-Protection

## Summary

This procedure verifies the lack of Cross-Site Request Forgery (CSRF) protections on a POST endpoint, allowing unauthorized cross-origin form submissions that can be chained with other vulnerabilities like XSS.

## Description

The target POST endpoint at /██████ on https://██████████ does not include CSRF tokens, origin header checks, or same-site cookie attributes, making it vulnerable to forgery from external sites. This confirmation step involves inspecting requests and testing cross-origin submissions to ensure attackers can force authenticated users to perform actions without consent, such as submitting malicious payloads.

## Requirements

1. Burp Suite for request inspection and modification.
2. Access to the target web application.
3. A test environment simulating cross-origin requests.

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all state-changing POST requests.
- Enforce SameSite=Strict or Lax on session cookies.
- Log and alert on requests missing CSRF tokens or from unexpected origins.

## Objectives

1. Inspect for absence of anti-CSRF mechanisms.
2. Test successful cross-site request execution.
3. Evaluate risk for chaining with input vulnerabilities.

## Instructions

### Step 1: Inspect Request Headers and Parameters

**Context**: Analyze the legitimate POST request for CSRF-related elements.

Use Burp Suite to capture the request and check for parameters like a CSRF token or headers like Origin and Referer.

**Expected Output**: No CSRF token present; standard headers only.

### Step 2: Test Cross-Origin Submission

**Context**: Simulate a request from an external domain to confirm acceptance.

Modify the request in Burp Suite to originate from a different domain (e.g., via a local HTML page) and submit to the endpoint without any token.

**Expected Output**: Server processes the request successfully, indicating no protection.

### Step 3: Document Findings

**Context**: Note the implications for exploitation.

Record that the endpoint is susceptible to CSRF, enabling attacks like forced XSS injection.

**Expected Output**: Confirmation report of vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Steal Web Session Cookie]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- csrf
- cross-site-request-forgery
- web-security
