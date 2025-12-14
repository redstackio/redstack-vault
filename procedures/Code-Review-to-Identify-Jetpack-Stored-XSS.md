---
id: proc-jetpack-code-review-001
tags:
  - code-review
  - xss
  - wordpress
  - jetpack
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - WordPress
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:39.035Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Code-Review-to-Identify-Jetpack-Stored-XSS

## Summary

This procedure involves statically analyzing Jetpack's Simple Payments module code to identify a stored XSS vulnerability arising from unsanitized output of post meta in shortcode rendering, enabling low-privilege users to inject scripts.

## Description

In WordPress environments with Jetpack premium, the Simple Payments module registers a custom post type for products with edit permissions for contributors and authors. Post meta like 'spay_formatted_price' can be set arbitrarily without validation. The shortcode rendering function outputs this meta directly into HTML without escaping, creating a stored XSS vector. This procedure details reviewing the relevant code paths to confirm the issue, typically done by downloading the Jetpack plugin and inspecting PHP files.

## Requirements

1. Access to Jetpack plugin source code (download from WordPress.org or GitHub)
2. PHP/WordPress knowledge for code analysis
3. Text editor or IDE for searching code

## Defense

Defensive measures and detection strategies:

- Sanitize all post meta outputs using esc_html() or similar in shortcodes
- Restrict custom post type capabilities to higher roles
- Enable Content Security Policy (CSP) to block inline scripts
- Monitor for anomalous JavaScript in post meta via audits

## Objectives

1. Confirm edit permissions on product post type for low-privilege users
2. Trace unsanitized data flow from post meta to HTML output
3. Identify lack of escaping in format_price and output_shortcode functions

## Instructions

### Step 1: Review Post Type Registration

**Context**: Examine how the product post type is registered to understand permissions and supported fields.

Locate the register_post_type call for 'self::$post_type_product' in Jetpack's Simple Payments files (e.g., modules/simple-payments/simple-payments.php). Note capabilities like 'edit_post' granted to contributors/authors and support for 'custom-fields'.

**Expected Output**: Code snippet showing open permissions on meta fields.

### Step 2: Analyze Meta Setting Mechanisms

**Context**: Verify that low-privilege users can set arbitrary meta without validation.

Search for wp_ajax_add_meta handler or custom fields interface. Confirm users with 'edit_posts' can set keys like 'spay_formatted_price' via AJAX without checks.

**Expected Output**: Documentation or code confirming no validation on meta values.

### Step 3: Inspect Shortcode Output

**Context**: Trace the rendering path to find unsanitized output.

In the output_shortcode function, locate `<div class='${css_prefix}-price'><p>{$data['price']}</p></div>`. Check parse_shortcode method where $data['price'] pulls from get_post_meta('spay_formatted_price', true) and passes to format_price without escaping.

**Expected Output**: Confirmation of direct HTML insertion of meta value.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- code-review
- xss
- wordpress
