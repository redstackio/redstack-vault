---
id: craft-sqli-payload-001
tags:
  - sql-injection
  - payload-crafting
  - drupal
type: procedure
tools: []
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
updated_at: '2025-12-14T03:46:20.032Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft SQL Injection Payload Using Associative Arrays

## Summary

This procedure crafts a SQL injection payload exploiting Drupal 7's expandArguments flaw by using associative arrays with malicious string keys to inject arbitrary SQL into prepared statements via IN clauses.

## Description

Target pre-auth endpoints in Drupal 7 that use db_query with IN parameters, such as user search or node queries. The payload leverages PDO's multi-query support by closing the IN clause early with a comment in the array key, allowing appended SQL. This enables attackers to execute without authentication on vulnerable sites.

## Requirements

1. Identified vulnerable endpoint from analysis
2. Ability to send crafted HTTP requests (e.g., via browser dev tools or scripts)
3. Target running Drupal 7 < 7.32

## Defense

Defensive measures and detection strategies:

- Sanitize array inputs to ensure numeric keys only
- Use strict prepared statements without dynamic placeholders
- Monitor for unusual array structures in request parameters
- Enable Drupal's database error logging

## Objectives

1. Bypass prepared statement protections
2. Inject custom SQL into the query
3. Validate injection success without full exploit

## Instructions

### Step 1: Identify Vulnerable Parameter

**Context**: Find a form or API endpoint using IN clauses, e.g., user name search.

Inspect the form action and parameters, ensuring it passes arrays to db_query.

### Step 2: Build Associative Array Payload

**Context**: Create the malicious array with a key that includes SQL termination.

In a POST request:

```http
Content-Type: application/x-www-form-urlencoded

search_names[\"test) -- \"]=dummy&search_names[test]=user1
```

This translates to PHP array(':name' => array('test) -- ' => 'dummy', 'test' => 'user1')), generating: 'IN (:name_test) -- , :name_test )'.

> The comment '--' ignores trailing SQL, allowing injection before it.

### Step 3: Inject Basic Test

**Context**: Append a benign SQL like 'SELECT 1' to confirm execution.

Full payload: ') -- ; SELECT 1 -- ' in the key, sent via the endpoint.

> Success: No errors, and query returns expected results altered by injection.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- sql-injection
- payload-crafting
- drupal
