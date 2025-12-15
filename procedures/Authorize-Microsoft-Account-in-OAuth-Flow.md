---
tags:
  - oauth-authorization
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
  - Mobile
techniques:
  - '[[Network Device Authentication]]'
skill_level: basic
impact_level: medium
detection_risk: low
sub_techniques: []
id: e4da6227-3b75-43a7-8ba5-6eeb2aa38e02
created_at: '2025-12-14T17:31:31.009Z'
updated_at: '2025-12-14T17:31:31.009Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Network Device Authentication]]'
---
# Authorize-Microsoft-Account-in-OAuth-Flow

## Summary

This procedure handles the Microsoft side of the OAuth flow, logging in and granting permissions to generate the authorization code in the returning deep link.

## Description

The browser redirect prompts for Microsoft credentials and consent to email access. Upon approval, Microsoft issues the code via the shopapp:// URI, which is vulnerable to hijacking due to lack of PKCE.

## Requirements

1. Valid Microsoft Outlook credentials
2. Browser access during redirect
3. Permissions for email read access

## Defense

Defensive measures and detection strategies:

- Require PKCE for mobile OAuth clients
- Scope permissions minimally
- Alert on unusual authorization attempts

## Objectives

1. Authenticate the Microsoft account
2. Grant necessary scopes (e.g., Mail.Read)
3. Return the authorization code via deep link

## Instructions

### Step 1: Enter Credentials

**Context**: Log in to Microsoft in the opened browser.

Provide email and password.

**Expected Output**: Account verified.

### Step 2: Review Permissions

**Context**: Authorize the Shop App's requested scopes.

Review and approve access to emails.

**Expected Output**: Consent granted.

### Step 3: Complete Redirect

**Context**: Allow the redirect to the deep link.

Browser closes or hands off to app.

**Expected Output**: OS modal for app selection appears.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Network Device Authentication]] Network Device Authentication

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[oauth-authorization]]
