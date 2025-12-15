---
id: cmd-uuid-002
data: >-
  <?php for ($i=0;$i<30;$i++){ echo '<img id=grr"'.$i.'"
  src="https://hackerone.com/programs/search.json?query=IBB&sort=published_at%3Adescending&page=1&rnd='.rand(1,5000).'"></img>';
  } ?>
tags:
  - baseline-generation
type: command
output: HTML output with 30 <img> elements triggering requests
executor: php
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:50.087Z'
verified: false
validated: true
submitted: true
---
# generate-programs-baseline-php

## Command

```php
<?php for ($i=0;$i<30;$i++){ echo '<img id=grr"'.$i.'" src="https://hackerone.com/programs/search.json?query=IBB&sort=published_at%3Adescending&page=1&rnd='.rand(1,5000).'"></img>'; } ?>
```

## Description

PHP loop generates 30 <img> tags to load a fixed HackerOne endpoint for baseline timing measurement, with random param to bust cache.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $i | Loop counter 0-29 | Yes |
| src URL | Fixed endpoint for ~9200 bytes | Yes |
| rand(1,5000) | Anti-caching randomizer | Yes |

## Examples

### Basic Usage

Embed in PHP file and serve.

### Advanced Usage

Increase loop to 50 for more samples.

## Expected Output

HTML: <img id=grr"0" src="https://...rnd=1234"></img> ... (30 times).

## Related

- [[Related Procedure: Measure-Baseline-Load-Times]]
