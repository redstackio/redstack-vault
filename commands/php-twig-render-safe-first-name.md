---
type: command
executor: php
data: |-
  $output = $twig->render(
    "Dear {first_name}",
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
  - safe
verified: true
validated: true
---

# php-twig-render-safe-first-name

## Command

```php
$output = $twig->render(
  "Dear {first_name}",
  array("first_name" => $user.first_name)
);
```

## Description

This PHP command safely renders a Twig template using a placeholder {first_name} and passes the user's first name via a context array, avoiding direct concatenation of user input. This prevents SSTI by ensuring inputs are treated as variables, not executable code.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $user.first_name | User's first name from application context | Yes |
| $twig | Initialized Twig environment instance | Yes |

## Examples

### Basic Usage

```php
$output = $twig->render(
  "Dear {first_name}",
  array("first_name" => $user.first_name)
);
echo $output;
```

### Advanced Usage

With safe context:

```php
$user.first_name = 'John'; // Sanitized input
$output = $twig->render(
  "Dear {first_name}!",
  array("first_name" => $user.first_name)
);
// Outputs: Dear John!
```

## Expected Output

The rendered template with substituted variables, e.g., "Dear John".

## Related

- [[procedures/Exploit-SSTI-in-Twig-Templates-for-RCE]]
- [[commands/php-twig-render-vulnerable-greeting]]
