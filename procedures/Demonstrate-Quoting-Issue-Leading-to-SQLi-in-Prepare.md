---
id: proc-quoting-issue-demo
tags:
  - sqli
  - information-disclosure
  - wordpress
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/test-quoting-flaw-in-prepare]]'
verified: false
platforms:
  - Web
  - WordPress
  - PHP
  - MySQL
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:19.773Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Demonstrate-Quoting-Issue-Leading-to-SQLi-in-Prepare

## Summary

This procedure shows how the quoting of %s placeholders in $wpdb->prepare() allows breaking out of strings when user input is involved, enabling SQL injection for information disclosure.

## Description

Queries using prepare() with quoted user input and %s can be injected by crafting input that closes the quote early. Demonstrated in bbPress or custom queries, this leads to data extraction. Requires a vulnerable WordPress setup; reference attachment dh1.php for PoC.

## Requirements

1. User input field accepting strings (e.g., bbPress post title)
2. Access to trigger prepared queries
3. MySQL database for impact verification

## Defense

Defensive measures and detection strategies:

- Parameterize all queries without relying on %s quoting
- Input validation to strip SQL keywords
- WAF rules to block common SQLi patterns in POST data

## Objectives

1. Craft payload to breakout quotes
2. Achieve SQL injection
3. Extract sensitive data like user info

## Instructions

### Step 1: Identify Quoted Query

**Context**: Find a prepare() call with VALUES (%s) or similar.

In bbPress, look for insert queries with user post data.

### Step 2: Inject Payload

**Context**: Submit input like "' OR 1=1; --" via form.

Simulate with custom code using [[commands/test-quoting-flaw-in-prepare]]:

```php
// In a test script
$wpdb->prepare("SELECT * FROM wp_posts WHERE title = '%s'", $user_input);
// $user_input = "test' OR '1'='1"
```

> Quoting becomes 'test' OR '1'='1', injecting the condition. Expected output: All posts returned due to true condition.

### Step 3: Verify Disclosure

**Context**: Check query results for leaked data.

Monitor $wpdb->last_query for the injected string.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/test-quoting-flaw-in-prepare]]

## Tools Used


## Tags

- sqli
- information-disclosure
- wordpress
