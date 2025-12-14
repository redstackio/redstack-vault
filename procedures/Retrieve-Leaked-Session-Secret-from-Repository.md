---
tags:
  - secret-leak
  - rails
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Credentials In Files]]'
updated_at: '2025-12-14T17:23:54.963Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: f03d0f66-8d75-4811-b988-7bca877a46db
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Credentials In Files]]'
---
# Retrieve-Leaked-Session-Secret-from-Repository

## Summary

This procedure involves manually accessing a public GitHub commit to extract a leaked Rails session secret, providing the key needed for crafting malicious cookies in deserialization attacks.

## Description

Following repository scanning, navigate to the specific commit URL to copy the secret_key_base value. In the Algolia case, the secret is in secret_token.rb at a known commit hash. This step requires no tools beyond a browser and is low-risk as it uses public data. Outcome: The exact secret string for use in exploits.

## Requirements

1. URL to the commit with the leaked secret
2. Basic web browsing capability

## Defense

Defensive measures and detection strategies:

- Regularly audit and remove secrets from Git history using BFG Repo-Cleaner
- Educate developers on secret management with tools like git-secrets
- Use GitHub's secret scanning alerts

## Objectives

1. Obtain the precise secret value
2. Prepare for session manipulation
3. Avoid detection by using public sources

## Instructions

### Step 1: Access the Commit URL

**Context**: Open the browser to the specific diff.

Navigate to: https://github.com/algolia/facebook-search/commit/f3adccb5532898f8088f90eb57cf991e2d499b49#diff-afe98573d9aad940bb0f531ea55734f8R12

> Expected output: View of secret_token.rb showing secret_key_base = "..."

### Step 2: Copy the Secret Value

**Context**: Extract the full hex string.

Copy the 128-character value from line 12.

> Expected output: String like "a1b2c3..." (actual leaked value).

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Credentials In Files]] Credentials In Files

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- secret-leak
- github
