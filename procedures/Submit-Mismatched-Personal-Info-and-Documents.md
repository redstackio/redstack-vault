---
id: proc-exness-mismatched-submit-001
tags:
  - document-upload
  - mismatch-exploit
type: procedure
tools: []
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Impair Defenses]]'
updated_at: '2025-12-14T17:25:12.744Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Impair Defenses]]'
---
# Submit Mismatched Personal Info and Documents

## Summary

This procedure uploads official identity documents that do not match the previously entered personal information during EXNESS KYC, exploiting inadequate cross-checking to achieve verification approval under false identity.

## Description

After entering profile details, mismatched ID and proof of address documents are uploaded. The third-party verification service approves without integrating checks against profile data, allowing the account to be verified fraudulently. This targets the web verification flow on my.exness.com, with a 15-30 minute wait for automated processing.

## Requirements

1. Scanned official ID and proof of address documents (mismatched to profile)
2. Active session from account creation
3. Patience for verification wait time

## Defense

Defensive measures and detection strategies:

- Integrate document OCR/extraction with profile data validation
- Manual review for high-risk verifications (e.g., trading limits)
- Anomaly detection on document-profile mismatches via AI

## Objectives

1. Bypass identity matching in KYC
2. Obtain verified account status
3. Enable subsequent profile manipulation

## Instructions

### Step 1: Select and Upload ID Document

**Context**: Choose document type and upload mismatched ID to initiate proof submission.

No command; web upload:
- In verification form, select "ID Card".
- Upload file of official ID not matching entered name/DoB.

> Upload succeeds; proceeds to next step.

### Step 2: Upload Proof of Address

**Context**: Submit address proof aligned with ID but conflicting with profile.

No command; web upload:
- Select proof type (e.g., utility bill).
- Upload document matching ID address but not profile address.

> Both documents queued for verification.

### Step 3: Submit and Wait for Approval

**Context**: Finalize submission and monitor for automated approval.

No command; keep session active:
- Click submit; interact with site (e.g., refresh dashboard) to maintain cookies.
- Wait 15-30 minutes; refresh verification status.

> Status changes to "completed" despite mismatches.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Impair Defenses]] Impair Defenses

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- kyc-exploit
- document-fraud
