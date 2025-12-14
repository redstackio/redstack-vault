---
id: p-identify-uniqid-weakness
tags:
  - entropy-analysis
  - crypto-weakness
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T17:31:31.166Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Identify-Uniqid-Entropy-Weakness

## Summary

This procedure details the analysis of PHP's uniqid() function to confirm its low entropy and predictability, as used in Revive Adserver's token generation, providing less than 2^20 possibilities per second.

## Description

uniqid() generates unique IDs based on the current timestamp in microseconds but lacks cryptographic security, making it vulnerable to prediction if the attacker's time is synchronized with the server. Per the PHP manual, it is not suitable for security-sensitive contexts. This step builds on source code review to quantify the weakness and plan brute-force feasibility.

## Requirements

1. PHP documentation access
2. Understanding of entropy and randomness in cryptography
3. Local PHP environment for testing uniqid() outputs

## Defense

Defensive measures and detection strategies:

- Replace uniqid() with random_bytes() or openssl_random_pseudo_bytes() for tokens
- Monitor for unusual token generation patterns in logs
- Use hardware security modules (HSMs) for high-entropy randomness

## Objectives

1. Confirm uniqid()'s reliance on system time
2. Calculate entropy limitations (microsecond precision)
3. Assess brute-force viability

## Instructions

### Step 1: Review PHP Manual

**Context**: Understand uniqid() parameters and limitations.

Read the official PHP docs for uniqid(), noting the optional prefix and more_entropy flag (not used here), and its base on gettimeofday().

### Step 2: Test Local Entropy

**Context**: Generate sample IDs to observe predictability.

Run a simple PHP script locally: echo uniqid('', true); multiple times in a second to see repetition patterns.

**Expected Output**: IDs varying only in the last few digits, confirming low variety per timestamp.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Software

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- crypto-weakness
- uniqid
