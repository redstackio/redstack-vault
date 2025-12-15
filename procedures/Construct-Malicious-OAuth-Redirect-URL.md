---
id: proc-respondly-url-construct-001
name: Construct-Malicious-OAuth-Redirect-URL
type: procedure
verified: false
submitted: true
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:35.352Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - open-redirect
  - oauth
  - url-crafting
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: medium
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Construct-Malicious-OAuth-Redirect-URL

## Summary

This procedure involves crafting a malicious URL for Respondly's Twitter OAuth endpoint by exploiting the unvalidated 'requestTokenAndRedirect' parameter, allowing redirection to an arbitrary attacker-controlled domain.

## Description

The vulnerability stems from Respondly's use of the Meteor framework's OAuth1 implementation, which fails to whitelist or validate redirect domains. By setting 'requestTokenAndRedirect' to an external URL, an attacker can initiate the OAuth flow and redirect the victim post-authorization to a malicious site. This is tested by constructing and accessing the URL in a browser, confirming the flow proceeds without blocking the redirect.

## Requirements

1. Access to Respondly's OAuth endpoint (https://app.respond.ly/_oauth/twitter/)
2. Control over a domain to host the redirect target
3. Web browser for URL construction and testing

## Defense

Defensive measures and detection strategies:

- Implement domain whitelisting for redirect parameters in OAuth flows
- Validate all redirect URIs against a strict allowlist
- Monitor for unusual redirects in application logs

## Objectives

1. Create a functional malicious URL that bypasses redirect validation
2. Verify the URL initiates the OAuth process correctly
3. Prepare for victim redirection to attacker site

## Instructions

### Step 1: Identify the Vulnerable Endpoint

**Context**: Locate the Twitter OAuth initiation point in Respondly.

The base endpoint is https://app.respond.ly/_oauth/twitter/.

### Step 2: Append Malicious Redirect Parameter

**Context**: Modify the URL to include the unvalidated parameter pointing to your controlled domain.

Construct the full URL:

https://app.respond.ly/_oauth/twitter/?requestTokenAndRedirect=https://your-attacker-domain.com/callback

### Step 3: Test the Constructed URL

**Context**: Verify the URL loads and starts the OAuth flow without errors.

Open the URL in a browser. It should redirect to Twitter's authorization page if the parameter is accepted.

**Expected Output**: OAuth flow begins, confirming redirect acceptance.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[open-redirect]]
- [[oauth]]
- [[url-crafting]]
