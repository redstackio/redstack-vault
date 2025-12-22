---
id: p-generate-tokens
tags:
  - token-generation
  - brute-force-prep
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/generate-recovery-tokens-php]]'
verified: false
platforms:
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:31:31.155Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Generate-Candidate-Recovery-Tokens-Locally

## Summary

This procedure runs a local PHP script to generate thousands of candidate recovery tokens using the same insecure uniqid() method as Revive Adserver, formatted to match the server's output for subsequent brute-forcing.

## Description

After triggering a password recovery, generate tokens locally while time is synchronized. The script mimics strtoupper(md5(uniqid('',true))) and formats to 22 characters, producing ~10,000 possibilities to cover microsecond variations.

## Requirements

1. Local PHP installation
2. Synchronized system time
3. Text file to store outputs

## Defense

Defensive measures and detection strategies:

- Use high-entropy token generation (e.g., 256-bit random)
- Short token expiration (e.g., 5 minutes)
- Log token usage and detect patterns

## Objectives

1. Simulate server token generation
2. Produce brute-force candidate list
3. Format tokens correctly for requests

## Instructions

### Step 1: Prepare PHP Environment

**Context**: Ensure PHP is ready for execution.

Verify PHP version matches target's (e.g., PHP 7+).

### Step 2: Execute Token Generation Script

**Context**: Run the loop to create candidates.

Execute [[commands/generate-recovery-tokens-php]] and redirect output to a file: php -r 'for($i=0;$i<=10000;$i++){ $recoveryId=strtoupper(md5(uniqid('',true))); $recoveryId=substr(chunk_split($recoveryId,8,'-'),-23,22); print $recoveryId."\n"; }' > tokens.txt

**Expected Output**: File with 10,000 lines of 22-char tokens like '58FC30C5-3DB6-3XXX-XXXX'.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] Command and Scripting Interpreter: JavaScript (adapted for PHP)

### Sub-Techniques


## Commands Used

- [[commands/generate-recovery-tokens-php]]

## Tools Used


## Tags

- generation
- php-script
