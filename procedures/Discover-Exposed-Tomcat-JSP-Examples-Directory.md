---
tags:
  - recon
  - web
  - tomcat
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
updated_at: '2025-12-14T03:16:08.334Z'
sub_techniques: []
id: e19340d9-f782-4241-a142-7a89bd375dd7
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Discover Exposed Tomcat JSP Examples Directory

## Summary

This procedure involves scanning and accessing a target web host to identify if the Apache Tomcat /jsp-examples directory is publicly exposed, revealing example JSP files that may contain vulnerabilities like improper input handling.

## Description

In production or pilot environments, development example directories like /jsp-examples in Apache Tomcat are sometimes left accessible, providing an entry point for attackers to probe for weaknesses. This procedure targets hosts running Tomcat, such as 8x8pilot.com, by directly accessing the path to confirm exposure. Successful discovery allows follow-on testing for issues like reflected XSS, potentially leading to JavaScript execution in user browsers for data theft or phishing.

## Requirements

1. Internet access to the target host
2. Web browser for manual navigation
3. Basic understanding of web server structures (e.g., Tomcat defaults)

## Defense

Defensive measures and detection strategies:

- Remove or restrict access to example directories in production (e.g., via .htaccess or server config)
- Implement web application firewalls (WAF) to block directory enumeration attempts
- Monitor access logs for suspicious paths like /jsp-examples

## Objectives

1. Confirm public exposure of /jsp-examples directory
2. Identify available JSP example files for further testing
3. Establish initial foothold for vulnerability assessment

## Instructions

### Step 1: Access Target Host and Append Path

**Context**: Directly navigate to the suspected directory path to check for exposure without authentication.

Use a web browser to visit the target URL with the /jsp-examples suffix, e.g., http://8x8pilot.com/jsp-examples/.

> If the directory loads, it lists JSP files like ssn.jsp, confirming exposure. No command-line tool is required; this is manual reconnaissance.

### Step 2: Verify Directory Contents

**Context**: Interact with the directory to ensure it's not just a 404 but contains executable JSP examples.

Click on or access individual files, such as http://8x8pilot.com/jsp-examples/ssn.jsp, to see if forms or inputs are present.

> Successful access shows interactive pages with user input fields, indicating potential for input reflection testing.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- recon
- web
- tomcat
