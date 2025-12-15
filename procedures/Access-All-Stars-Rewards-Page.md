---
id: proc-access-rewards-page-1070510
tags:
  - unauthorized-access
  - rewards-abuse
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:36.354Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-All-Stars-Rewards-Page

## Summary

This procedure accesses the Streamlabs All Stars rewards page with tampered API responses active, unhiding the redeem button for non-Prime users and enabling reward exploitation.

## Description

The rewards page at https://streamlabs.com/dashboard#/streamlabs-rewards?skipPrimeOnboarding=1 relies on the Prime API response to toggle UI elements. With Burp's modifications, the client-side JavaScript treats the user as subscribed, exposing the redemption interface for unlimited high-value items like Logitech coupons.

## Requirements

1. Active Burp proxy with Match and Replace rules configured
2. Logged-in Streamlabs session
3. Valid email for reward delivery

## Defense

Defensive measures and detection strategies:

- Server-side enforcement of subscription before reward issuance
- Anomaly detection on redemption rates per account/IP
- Two-factor confirmation for high-value redemptions

## Objectives

1. Unlock hidden rewards UI via bypass
2. Prepare for multiple redemptions
3. Demonstrate financial impact potential

## Instructions

### Step 1: Ensure Proxy is Active

**Context**: Confirm Burp is intercepting traffic before navigating.

Verify in Burp's Proxy tab that the listener is running and browser proxy is set.

### Step 2: Navigate to Rewards Page

**Context**: Load the page that triggers the Prime check.

In the proxied browser, go to https://streamlabs.com/dashboard#/streamlabs-rewards?skipPrimeOnboarding=1.

**Expected Output**: Page loads with 'redeem' button visible, no Prime upgrade prompt.

### Step 3: Verify Unlock

**Context**: Interact to confirm bypass success.

Attempt to hover or click elements; inspect page source for unhidden Prime sections.

**Expected Output**: Full rewards catalog accessible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[unauthorized-access]]
- [[rewards-abuse]]
