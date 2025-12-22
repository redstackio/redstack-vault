---
tags:
  - css-injection
  - bbcode
  - payload
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 1a264e1a-9cd5-4dad-8441-2eeaaadc6f44
created_at: '2025-12-13T23:52:24.856Z'
updated_at: '2025-12-13T23:52:24.856Z'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inject-Arbitrary-CSS-Properties-Using-BBcode

## Summary

This procedure exploits the CSS injection in phpBB's style BBcode tag by injecting arbitrary CSS properties to create overlay elements, enabling visual manipulation of the forum page.

## Description

By crafting BBcode payloads with CSS like position:fixed and z-index, attackers can place elements over the page content. The input is inserted into a span's style attribute post-quote removal, allowing properties such as background-image for deceptive overlays (e.g., a skull image). This is performed via forum posts viewable by others, leading to UI redressing. Requires posting access on a vulnerable phpBB instance.

## Requirements

1. phpBB account with post creation rights.
2. Knowledge of CSS for payload design.
3. Target forum URL accessible.

## Defense

Defensive measures and detection strategies:

- Filter CSS properties to a safe subset (e.g., only font, color).
- Escape or validate all style attribute inputs server-side.
- Use WAF rules to block suspicious BBcode in posts.

## Objectives

1. Inject CSS to alter element positioning and layering.
2. Create overlays for visual deception.
3. Demonstrate potential for misleading user interactions.

## Instructions

### Step 1: Craft Payload

**Context**: Design CSS to overlay an image across the page.

Use BBcode: [style=position:fixed; top:0; left:0; z-index:9999; background-image:url(https://attacker.com/skull.png); width:100%; height:100%; opacity:0.8][/style]. This positions a semi-transparent skull image on top.

> Payload focuses on fixed positioning to ignore normal flow.

### Step 2: Post and Verify

**Context**: Submit the payload in a forum thread and load the page.

Create a new post with the BBcode, publish it, and refresh the thread view.

> Expected: Span renders with styles applied, overlaying the skull image over forum content.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[css-injection]]
- [[bbcode]]
- [[payload]]
