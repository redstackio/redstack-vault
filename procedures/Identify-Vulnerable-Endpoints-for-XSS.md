---
tags:
  - xss
  - recon
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 967bd6cd-2747-465b-b633-60f464b22853
created_at: '2025-12-14T00:11:25.188Z'
updated_at: '2025-12-14T00:11:25.188Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify Vulnerable Endpoints for XSS

## Summary

This procedure involves discovering web endpoints that accept user-controllable parameters, such as miniUrl, which can be tested for reflected XSS vulnerabilities through brute-force or manual exploration.

## Description

In this attack scenario, endpoints like /resources/read/embed_mini/ on sites such as www.hackerone.com and resources.hackerone.com are identified as accepting a miniUrl parameter without sufficient sanitization, enabling potential XSS injection. The procedure is useful for initial reconnaissance in web vulnerability assessments, targeting public-facing applications. Expected outcomes include a list of injectable endpoints.

## Requirements

1. Access to the target web application
2. Web browser or HTTP client for testing
3. Knowledge of common parameter names (e.g., miniUrl)

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and output encoding on all parameters
- Use web application firewalls (WAF) to detect XSS patterns

## Objectives

1. Identify endpoints vulnerable to parameter injection
2. Confirm parameter acceptance without immediate rejection
3. Prepare for payload testing

## Instructions

### Step 1: Enumerate Endpoints

**Context**: Manually explore or brute-force potential URLs to find those with injectable parameters.

Navigate to base URLs like https://www.hackerone.com/resources/ and append /read/embed_mini/?miniUrl=test to check for parameter processing.

> Expect the endpoint to load without errors, indicating acceptance.

### Step 2: Document Findings

**Context**: Record the full URLs of vulnerable endpoints.

List endpoints such as https://www.hackerone.com/resources/read/embed_mini/ and https://resources.hackerone.com/resources/read/embed_mini/.

> Ensure documentation includes parameter details for further testing.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[xss]]
- [[recon]]
