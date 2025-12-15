---
tags:
  - open-redirect
  - bypass
  - url-encoding
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:31.457Z'
sub_techniques: []
id: 07775d48-95b1-420f-bfaf-38752ccfd654
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass Open Redirect Protection with Double Slashes

## Summary

This procedure exploits a bypass in the open redirect protection of the 'path' parameter by using double slash encoding (%2F%2F), forcing a redirect to an external attacker-controlled site after a brief delay.

## Description

The Locksmith app on supporthiring.shopify.com includes protections against external redirects in the 'path' parameter, but these can be evaded by encoding double slashes. This allows attackers to craft phishing links that briefly show a 404 page before redirecting victims, facilitating social engineering across Shopify sites.

## Requirements

1. Identified vulnerable endpoint from prior reconnaissance.
2. Control over a malicious domain (e.g., evil.com).
3. Ability to URL-encode payloads.

## Defense

Defensive measures and detection strategies:

- Normalize URLs by decoding and validating against whitelists.
- Log and alert on encoded slash patterns in redirects.

## Objectives

1. Evade redirect filters.
2. Achieve external redirection.
3. Enable phishing attacks.

## Instructions

### Step 1: Craft Encoded Payload

**Context**: Encode the target domain to bypass internal path checks.

Use %2F%2Fevil.com as the path value.

> This tricks the app into treating it as an external URL.

### Step 2: Inject and Trigger

**Context**: Append to vulnerable URL and load.

Set the full URL to http://supporthiring.shopify.com/apps/locksmith/resource/pages/gauntlet-challenge?path=%2F%2Fevil.com.

> Expect a 2-second 404 before redirect to https://evil.com.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[open-redirect]]
- [[bypass]]
