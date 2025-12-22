---
id: a2a1d21b-7b19-43e3-9184-79f51643c435
name: Inject Malicious XSS Payload in Workflow Keyword
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T06:10:15.466Z'
updated_at: '2025-12-11T06:10:15.466Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - xss
  - payload-injection
commands:
  - '[[commands/git-clone-trac-repo]]'
platforms:
  - Web
tools:
  - '[[tools/Git]]'
  - '[[tools/Web-Browser]]'
skill_level: beginner
impact_level: medium
detection_risk: medium
validated: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059.007]]'
---

# Inject Malicious XSS Payload in Workflow Keyword

## Summary

This procedure describes how to inject a malicious XSS payload into the workflow keyword field during Trac ticket creation, exploiting unescaped user input to enable arbitrary JavaScript execution.

## Description

The attack targets the workflow keywords feature where input is not properly escaped in the JavaScript-generated delete button. By pasting a payload like "><svg/onload=alert(document.domain)>, attackers can store malicious code that executes when the ticket is viewed. This is part of a stored XSS attack in a web environment using jQuery.

## Requirements

1. Access to the new ticket creation page
2. Web browser for form interaction
3. Knowledge of basic XSS payloads

## Defense

Defensive measures and detection strategies:

- Use jQuery's safe .attr() method to escape inputs
- Implement content security policy (CSP) to restrict script execution

## Objectives

1. Insert payload into vulnerable field
2. Bypass any basic input checks
3. Prepare for storage and execution

## Instructions

### Step 1: Select and Inject Payload

**Context**: Locate the workflow keyword field and insert the payload.

Using [[tools/Web-Browser]], select a Workflow Keyword, click manual, and paste the payload: "><svg/onload=alert(document.domain)>

> Expected: Payload accepted into the field without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Web-Browser]]

## Tags

- [[xss]]
- [[payload-injection]]
