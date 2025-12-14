---
id: analyze-drupal-query-001
tags:
  - reconnaissance
  - drupal
  - sql-injection
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T03:46:20.035Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Analyze Drupal Database Query Preparation for IN Statements

## Summary

This procedure involves static analysis of Drupal 7's database API to identify vulnerabilities in query preparation for IN clauses, specifically how the expandArguments function mishandles associative arrays with non-integer keys, enabling SQL injection.

## Description

In the context of auditing Drupal 7 sites, this procedure targets the expandArguments function in the database API, which prepares placeholders for db_query calls. When IN clauses receive associative arrays with string keys containing SQL syntax like comments (' ) -- '), it generates invalid SQL, allowing injection. This is crucial for pre-auth exploits on unpatched sites using PDO. Prerequisites include access to Drupal source code or a local installation for testing.

## Requirements

1. Access to Drupal 7 source code (e.g., via Git or downloaded package)
2. PHP environment to run and debug Drupal queries
3. Knowledge of SQL and PHP prepared statements

## Defense

Defensive measures and detection strategies:

- Patch to Drupal 7.32 or later, which fixes expandArguments handling
- Input validation on array parameters in custom modules
- Database query logging to detect malformed placeholders
- WAF rules blocking suspicious array inputs in forms

## Objectives

1. Identify vulnerable db_query patterns using IN clauses
2. Understand key-based array expansion flaws
3. Prepare for payload crafting based on analysis

## Instructions

### Step 1: Review Source Code

**Context**: Locate and examine the expandArguments function to understand array iteration logic.

Open includes/database/database.inc and search for expandArguments. Note how it loops over array keys assuming integers:

```php
function expandArguments(&$query, &$args) {
  // ...
  foreach ($args as $key => $value) {
    if (is_array($value)) {
      // Handles IN clauses but fails on string keys with SQL
    }
  }
}
```

> This reveals the assumption of numeric keys; test with strings to confirm malformation.

### Step 2: Test Locally

**Context**: Set up a local Drupal instance and debug a sample query.

Create a test module or use an existing form (e.g., search) that uses db_query with IN. Pass an associative array via debugger (e.g., Xdebug) and observe the generated SQL.

Example test query:

```php
$test_array = array('key1' => 'value1');
db_query('SELECT * FROM {test} WHERE id IN (:ids)', array(':ids' => $test_array));
```

> Expected: Malformed SQL if key contains ') -- ', confirming injection vector.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- reconnaissance
- drupal
- sql-injection
