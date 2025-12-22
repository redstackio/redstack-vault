---
id: proc-inject-xss-db-name
tags:
  - xss
  - payload-injection
  - reflected-xss
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T00:11:09.150Z'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-in-Database-Name

## Summary

This procedure involves entering a malicious JavaScript payload into the Database Name field of the Concrete CMS installer to exploit a reflected XSS vulnerability, allowing arbitrary code injection during configuration.

## Description

During the Concrete CMS installation, the database configuration screen lacks proper input validation for the Database Name field. By supplying a payload like '<script>alert(1)</script>', attackers can reflect and execute JavaScript in the user's browser upon form submission. This targets PHP-based web applications in setup mode, with outcomes including proof-of-concept alerts or more severe client-side attacks like keylogging.

## Requirements

1. Access to the database configuration screen in the installer
2. Valid MySQL connection details (host, user, password)
3. Web browser to interact with the form

## Defense

Defensive measures and detection strategies:

- Implement client-side and server-side escaping for all form inputs (e.g., htmlspecialchars in PHP)
- Validate database names against expected patterns (alphanumeric only)
- Log and alert on suspicious inputs during installation

## Objectives

1. Successfully inject JavaScript without form validation blocking
2. Prepare for reflection upon submission
3. Demonstrate lack of sanitization in the field

## Instructions

### Step 1: Navigate to Database Configuration

**Context**: Reach the form where database details are entered.

Proceed through the installer until the DB config screen loads.

> Ensure previous steps (e.g., license acceptance) are completed.

### Step 2: Fill Valid Fields

**Context**: Provide legitimate values to avoid errors in other areas.

Enter: Host = 'localhost', Username = 'root', Password = 'yourpassword'.

> Use an existing MySQL user with create database privileges.

### Step 3: Set Malicious Database Name

**Context**: Inject the payload to test reflection.

Set Database Name to '<script>alert(1)</script>'.

> This payload will be echoed back unescaped in the response.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[payload-injection]]
