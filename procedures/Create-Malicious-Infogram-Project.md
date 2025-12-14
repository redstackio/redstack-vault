---
tags:
  - xss
  - payload-creation
  - infogram
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:14.256Z'
sub_techniques: []
id: d518ac64-f536-446c-8196-da7d27c7255d
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create Malicious Infogram Project

## Summary

This procedure creates an Infogram project with a stored XSS payload in the project name, which will be reflected unsanitized when embedded in WordPress via the plugin.

## Description

Using an Infogram account, a new project is initiated with a name containing a JavaScript payload like `"><img src=x onerror=prompt(0);>`. A basic report is generated to make the project embeddable. This stores the malicious input on Infogram's servers, which the WordPress plugin retrieves without escaping. The target environment is any Infogram instance, and outcomes include a publishable project ID for embedding.

## Requirements

1. Valid Infogram account credentials
2. Web browser for accessing infogram.com
3. Basic knowledge of XSS payloads

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs on external platforms like Infogram
- Implement output encoding for project metadata in APIs
- Use web application firewalls (WAF) to scan for XSS patterns in project names

## Objectives

1. Inject and store XSS payload in project metadata
2. Generate embeddable content with the payload
3. Enable reflection in downstream applications like WordPress plugins

## Instructions

### Step 1: Log In to Infogram

**Context**: Access the platform to create content.

Open a browser and navigate to infogram.com. Log in with your credentials to reach the dashboard.

### Step 2: Create Project with Payload

**Context**: Set the malicious name during project initialization.

Click 'Create New' and select a template (e.g., simple chart). In the project name field, enter `"><img src=x onerror=prompt(0);>`. Add minimal content like a blank report, then save and publish the project.

> Note the project ID or embed URL for later use in WordPress.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- payload-creation
- infogram
