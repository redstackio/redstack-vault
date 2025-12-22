---
id: uuid-observe-oauth
tags:
  - oauth
  - recon
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:24:35.862Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Observe-Normal-OAuth-Flow

## Summary

This procedure involves monitoring the standard GitHub OAuth flow on edoverflow.com pages with the comments widget to understand how authorization codes are handled and stripped from URLs post-authentication.

## Description

In the target environment, a Jekyll-based site like edoverflow.com uses GitHub OAuth for comments widget login. On pages with the widget enabled (e.g., blog posts), successful authentication strips the code parameter from the URL, preventing leakage via Referer on external link clicks. This reconnaissance step identifies the normal behavior to contrast with manipulated flows. Prerequisites include access to a browser and the target site.

## Requirements

1. Web browser with developer tools
2. Access to target site (edoverflow.com or similar)
3. No authentication required initially

## Defense

Defensive measures and detection strategies:

- Monitor OAuth logs for unusual redirect patterns
- Implement strict redirect_uri validation beyond domain whitelisting

## Objectives

1. Confirm code stripping on widget pages
2. Identify safe vs. vulnerable flow differences
3. Prepare for manipulation testing

## Instructions

### Step 1: Navigate to Widget-Enabled Page

**Context**: Select a blog post page with comments to observe authentic flow.

**Command** (Browser Navigation):

Visit https://edoverflow.com/2017/[post-title]/ and click GitHub login.

> Initiates OAuth; after approval, observe URL change removing ?code= parameter.

### Step 2: Inspect Post-Auth URL

**Context**: Verify stripping prevents Referer leakage.

**Command** (Developer Tools):

Open Network tab and click an external link post-auth.

> Expected: No code in Referer header.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- oauth
- reconnaissance
