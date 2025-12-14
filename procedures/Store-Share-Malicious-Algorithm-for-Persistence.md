---
id: proc-uuid-006
tags:
  - persistence
  - algorithm-sharing
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/define-malicious-get-datetime-class]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:23.604Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Store-Share-Malicious-Algorithm-for-Persistence

## Summary

Obfuscate the malicious class within a larger algorithm code and share it via Quantopian's platform, allowing persistent XSS against anyone who clones and debugs it.

## Description

After injection, hide the class (e.g., in comments or unused sections) to avoid detection. Saving and sharing the algorithm turns it into a vector for broad exploitation, as cloning preserves the code and triggers XSS on debugger use.

## Requirements

1. Completed malicious code injection
2. Obfuscation techniques (e.g., string concatenation)
3. Sharing permissions on Quantopian

## Defense

Defensive measures and detection strategies:

- Scan shared algorithms for suspicious class definitions
- Warn users on cloning untrusted code
- Disable debugger for public algos

## Objectives

1. Create a self-propagating exploit vector
2. Target broad user base
3. Ensure long-term access via data theft

## Instructions

### Step 1: Obfuscate the Class

**Context**: Hide the payload to evade reviews.

Modify [[commands/define-malicious-get-datetime-class]] with splits or comments, e.g., place in a def unused(): block.

**Expected Output**: Code appears benign on inspection.

### Step 2: Save and Share

**Context**: Distribute for cloning.

Save the algorithm, set to public or invite collaborators, and encourage debugging.

**Expected Output**: Cloners trigger XSS on run.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/define-malicious-get-datetime-class]]

## Tools Used


## Tags

- persistence
- algorithm-sharing
