---
id: proc-pollution-identify-001
tags:
  - parameter-pollution
  - web-vulnerability
  - recon
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:39.498Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify Parameter Pollution on Badges Page

## Summary

This procedure identifies HTTP parameter pollution vulnerabilities on web applications like IRCCloud's badges page by testing duplicate parameters to reveal inconsistent server-side handling, setting the stage for further exploitation such as XSS evasion.

## Description

Parameter pollution occurs when a server fails to properly normalize or handle multiple instances of the same parameter in a request, leading to manipulated output. In this scenario, targeting the 'hostname' parameter on www.irccloud.com/badges allows conflicting values to alter page rendering. This is useful in authenticated web environments to probe for weaknesses in parameter processing, potentially enabling injection attacks. Prerequisites include a web browser and access to the target page.

## Requirements

1. Authenticated session to IRCCloud badges page
2. Web browser with URL manipulation capability (e.g., address bar or developer tools)
3. Basic understanding of HTTP requests and parameters

## Defense

Defensive measures and detection strategies:

- Implement strict parameter normalization to handle duplicates (e.g., take the first or last value consistently)
- Use web application firewalls (WAFs) to detect and block duplicate parameter patterns
- Log and monitor requests with unusual parameter repetition for anomaly detection

## Objectives

1. Confirm vulnerability to parameter pollution
2. Map how server handles duplicate 'hostname' values
3. Identify opportunities for output manipulation

## Instructions

### Step 1: Access the Target Page

**Context**: Navigate to the badges page to establish a baseline.

Visit www.irccloud.com/badges in an authenticated browser session and inspect the page source for 'hostname' parameter usage in scripts or attributes.

> Expected: Page loads normally with 'hostname' reflected in output.

### Step 2: Test Duplicate Parameters

**Context**: Introduce multiple 'hostname' parameters to observe inconsistencies.

Append parameters to the URL: www.irccloud.com/badges?hostname=value1&hostname=value2. Reload and compare output to single-parameter version.

> Expected: Altered rendering, such as conflicting hostname values in page elements, indicating pollution.

### Step 3: Validate Inconsistency

**Context**: Experiment with parameter order to confirm manipulation.

Swap order (e.g., ?hostname=value2&hostname=value1) and check for varying results.

> Expected: Different outputs based on order, proving inadequate handling.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- parameter-pollution
- web-testing
