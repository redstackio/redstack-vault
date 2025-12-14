---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - listing-creation
  - api-trigger
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:29.114Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Test-Product-Listing

## Summary

This procedure creates a new unpublished product listing on Reverb.com to trigger and observe the vulnerable API endpoint, capturing the request format for later manipulation.

## Description

Using the authenticated session, a test listing is created via the web interface, which internally calls the /api/listings/{id}/product_bundle endpoint. This reveals the JSON structure of listing data and provides a legitimate request example. The target is the sandbox environment, where listings remain unpublished. Outcomes include obtaining a listing ID and understanding API responses, setting up for IDOR exploitation.

## Requirements

1. Authenticated session from previous procedure
2. Access to listing creation UI
3. Basic product details (e.g., title, description)

## Defense

Defensive measures and detection strategies:

- Log all listing creation events with user IDs
- Validate input data during creation
- Alert on rapid listing creations from single accounts

## Objectives

1. Trigger the API endpoint to capture request
2. Obtain a sample listing ID
3. Confirm JSON response format

## Instructions

### Step 1: Start New Listing

**Context**: Use the web UI to initiate listing creation.

No command; browser-based:

- Navigate to listings/create
- Enter product details (e.g., guitar, unpublished status)
- Save the listing

> API call triggers, response includes JSON with ID (e.g., {own_id}).

### Step 2: Inspect Response

**Context**: Review the created listing details.

Check the listing page or network tab for the API response.

> Expected: JSON with product_bundle data, confirming endpoint behavior.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[listing-creation]]
- [[api-trigger]]
- [[web]]
