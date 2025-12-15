---
id: 123e4567-e89b-12d3-a456-426614174001
name: Identify-Missing-CSRF-Protections-in-Concrete5
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:15.469Z'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Active Scanning]]'
sub_techniques: []
tags:
  - csrf
  - reconnaissance
  - concrete-cms
platforms:
  - Web
  - PHP
commands: []
tools: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---

# Identify Missing CSRF Protections in Concrete5

## Summary

This procedure involves analyzing the Concrete CMS 5.7.3.1 codebase and testing administrative endpoints to uncover inconsistencies in CSRF token validation, enabling the identification of state-changing POST requests vulnerable to forgery.

## Description

In Concrete CMS 5.7.3.1, the Synchronizer Token Pattern is implemented via the Concrete\Core\Validation\CSRF\Token class, but its usage is inconsistent across dashboard pages and blocks. This procedure reviews source code and performs manual testing on functions like file deletion, registration settings, and user group management to detect missing validations. The target environment is a PHP-based web application with administrative interfaces. Expected outcomes include a catalog of exploitable endpoints that allow unauthorized actions when an authenticated user is tricked into submitting forged requests.

## Requirements

1. Access to Concrete CMS 5.7.3.1 source code or a running instance
2. Authenticated administrative session for testing legitimate requests
3. Web browser developer tools for inspecting network traffic

## Defense

Defensive measures and detection strategies:

- Implement consistent CSRF token validation on all state-changing endpoints
- Use web application firewalls (WAFs) to detect anomalous POST requests from external referrers
- Enable logging of administrative actions for anomaly detection

## Objectives

1. Catalog vulnerable endpoints lacking CSRF checks
2. Understand the scope of potential unauthorized actions
3. Prepare for crafting targeted exploits

## Instructions

### Step 1: Review CSRF Token Class

**Context**: Examine the core CSRF implementation to identify its intended usage and gaps in application-wide adoption.

Inspect the Concrete\Core\Validation\CSRF\Token class in the source code, noting methods for generating and validating tokens. Look for patterns where tokens are required in forms but omitted in certain controllers.

### Step 2: Test Administrative Endpoints

**Context**: Simulate legitimate POST requests to dashboard and block endpoints, monitoring for token presence in requests and server-side validation.

Use browser tools to perform actions like deleting a file via /index.php/tools/required/files/delete or updating registration at /index.php/dashboard/system/registration/open/update_registration_type. Check if requests include CSRF tokens and attempt to replay without them to confirm bypass.

### Step 3: Document Vulnerabilities

**Context**: Compile a list of confirmed vulnerable endpoints with their impacts.

Record details for each, such as location, root cause (missing validation), and impact (e.g., arbitrary file deletion).

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[Reconnaissance]]
- [[concrete-cms]]
