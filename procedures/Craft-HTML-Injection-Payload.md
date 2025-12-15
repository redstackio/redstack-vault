---
tags:
  - payload-crafting
  - html-injection
  - phishing
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:36.075Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: a6fab6c6-3a8c-4c0b-bf08-cac83096d2eb
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Craft-HTML-Injection-Payload

## Summary

This procedure details the creation of a malicious HTML payload targeting the 'keyword' parameter, designed to inject persistent content like phishing links into search results while evading partial XSS filters.

## Description

Given the lack of full input sanitization in the PHP backend, craft HTML that renders without escaping, such as anchor tags linking to external phishing sites. The payload must survive storage and display on the results page, persisting across refreshes. Use entity encoding to bypass basic filters. Primary use case: Enabling social engineering via injected links visible to all users searching case studies.

## Requirements

1. Knowledge of HTML encoding (e.g., URL, HTML entities)
2. Text editor or online encoder for payload preparation
3. Understanding of the target's partial protections (e.g., XSS blocked but HTML allowed)

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs with HTML entity encoding on server-side
- Use content security policy (CSP) to restrict inline HTML rendering
- Scan stored content for suspicious tags before display

## Objectives

1. Generate a functional HTML injection string
2. Ensure compatibility with the vulnerable parameter
3. Test for persistence in search results

## Instructions

### Step 1: Design Raw Payload

**Context**: Create a simple phishing link that mimics legitimate content.

Example raw HTML: <a href="https://evil.site">Click here to win 1000$!</a>

> This will render as a clickable link if injected successfully.

### Step 2: Encode for Submission

**Context**: Apply URL and HTML entity encoding to evade filters and ensure transmission.

Encoded version: &lt;a&#32;href&#61;https&#58;&#47;&#47;evil&#46;site&gt;Click&#32;here&#32;to&#32;win&#32;1000&#36;&#33;&lt;&#47;a&gt;

> Paste into the 'keyword' field during testing; verify reflection in results page source.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[payload-crafting]]
- [[html-injection]]
