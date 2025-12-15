---
id: proc-trigger-burp-rendering
tags:
  - burp-suite
  - html-rendering
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Desktop
  - Java
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:26:56.386Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-HTML-Rendering-in-Burp-Suite

## Summary

This procedure involves the victim interacting with a malicious HTTP request in Burp Suite's interface to activate the Swing HTML parser, which renders injected content and initiates external resource fetches.

## Description

The attack relies on social engineering to get the victim (e.g., pentester) to load the crafted request into Burp's Proxy intercept, HTTP history, or Repeater tab. Selecting or modifying the request triggers rendering, exploiting the lack of input sanitization in Swing's parser. This leads to client-side SSRF-like behavior, bypassing proxies. Expected outcomes include hidden network requests for leaks or exploits. Prerequisites: Victim running vulnerable Burp on a network with proxy configs.

## Requirements

1. Malicious request from prior procedure
2. Burp Suite access for victim
3. No special privileges needed

## Defense

Defensive measures and detection strategies:

- Train users to inspect requests in raw text mode
- Use Burp extensions to sanitize HTML
- Monitor Burp process for unexpected outbound traffic

## Objectives

1. Invoke Swing parser on injected HTML
2. Trigger resource loading without user awareness
3. Bypass upstream proxy/SOCKS settings

## Instructions

### Step 1: Intercept or Paste Request

**Context**: Victim loads the request into Burp Proxy or history.

**Command** (No CLI; UI-based):
Intercept traffic or paste crafted request into Proxy tab.

> Expected: Request displays in Burp interface.

### Step 2: Select or Send to Repeater

**Context**: Interaction forces rendering of content.

**Command** (UI):
Right-click request > Send to Repeater, then view/modify.

> Expected: HTML parsed, tags executed (e.g., img fetch starts).

### Step 3: Verify Trigger

**Context**: Confirm rendering occurs.

Monitor for visual changes or network activity.

> Expected: No visible alert, but backend fetches initiate.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript (adapted for HTML/Swing)

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[tools/Burp-Suite]]
- [[html-rendering]]
