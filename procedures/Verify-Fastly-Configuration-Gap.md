---
tags:
  - fastly
  - configuration
  - recon
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T04:51:26.666Z'
sub_techniques:
  - '[[Hardware]]'
id: 61eb2d1d-f8c2-4377-a959-d81221f0f307
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Verify-Fastly-Configuration-Gap

## Summary

This procedure checks if a CDN like Fastly has explicitly configured a subdomain in its service domains, identifying gaps that allow takeovers.

## Description

CDNs like Fastly use SNI to route traffic, but if a CNAME points to their infra without the subdomain listed in the service's domains, anyone can claim it. In this attack, verification shows registry.nodejs.org missing from the official service, enabling exploitation. Outcomes: Confirmation of vulnerability for takeover.

## Requirements

1. Fastly service ID or public access to the official domain (registry.npmjs.org)
2. Browser or curl for header inspection
3. Knowledge of Fastly's domain management

## Defense

Defensive measures and detection strategies:

- Add all CNAME subdomains to CDN service domains explicitly
- Enable automatic domain verification and alerts for additions
- Scan for dangling subdomains regularly with tools like dnsrecon

## Objectives

1. Inspect official Fastly service for subdomain inclusion
2. Confirm absence of protection
3. Assess takeover feasibility

## Instructions

### Step 1: Inspect Official Domain Headers

**Context**: Access the protected domain to understand service behavior.

Use a browser or curl to fetch https://registry.npmjs.org and check Fastly-specific headers like Server: Varnish or Fastly headers.

### Step 2: Attempt Subdomain Access

**Context**: Test if the subdomain resolves to the official service.

Visit https://registry.nodejs.org; if it 404s or doesn't match official content, a gap exists.

**Expected Output**: Mismatch in response, indicating no config for the subdomain.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Hardware

### Sub-Techniques

- [[Hardware]] Gather Victim Host Information: Hardware

## Commands Used

- None

## Tools Used

- None

## Tags

- [[fastly]]
- [[recon]]
