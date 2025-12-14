---
tags:
  - sqli
  - payload
  - drupal
type: procedure
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:30.673Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 7794976f-b96b-43cc-8b54-66099348055b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft Malicious Array for SQL Injection

## Summary

This procedure crafts a malicious array with non-integer keys to exploit the SQL injection in Drupal 7's expandArguments, allowing injection via prepared statement placeholders in IN clauses.

## Description

By using string keys containing SQL syntax like comments or operators, the array disrupts placeholder generation, resulting in injectable SQL. For example, an array passed to db_query's IN clause can comment out the rest of the query, enabling payload execution pre-authentication through vulnerable Drupal endpoints like search forms.

## Requirements

1. Vulnerable Drupal 7 site accessible via HTTP
2. Knowledge of a db_query IN usage (e.g., user filter)
3. Tool like curl or Burp Suite for request crafting

## Defense

Defensive measures and detection strategies:

- Sanitize array keys to integers only
- Use strict prepared statements without dynamic placeholders
- Log and monitor anomalous query patterns

## Objectives

1. Generate a payload that alters SQL structure
2. Test injection without full exploitation
3. Prepare for chained database operations

## Instructions

### Step 1: Design Array Structure

**Context**: Build the array to include a non-integer key with SQL injection elements.

Define $args = array(':name' => array('test) -- ' => 'user1', 'test' => 'user2')); This creates placeholders like :name_test)-- leading to 'IN (:name_test)-- , :name_test )'.

> Expected: SQL comment (--) bypasses closing parenthesis and additional placeholders.

### Step 2: Integrate into Request

**Context**: Embed the array in a HTTP request to trigger db_query.

Use curl to POST the serialized or form-encoded array to a vulnerable endpoint, e.g., curl -X POST -d 'names[0]=val&names[:inj)--]=payload' http://target/search.

> Expected: Server error or unexpected results indicating successful injection point.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[sqli]]
- [[drupal]]
- [[payload-crafting]]
