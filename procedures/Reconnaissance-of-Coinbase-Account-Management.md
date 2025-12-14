---
tags:
  - reconnaissance
  - web
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Gather Victim Host Information]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 057904aa-e24d-4481-b51c-27e836cc1e1c
created_at: '2025-12-14T17:27:15.811Z'
updated_at: '2025-12-14T17:27:15.811Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Reconnaissance-of-Coinbase-Account-Management

## Summary

This procedure involves inspecting Coinbase's accounts page to understand account management features, identifying state-changing actions, and noting protection differences like CSRF tokens on POST vs. unprotected GET requests.

## Description

In a web-based environment like Coinbase, reconnaissance reveals vulnerabilities in account management. By navigating to https://coinbase.com/accounts, an attacker observes options to create, rename, delete, or set accounts as primary. Delete actions use secure POST with CSRF tokens, but 'set as primary' uses vulnerable GET requests relying only on session cookies, enabling CSRF attacks. This step is prerequisite for targeted exploitation.

## Requirements

1. Access to a logged-in Coinbase session
2. Browser with developer tools enabled
3. Basic knowledge of HTTP requests

## Defense

Defensive measures and detection strategies:

- Implement consistent CSRF protection on all state-changing endpoints
- Monitor for anomalous account management requests
- Use web application firewalls to detect unusual GET-based modifications

## Objectives

1. Map account management endpoints and methods
2. Identify protection gaps for exploitation
3. Gather intel on multi-account handling

## Instructions

### Step 1: Navigate to Accounts Page

**Context**: Access the target page to view management options.

Log in to Coinbase and visit https://coinbase.com/accounts. Create multiple test accounts if needed to observe features.

### Step 2: Inspect Management Actions

**Context**: Use dev tools to analyze request methods for each action.

Right-click on 'Set as primary' and inspect the network request. Confirm it's a GET to /accounts/<id>/set_as_primary without tokens. Compare with delete, which is POST with CSRF.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Reconnaissance]]
- [[web]]
