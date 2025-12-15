---
id: proc-uuid-4
tags:
  - automation
  - burp-intruder
  - enumeration-scale
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:01.697Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
  - '[[Exploit Public-Facing Application]]'
---
# Automate-Enumeration-with-Burp-Intruder

## Summary

This procedure automates the request replay using Burp Suite's Intruder to send money requests to a large list of emails simultaneously, scaling user enumeration and information disclosure efficiently.

## Description

Building on manual replays, Intruder allows payload injection into the email parameter across multiple threads, testing 80+ emails in parallel without rate limits. Responses can be analyzed for success codes, and subsequent transaction reviews yield bulk enumeration. This amplifies the impact, potentially leading to DoS via email spam or comprehensive user database building.

## Requirements

1. Burp Suite Professional (Intruder feature).
2. Wordlist of target emails (e.g., 80 entries).
3. Captured request template from prior steps.

## Defense

Defensive measures and detection strategies:

- Deploy CAPTCHA or secondary verification after multiple requests.
- Rate limit at the application layer, including per-session caps.

## Objectives

1. Test hundreds of emails rapidly for account validation.
2. Collect responses for pattern analysis.
3. Enable large-scale name disclosure post-automation.

## Instructions

### Step 1: Load Request into Intruder

**Context**: Prepare the captured POST for automation.

In Burp, send the request to Intruder; mark §transaction[from]=test@email.com§ as payload position.

**Expected Output**: Intruder interface with marked position.

### Step 2: Configure Payloads

**Context**: Load list of emails to test.

Go to Positions > Payloads, select Simple list, paste 80 emails (e.g., user1@domain.com, user2@domain.com).

**Expected Output**: Payload set loaded.

### Step 3: Set Threads and Start Attack

**Context**: Run in parallel to bypass any soft limits.

In Options, set threads to 5; click Start attack.

**Expected Output**: Intruder sends requests concurrently, showing 200 OK for most.

### Step 4: Analyze Results and Review Transactions

**Context**: Correlate with transaction page for enumeration.

Export results; revisit /transactions to check displays for names.

**Expected Output**: Bulk data on valid users and disclosed names.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- automation
- burp-intruder
- enumeration-scale
