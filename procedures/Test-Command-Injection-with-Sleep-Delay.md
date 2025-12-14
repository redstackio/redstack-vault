---
id: proc-uuid-2
tags:
  - command-injection
  - rce
  - testing
type: procedure
tools:
  - '[[tools/WebPageTest]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/sleep-20-injection]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:23:41.146Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Test-Command-Injection-with-Sleep-Delay

## Summary

This procedure tests the command injection vulnerability by injecting a sleep command into the filter parameter, observing a delay to confirm remote code execution without direct output visibility.

## Description

Target the WebPageTest instance at http://wpt.ec2.shopify.com/. The injection uses $(`sleep 20`) in the filter field of the testlog interface, leveraging the flawed exec() call to execute the shell command, causing a measurable delay. This is a low-risk proof-of-concept for blind RCE in a PHP web app on AWS.

## Requirements

1. Access to the target URL http://wpt.ec2.shopify.com/
2. Web browser to interact with the application
3. Timer to measure response delay

## Defense

Defensive measures and detection strategies:

- Sanitize inputs thoroughly, avoiding shell metacharacters
- Log and alert on unusual process delays in web server logs
- Implement web application firewall (WAF) rules for injection patterns

## Objectives

1. Confirm command execution capability
2. Validate bypass of existing filters
3. Establish proof for further exploitation

## Instructions

### Step 1: Access the Vulnerable Endpoint

**Context**: Navigate to the main page and locate the filter input.

Access http://wpt.ec2.shopify.com/ and find the text area for filter input.

> No command; prepare the interface.

### Step 2: Inject and Test Payload

**Context**: Submit the sleep payload to observe execution.

**Command** ([[commands/sleep-20-injection]]):
```bash
# Payload entered in filter field: $(`sleep 20`)
# Then click 'Update List'
```

> This injects the sleep command via command substitution. Expected: 20-second delay before page updates, indicating successful RCE.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Unix Shell]]

### Sub-Techniques


## Commands Used

- [[commands/sleep-20-injection]]

## Tools Used

- [[tools/WebPageTest]]

## Tags

- command-injection
- rce
