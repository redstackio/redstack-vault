---
id: proc-uuid-002
tags:
  - phishing
  - email-spoofing
  - misconfiguration
type: procedure
tools:
  - '[[tools/DMARC-Inspector]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Email/DNS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Phishing]]'
updated_at: '2025-12-14T17:30:58.784Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
---
# Verify-Missing-DMARC-Implications

## Summary

This procedure analyzes the consequences of a missing DMARC record, explaining how it allows email spoofing and phishing while noting mitigations like GPG signatures.

## Description

Without DMARC, even if SPF and DKIM are configured, emails may not be properly authenticated if domains don't align. Attackers can forge From headers, leading to phishing or reputation harm. For paragonie.com, the absence was verified, but GPG was used for auth. This step involves reviewing tool outputs and understanding attack vectors like sending spoofed emails that pass basic checks.

## Requirements

1. Results from DMARC check
2. Knowledge of email protocols (SPF, DKIM, DMARC)
3. Optional: Email testing environment

## Defense

Defensive measures and detection strategies:

- Implement DMARC with quarantine/reject policies
- Train users on phishing indicators
- Use GPG or S/MIME for signed emails

## Objectives

1. Explain spoofing risks
2. Identify mitigation gaps
3. Recommend remediation

## Instructions

### Step 1: Review Tool Output

**Context**: Interpret the inspector's report on authentication failures.

**Command** (N/A - Analysis):

Examine output from [[tools/DMARC-Inspector]] showing no policy and examples of failed alignments.

> Look for messages like 'Mail from unaligned domains may be delivered'.

### Step 2: Simulate Spoofing Scenario

**Context**: Understand practical impacts without executing attacks.

**Command** (N/A - Conceptual):

Consider sending a test email with forged From: header using tools like swaks, observing if it bypasses filters due to no DMARC.

> Expected: Email appears legitimate to recipients without strict DMARC enforcement.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Phishing]] Phishing

### Sub-Techniques

- N/A

## Commands Used

- N/A

## Tools Used

- [[tools/DMARC-Inspector]]

## Tags

- phishing
- spoofing
- email-security
