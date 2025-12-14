---
tags:
  - recon
  - web
  - api
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 18167d37-ccb8-43d4-8bdf-73e450c76e39
created_at: '2025-12-14T03:15:10.058Z'
updated_at: '2025-12-14T03:15:10.058Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Promo-Page-and-Trigger-API-Request

## Summary

This procedure involves accessing the inDrive promo page to trigger a legitimate API request, establishing the baseline for identifying the vulnerable endpoint structure.

## Description

The attack scenario targets the promo page at https://promo.indrive.com/10ridestogetprize_ru/random. By navigating to this page and clicking the 'Сгенерировать' button, a GET request is generated to the API endpoint https://id.indrive.com/api/ten-drives/custom-winners/ten_drive_kz_second_weeks/number_trips/29/5/phone. This step confirms the endpoint's behavior without injection, setting up for subsequent SQLi tests in a web environment using PostgreSQL backend.

## Requirements

1. Web browser or HTTP client like curl for request simulation
2. Public access to https://promo.indrive.com
3. No authentication needed

## Defense

Defensive measures and detection strategies:

- Implement web application firewall (WAF) to monitor promo page interactions
- Log all API requests from promo pages for anomaly detection

## Objectives

1. Generate and observe a legitimate API response
2. Identify the exact URL path structure for injection points
3. Validate endpoint accessibility

## Instructions

### Step 1: Navigate to Promo Page

**Context**: Open the promo page in a browser to simulate user interaction.

**Instructions**: Visit https://promo.indrive.com/10ridestogetprize_ru/random and click 'Сгенерировать' to trigger the API request.

> This generates a GET request with path parameters like /number_trips/29/5/phone, returning JSON data.

### Step 2: Capture the Request

**Context**: Use browser dev tools or curl to replicate the request.

**Instructions**: Replicate the request using curl if needed, but primarily observe the response.

> Expected output: JSON with promo winner data.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/curl]]

## Tags

- [[recon]]
- [[web]]
