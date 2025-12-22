---
tags:
  - deserialization
  - yaml
  - rce
  - python
  - code-review
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
platforms:
  - Web
  - Python
techniques:
  - '[[Hardware]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: cd6cd3e3-a8ca-4a0a-bb8f-d2eee48b8ce0
created_at: '2025-12-14T17:23:54.010Z'
updated_at: '2025-12-14T17:23:54.010Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Identify-Unsafe-YAML-Deserialization

## Summary

This procedure details the manual code review process to detect unsafe YAML deserialization vulnerabilities in Python applications, such as the use of yaml.load() that allows arbitrary object construction, potentially leading to remote code execution if untrusted data is processed.

## Description

In the Liberapay project, a code review of the GitHub repository revealed an unsafe deserialization issue in liberapay/testing/vcr.py at line 40. The function used PyYAML's yaml.load(), which can instantiate arbitrary Python classes from YAML input, enabling attackers to craft malicious payloads for code execution. This is particularly risky in scenarios involving untrusted YAML, though here it's limited to repository files. The procedure involves searching for yaml.load() usages, analyzing context for untrusted input, and recommending yaml.safe_load() to restrict to safe primitives like dicts, lists, and strings. Expected outcomes include vulnerability confirmation and a mitigation plan.

## Requirements

1. Access to the target's source code repository (e.g., public GitHub)
2. Familiarity with Python and PyYAML library
3. Text editor or IDE for browsing code (e.g., VS Code)

## Defense

Defensive measures and detection strategies:

- Use yaml.safe_load() exclusively for all YAML parsing to prevent arbitrary object creation
- Implement input validation to ensure YAML sources are trusted
- Conduct static code analysis with tools like Bandit to flag unsafe deserialization
- Monitor for anomalous object instantiations in logs during deserialization

## Objectives

1. Identify instances of unsafe yaml.load() in the codebase
2. Assess the risk of RCE from arbitrary object construction
3. Recommend and verify safer deserialization practices

## Instructions

### Step 1: Access and Clone the Repository

**Context**: Obtain the source code for review without needing runtime access.

Navigate to the Liberapay GitHub repository at https://github.com/liberapay/liberapay and clone it locally for inspection.

### Step 2: Search for Vulnerable Patterns

**Context**: Locate deserialization calls that use unsafe functions.

Open the codebase in an editor and search for 'yaml.load' across files, focusing on the testing module.

### Step 3: Analyze Context and Impact

**Context**: Determine if the deserialization processes untrusted data.

Examine liberapay/testing/vcr.py line 40: Confirm yaml.load() is used on YAML data from repository files. Note that while trusted, introducing untrusted YAML could allow RCE via custom class instantiation (e.g., os.system calls).

### Step 4: Propose and Verify Fix

**Context**: Suggest mitigation and test the change.

Replace yaml.load() with yaml.safe_load(). Test by processing sample YAML to ensure no arbitrary objects are created, confirming restriction to basic types.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Hardware]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- deserialization
- yaml
- rce
- python
- code-review
