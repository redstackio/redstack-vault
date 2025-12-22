---
id: proc-verify-vercel-claim
tags:
  - subdomain-takeover
  - vercel
  - claim
  - exploit
type: procedure
tools:
  - '[[tools/Vercel-Dashboard]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - DNS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:31.311Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify-and-Attempt-Subdomain-Claim

## Summary

This procedure verifies the claimability of a dangling subdomain on Vercel and attempts to add it to a project, confirming takeover vulnerability while noting any authorization blocks that prevent full hijacking.

## Description

In scenarios like the Sifchain report, this targets subdomains with CNAMEs to Vercel (e.g., dex2.sifchain.finance) lacking deployments. The technical approach involves the domain addition flow, revealing unowned status and potential for hosting malicious content like phishing pages. Outcomes include validation of the vulnerability, with impacts on reputation if successfully claimed.

## Requirements

1. Confirmed available subdomain from prior check
2. Vercel project ready for domain association
3. Understanding of DNS propagation (though not directly used here)

## Defense

Defensive measures and detection strategies:

- Verify all cloud subdomains with ownership proofs (e.g., Vercel TXT records)
- Set up alerts on DNS changes via providers like Cloudflare
- Conduct periodic subdomain takeover scans using tools like Subjack

## Objectives

1. Confirm no existing ownership or deployment
2. Attempt claim to test exploitability
3. Document blocks for informative reporting

## Instructions

### Step 1: Initiate Domain Addition

**Context**: Proceed with adding the subdomain to test ownership.

Click 'Add' or continue in the domains interface for the target subdomain.

> Expected output: Prompt for verification or error like 'DEPLOYMENT_NOT_FOUND'.

### Step 2: Observe Authorization Response

**Context**: Evaluate if claim succeeds or fails due to protections.

If prompted, attempt to verify; note any blocks from Vercel's checks.

> Expected output: Claim blocked, confirming dangling but protected status; potential for bypass research.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Vercel-Dashboard]]

## Tags

- claim-attempt
- verification
- takeover
