---
tags:
  - onboarding
  - shopify
type: procedure
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques: []
updated_at: '2025-12-13T23:52:43.847Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 57c31f93-bbf9-476e-94a0-5e8b675323b9
validated: true
mitre_tactics:
  - '[[Initial Access]]'
---
# Access-Shopify-Collabs-Onboarding-Page

## Summary

This procedure follows account creation by accessing the Shopify Collabs onboarding page, where profile setup begins.

## Description

After new account registration, the platform redirects to the onboarding interface at https://collabs.shopify.com/onboarding. This step confirms the redirect and loads the page, preparing for social media connection and profile editing. It's a non-exploitative setup phase in the chain leading to authenticated XSS exploitation.

## Requirements

1. Recently created Shopify account
2. Active browser session
3. Internet connectivity

## Defense

Defensive measures and detection strategies:

- Session timeout on incomplete onboarding
- Log access to onboarding endpoints
- Verify user agent and referer headers

## Objectives

1. Load the onboarding page
2. Confirm post-registration redirect
3. Prepare for profile completion

## Instructions

### Step 1: Follow Post-Registration Redirect

**Context**: Allow the browser to navigate automatically after account creation.

Do not interrupt the redirect; let the page load.

> Loads https://collabs.shopify.com/onboarding. Expected output: Onboarding interface with setup prompts.

### Step 2: Verify Page Accessibility

**Context**: Ensure the page is fully loaded and interactive.

Check for elements like social media connection buttons.

> Page is ready for input. Expected output: Visible onboarding steps.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques


### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[onboarding]]
- [[shopify]]
- [[web]]

