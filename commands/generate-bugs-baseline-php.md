---
id: cmd-uuid-003
data: >-
  <?php for ($i=0;$i<30;$i++){ echo '<img id=grr"'.$i.'"
  src="https://hackerone.com/bugs.json?text_query=999999&subject=&sort_type=pg_search_rank&substates%5B%5D=triaged&rnd='.rand(1,5000).'">';
  } ?>
tags:
  - baseline-generation
type: command
output: HTML output with 30 <img> elements triggering requests
executor: php
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:50.082Z'
verified: false
validated: true
submitted: true
---
# generate-bugs-baseline-php

## Command

```php
<?php for ($i=0;$i<30;$i++){ echo '<img id=grr"'.$i.'" src="https://hackerone.com/bugs.json?text_query=999999&subject=&sort_type=pg_search_rank&substates%5B%5D=triaged&rnd='.rand(1,5000).'">'; } ?>
```

## Description

Generates 30 <img> tags for empty bugs endpoint (~750 bytes) to measure low-end baseline timings.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $i | Loop counter | Yes |
| src URL | Empty query endpoint | Yes |
| rnd | Random anti-cache | Yes |

## Examples

### Basic Usage

Serve as 2.php.

## Expected Output

30 <img> tags in HTML.

## Related

- [[Related Procedure: Measure-Baseline-Load-Times]]
