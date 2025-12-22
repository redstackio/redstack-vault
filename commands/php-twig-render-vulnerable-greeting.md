---
type: command
executor: php
data: |-
  $output = $twig->render(
    'Dear' . $_GET['custom_greeting'],
    array("first_name" => $user.first_name)
  );
output: null
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - php
  - web
tags:
  - ssti
  - twig
  - vulnerable
verified: true
validated: true
---

# php-twig-render-vulnerable-greeting

## Command

```php
$output = $twig->render(
  'Dear' . $_GET['custom_greeting'],
  array("first_name" => $user.first_name)
);
```

## Description

This PHP command renders a Twig template by concatenating unsanitized user input from $_GET['custom_greeting'] into the template string, making it vulnerable to SSTI. It passes an array with the user's first name as context. Use this to simulate or analyze vulnerable rendering in a test environment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_GET['custom_greeting'] | User-supplied greeting string injected into template | Yes |
| $user.first_name | User's first name from application context | Yes |
| $twig | Initialized Twig environment instance | Yes |

## Examples

### Basic Usage

```php
$output = $twig->render(
  'Dear' . $_GET['custom_greeting'],
  array("first_name" => $user.first_name)
);
echo $output;
```

### Advanced Usage

Inject a test payload:

```php
// With SSTI test
$_GET['custom_greeting'] = '{{7*7}}';
$output = $twig->render(
  'Dear' . $_GET['custom_greeting'],
  array("first_name" => 'John')
);
// Outputs: Dear 49 John
```

## Expected Output

The rendered template string, e.g., "Dear Custom Greeting, John" if no injection, or evaluated expression if SSTI is exploited (e.g., "Dear 49, John" for {{7*7}}).

## Related

- [[procedures/Exploit-SSTI-in-Twig-Templates-for-RCE]]
- [[commands/php-twig-render-safe-first-name]]
