---
tags:
  - verification
  - impact-assessment
  - wordpress
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
  - '[[Browser Bookmark Discovery]]'
updated_at: '2025-12-14T17:27:42.750Z'
skill_level: low
impact_level: medium
detection_risk: low
sub_techniques: []
id: 7ec78a62-87c3-4b12-9e96-ec1ea9b474db
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Browser Bookmark Discovery]]'
---
# Verify-WordPress-Background-Image-Change

## Summary

This procedure checks the success of the CSRF exploitation by inspecting the WordPress site's homepage for the altered background image, confirming the theme modification.

## Description

Post-exploitation, the custom_background option in wp_options table is updated, applying the new image via CSS (background-image: url(...); background-repeat: repeat;). A repeating thumbnail can mask text, causing readability issues and alerting admins to the change.

## Requirements

1. Access to view the target site's frontend (https://[WP]/)
2. Knowledge of the targeted attachment_id and expected visual effect
3. Browser dev tools for CSS inspection

## Defense

Defensive measures and detection strategies:

- Regularly audit theme customizer settings for unauthorized changes
- Implement integrity checks on media attachments used in themes
- Use monitoring tools to alert on option table modifications
- Revert changes via admin panel and investigate logs

## Objectives

1. Confirm the background has been set to the malicious image
2. Assess disruption level (e.g., text obscuration)
3. Document impact for reporting or further exploitation

## Instructions

### Step 1: Visit Site Homepage

**Context**: Load the frontend to observe the applied theme change.

Navigate to https://[WP]/ in a browser.

> Expected: Background image from attachment_id=5 visible, repeating across the page.

### Step 2: Inspect and Validate

**Context**: Use dev tools to confirm the CSS update.

Right-click > Inspect Element > Check body or #page styles for background-image url matching the media file.

> Expected: CSS shows url(https://[WP]/wp-content/uploads/...-5-thumbnail.jpg); background-repeat: repeat; obscuring content if image is suitable.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Browser Bookmark Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[verification]]
- [[wordpress]]
- [[Impact]]
