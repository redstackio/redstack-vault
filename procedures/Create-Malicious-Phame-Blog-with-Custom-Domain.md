---
id: proc-1
tags:
  - open-redirect
  - phabricator
  - phame
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:24:35.299Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Create-Malicious-Phame-Blog-with-Custom-Domain

## Summary

This procedure sets up a Phame blog post in Phabricator using a custom domain controlled by the attacker, enabling the blog to be served from the attacker's server while mimicking Phabricator's URL structure. This misconfiguration allows subsequent redirects to preserve sensitive URL fragments like OAuth tokens.

## Description

Phabricator's Phame feature permits users to configure custom domains for blogs without sufficient validation, allowing an attacker with a Phabricator account to point a blog post to their own server. When combined with OAuth flows, this leads to an open redirect where the victim's browser fetches content from the attacker's domain, exposing URL anchors. The procedure assumes the attacker has a Phabricator account and controls a domain (e.g., files.nirgoldshlager.com) with a server capable of proxying or logging requests. Expected outcome: A live blog post accessible via the custom domain that can intercept redirects.

## Requirements

1. Valid Phabricator account with Phame blogging permissions
2. Control over a custom domain and web server to host the blog endpoint
3. Access to Phabricator's Phame creation interface (e.g., https://secure.phabricator.com/phame/blog/new/)

## Defense

Defensive measures and detection strategies:

- Validate and restrict custom domain configurations in Phame to trusted domains only
- Monitor for unusual custom domain setups in Phabricator logs
- Implement strict redirect_uri validation in OAuth integrations to block untrusted domains

## Objectives

1. Establish a foothold for redirect-based attacks via custom domain
2. Prepare for token capture by serving Phabricator-like content from attacker server
3. Enable preservation of URL fragments across browser redirects

## Instructions

### Step 1: Access Phame Blog Creation

**Context**: Log in to the target Phabricator instance and navigate to create a new blog to configure the custom domain.

Browse to https://secure.phabricator.com/phame/blog/new/ and authenticate if needed. Fill in basic blog details like title and description.

> No command executed; use web interface. Expected: Blog creation form loaded.

### Step 2: Configure Custom Domain

**Context**: Set the blog to use the attacker's controlled domain, enabling external serving of Phabricator URLs.

In the blog settings, enter the custom domain (e.g., files.nirgoldshlager.com). Save and publish a simple post (e.g., post ID 47).

> No command; web form submission. Expected: Confirmation of custom domain activation.

### Step 3: Verify Setup

**Context**: Test that the blog post is accessible via the custom domain while retaining Phabricator's path structure.

Visit https://files.nirgoldshlager.com/phame/live/47/ in a browser. Ensure it loads Phabricator content or a proxy setup on your server.

> Manual verification. Expected: Page loads without errors, confirming redirect potential.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[open-redirect]]
- [[phabricator]]
- [[phame]]
