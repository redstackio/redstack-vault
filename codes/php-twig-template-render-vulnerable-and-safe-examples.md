---
type: code
language: php
verified: true
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - php
  - web
tags:
  - ssti
  - twig
  - example
  - vulnerable
validated: true
---

# php-twig-template-render-vulnerable-and-safe-examples

## Code

```php
$output = $twig->render(
  'Dear' . $_GET['custom_greeting'],
  array("first_name" => $user.first_name)
);

$output = $twig->render(
  "Dear {first_name}",
  array("first_name" => $user.first_name)
);
```

## Description

This code snippet provides examples of Twig template rendering in PHP: the first is vulnerable to SSTI due to unsanitized concatenation of $_GET['custom_greeting'], while the second uses safe placeholder substitution. It illustrates how improper handling leads to injection risks and how to mitigate them in web applications.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_GET['custom_greeting'] | Unsanitized user input for vulnerable render | '{{7*7}}' |
| $user.first_name | Application context variable for name | 'John' |
| $twig | Twig_Loader and Environment instance | $loader = new Twig_Loader_Filesystem('/path'); $twig = new Twig_Environment($loader); |

## Usage

Embed this in a PHP script to demonstrate SSTI during training or auditing. For exploitation, modify $_GET['custom_greeting'] with payloads in a proxy like Burp Suite. Use the safe example as a reference for secure coding practices in red team reports or developer training.

## Detection

- Review PHP source for concatenation into Twig render strings (e.g., grep for 'render.*\.' ).
- Monitor access logs for suspicious parameters containing '{{' or Twig syntax.
- Enable PHP error logging to catch template evaluation exceptions.
- Use static analysis tools like PHPStan to flag unsanitized inputs in templates.

## Related

- [[procedures/Exploit-SSTI-in-Twig-Templates-for-RCE]]
- [[tools/Burp-Suite]]
