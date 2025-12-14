---
tags:
  - api-settings
  - token-invalidation
  - privilege-escalation
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:29:57.348Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 8a3c2933-b275-4721-bb5b-792fdb76e786
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Access-Restricted-API-Settings-and-Refresh-Token

## Summary

This procedure bypasses admin menu restrictions in Streamlabs by directly navigating to the owner's API settings page, allowing the admin to refresh and invalidate the API access token, which disrupts streaming integrations.

## Description

From the impersonated admin view, directly enter the URL for the API settings endpoint, which is not visible in the admin menu due to insufficient access controls. The page loads, showing an empty token field, and the 'Refresh' button is clickable, generating a new token and invalidating the old one. This affects widgets like alert boxes, donation goals, and OBS Studio integrations, potentially halting live streams. Prerequisites: Impersonated access from prior steps. Expected outcomes: Token invalidated, leading to API request failures.

## Requirements

1. Impersonated admin access to owner's account
2. Knowledge of the direct URL: https://streamlabs.com/dashboard#/settings/api-settings
3. Web browser for URL navigation

## Defense

Defensive measures and detection strategies:

- Implement URL-based authorization checks on all endpoints
- Restrict 'Refresh' actions to owner role only
- Monitor API token changes and correlate with user roles

## Objectives

1. Access hidden owner-only settings as admin
2. Manipulate API token to cause disruptions
3. Achieve denial-of-service on streaming features

## Instructions

### Step 1: Direct Navigation to API Settings

**Context**: Bypass the admin menu by entering the restricted URL directly.

In the impersonated dashboard, manually type or paste https://streamlabs.com/dashboard#/settings/api-settings into the address bar and press Enter.

> The page loads despite not being linked in the admin interface, revealing the API token management section.

### Step 2: Refresh and Invalidate Token

**Context**: Use the exposed interface to generate a new token, invalidating the existing one.

Locate the empty token field and click the 'Refresh' button to create a new API Access Token.

> This action immediately invalidates the old token, breaking any active integrations reliant on it, such as OBS widgets during a live stream.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- url-bypass
- token-manipulation
- stream-disruption
