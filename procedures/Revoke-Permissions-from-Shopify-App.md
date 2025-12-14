---
tags:
  - shopify
  - permission-revocation
  - persistence-setup
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:32:11.025Z'
sub_techniques: []
id: 9e090e5c-6800-41d4-ae4e-200ec805061b
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Revoke-Permissions-from-Shopify-App

## Summary

This procedure revokes read permissions from a Shopify private app after webhook creation, exploiting the vulnerability where webhooks remain active and hidden, enabling persistence.

## Description

Following webhook setup, permissions are removed to simulate a cleanup or detection evasion scenario. Due to improper access control in Shopify's API, the webhook continues firing events without appearing in listings or the UI. This targets the Shopify Admin interface and API, assuming prior app creation. Outcomes include a seemingly cleaned environment while maintaining backdoor access to event data.

## Requirements

1. Existing private app with active read orders permission
2. Shopify admin access to edit app settings
3. No additional tools beyond browser access

## Defense

Defensive measures and detection strategies:

- Enforce automatic webhook deletion on permission changes via custom scripts or monitoring
- Audit API tokens periodically for mismatched permissions and active webhooks
- Enable detailed logging of permission modifications and correlate with webhook activity
- Use third-party tools to scan for orphaned webhooks not visible in standard queries

## Objectives

1. Remove read access to orders from the private app
2. Trigger the vulnerability by making the webhook invisible
3. Maintain functional persistence for future exfiltration

## Instructions

### Step 1: Edit Private App Permissions

**Context**: Navigate to the app settings and revoke the specific permission.

**Instructions**: In Shopify admin, go to Settings > Apps and sales channels > Develop apps, select the app, and under API access scopes, uncheck Read orders. Save changes.

> The UI updates without errors, but the webhook persists due to the flaw.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Account Manipulation]] Account Manipulation

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- shopify
- permission-revocation
- persistence-setup
