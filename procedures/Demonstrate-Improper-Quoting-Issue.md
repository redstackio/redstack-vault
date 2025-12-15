---
id: proc-quoting-breakout-sqli
tags:
  - sqli
  - wordpress
  - quoting
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/test-quoting-breakout-prepare]]'
verified: false
platforms:
  - Web
  - PHP
  - MySQL
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:56.635Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Demonstrate Improper Quoting Issue

## Summary

This procedure demonstrates how $wpdb->prepare() improperly quotes %s placeholders in queries with pre-quoted user inputs, allowing attackers to break out of quotes and inject SQL in affected WordPress components.

## Description

When a query string already contains quoted user input (e.g., from esc_sql()), prepare() adds extra quotes around %s values, enabling escape via payloads like "'; MALICIOUS --". This affects plugins/themes using prepare() on such queries. Test in a controlled setup by constructing a vulnerable query and observing injection success, leading to broad SQLi across the ecosystem.

## Requirements

1. Custom PHP script or plugin to build quoted queries.
2. User-controlled input simulation via $_GET/$_POST.
3. MySQL with a test table containing quoted data.
4. WordPress debug mode for query inspection.

## Defense

Defensive measures and detection strategies:

- Avoid pre-quoting inputs before prepare(); let prepare() handle all escaping.
- Validate query strings for existing quotes before binding.
- Deploy SQLi scanners like sqlmap on development sites.
- Review plugin code for mixed esc_sql() and prepare() usage.

## Objectives

1. Exploit double-quoting to break out.
2. Inject SQL in placeholder-bound queries.
3. Achieve info disclosure via injected SELECT.

## Instructions

### Step 1: Construct Pre-Quoted Query

**Context**: Build a base query with esc_sql() on input.

Use $quoted_input = "'" . esc_sql($_POST['input']) . "'";

### Step 2: Apply Prepare with %s

**Context**: Bind the quoted input via prepare(), triggering extra quotes.

**Command** ([[commands/test-quoting-breakout-prepare]]):
```php
$input = "' OR '1'='1";
$quoted = "'" . esc_sql($input) . "'";
$query = $wpdb->prepare("SELECT * FROM wp_posts WHERE post_title = %s", $quoted);
$wpdb->query($query);
```

> Extra quotes allow breakout: "... = '' OR '1'='1''". Expected output: All posts returned due to tautology.

### Step 3: Confirm Breakout

**Context**: Analyze executed query for injection traces.

Log the final $query and verify payload integration.

**Expected Output**: Injected logic executes, bypassing filters.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/test-quoting-breakout-prepare]]

## Tools Used


## Tags

- sqli
- wordpress
- quoting
