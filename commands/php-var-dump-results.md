---
data: var_dump($array_result);
tags:
  - output
  - debug
  - enumeration
type: command
output: >-
  array(1) { [user_id]=> array(1) { [0]=> array(2) { [0]=> string(11)
  "NON_AUTHORISED" [1]=> int(12345) } } }
executor: php
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:34.339Z'
id: ac918f85-1376-4901-85e5-ffac3683521e
verified: false
validated: true
submitted: true
---
# php-var-dump-results

## Command

```php
var_dump($array_result);
```

## Description

This PHP command dumps the contents of the $array_result variable, which holds enumerated data from bruteforcing, such as user_ids mapped to arrays of [status, calendar_id] pairs, for inspection and analysis.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $array_result | Associative array keyed by user_id with sub-arrays of results | Yes |

## Examples

### Basic Usage

```php
$array_result = [12345 => [['NON_AUTHORISED', 12346]]]; var_dump($array_result);
```

### Advanced Usage

Used at the end of a script after population:

```php
// After loop
if (!empty($array_result)) { var_dump($array_result); }
```

## Expected Output

A structured dump showing the array hierarchy, e.g., array(1) { [12345]=> array(1) { [0]=> array(2) { [0]=> string(11) "NON_AUTHORISED" [1]=> int(12345) } } }, revealing enumerated users and calendars.

## Related

- [[Related Procedure: Bruteforce-Calendar-IDs-to-Enumerate-Users-and-Integrations]]
