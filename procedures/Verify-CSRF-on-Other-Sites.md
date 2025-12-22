---
id: proc-verify-csrf-other-sites
tags:
  - csrf
  - web
  - multi-site
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-endpoint-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:42.794Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify-CSRF-on-Other-Sites

## Summary

This procedure extends the CSRF test to related sites like Starbucks to confirm similar vulnerabilities in the shared Demandware infrastructure.

## Description

Test the endpoint https://store.starbucks.com/on/demandware.store/Sites-Starbucks-Site/default/Sites-Teavana-Site/default/GiftCert-Purchase for the same lack of protection and persistent impact. Scenario: Reuse POC on Starbucks; outcome: Consistent cart lockout.

## Requirements

1. Access to Starbucks site
2. Existing POC from prior procedure
3. HTTP client for verification

## Defense

Defensive measures and detection strategies:

- Standardize CSRF protections across all sites
- Conduct unified vulnerability scans
- Cross-reference endpoint behaviors

## Objectives

1. Replicate endpoint discovery
2. Confirm CSRF exploit success
3. Assess broader impact

## Instructions

### Step 1: Locate Starbucks Endpoint

**Context**: Search for equivalent URL on Starbucks.

**Command** ([[commands/curl-endpoint-test]]):
```bash
curl -X GET "https://store.starbucks.com/on/demandware.store/Sites-Starbucks-Site/default/Sites-Teavana-Site/default/GiftCert-Purchase"
```

> Retrieves page. Expected output: Similar form structure.

### Step 2: Test CSRF POC

**Context**: Adapt and submit POC to Starbucks.

Update POC action to Starbucks URL and test on logged-in account.

> Expected output: Cart locked, mirroring Teavana behavior.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-endpoint-test]]

## Tools Used


## Tags

- [[csrf]]
- [[web]]
- [[multi-site]]
