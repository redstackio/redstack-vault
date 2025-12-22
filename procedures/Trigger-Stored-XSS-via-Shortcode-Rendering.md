---
id: proc-jetpack-trigger-xss-001
tags:
  - xss-trigger
  - shortcode
  - wordpress
  - jetpack
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - WordPress
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:39.030Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-via-Shortcode-Rendering

## Summary

This procedure triggers the stored XSS by embedding the [simple-payment] shortcode in a post, causing the unsanitized post meta payload to render and execute JavaScript in the viewer's browser upon page load.

## Description

Once the payload is stored in a product post's meta, any user viewing a post with the shortcode referencing that product will have the price field output directly, executing the script. This affects all viewers, including admins, enabling theft of session cookies or further attacks like keylogging.

## Requirements

1. Access to edit any post (author role)
2. Product post ID with injected payload
3. Target post to insert shortcode

## Defense

Defensive measures and detection strategies:

- Escape shortcode outputs with esc_html() or wp_kses_post()
- Audit shortcode usage and restrict to trusted posts
- Implement browser-based XSS filters or CSP
- Log and alert on script execution attempts via WAF

## Objectives

1. Render the shortcode to output the payload
2. Execute JavaScript in victim browser
3. Achieve session hijacking or escalation

## Instructions

### Step 1: Insert Shortcode in Post

**Context**: Add the shortcode to a visible post to trigger rendering.

Edit a post (e.g., a blog entry) and insert `[simple-payment id="123"]` where 123 is the product post ID with the payload. Save the post.

**Expected Output**: Shortcode embedded without errors.

### Step 2: View the Post

**Context**: Load the post in a browser to execute the payload.

Visit the published post URL as a target user (e.g., admin). The shortcode processes, fetches meta, formats price without escaping, and outputs to HTML.

**Expected Output**: JavaScript executes, e.g., alert pops or network request to steal data.

### Step 3: Verify Execution

**Context**: Confirm impact using browser tools.

Use developer console to check for errors or executed scripts. Test with payload targeting document.cookie for proof.

**Expected Output**: Console logs or network tabs show payload effects.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss-trigger
- shortcode
- wordpress
