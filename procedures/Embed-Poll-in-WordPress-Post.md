---
tags:
  - xss
  - wordpress
  - embedding
  - stored-xss
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 7898d992-d0da-420f-b135-9d43b8861d3b
created_at: '2025-12-13T23:52:49.676Z'
updated_at: '2025-12-13T23:52:49.676Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Embed-Poll-in-WordPress-Post

## Summary

This procedure embeds the malicious Crowdsignal poll link into a WordPress.com post, leveraging the integration to store the XSS payload persistently in a blog context where victims are likely to interact.

## Description

WordPress.com allows seamless embedding of Crowdsignal polls via links, which renders the poll inline without re-sanitizing the content. The attacker creates a new post, pastes the poll link, and the malicious answer from the prior procedure is displayed. This step bridges the poll creation to victim exposure, assuming the attacker has posting access on WordPress.com. The expected outcome is a published post containing the exploitable poll.

## Requirements

1. WordPress.com account with post creation privileges
2. The shareable poll link from Crowdsignal
3. Web browser for post editing

## Defense

Defensive measures and detection strategies:

- Scan embedded content for script tags or event handlers before rendering
- Restrict third-party embeds to trusted sources only
- Audit posts for suspicious links via moderation tools

## Objectives

1. Integrate the stored XSS payload into a viewable WordPress post
2. Ensure the poll renders with the malicious answer intact
3. Set up for social engineering to drive victim traffic

## Instructions

### Step 1: Access WordPress Posts

**Context**: Start a new post for embedding.

Navigate to https://wordpress.com/posts and click to add a new post.

### Step 2: Insert Poll Link

**Context**: Embed the malicious poll within post content.

In the post editor, paste the copied Crowdsignal poll link into the body text. WordPress will automatically convert it to an embedded poll.

### Step 3: Save Post as Draft

**Context**: Verify embedding without publishing yet.

Save the post as a draft and preview to confirm the poll displays with the injected answer visible but not triggered.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[wordpress]]
- [[embedding]]
- [[stored-xss]]
