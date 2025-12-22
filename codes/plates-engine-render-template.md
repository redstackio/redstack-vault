---
id: 46fbf6fd-8092-45ed-82c1-b1a6c723b2cc
name: plates-engine-render-template
type: code
language: PHP
verified: true
created_at: '2023-04-06T03:56:40.469049+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - PHP
tags:
  - ssti
  - plates
  - render
  - template
validated: true
---

# plates-engine-render-template

## Code

```php
// Create new Plates instance
$templates = new League\Plates\Engine('/path/to/templates');

// Render a template
echo $templates->render('profile', ['name' => 'Jonathan']);
```

## Description

This code snippet initializes the Plates templating engine and renders a template named 'profile' with a 'name' variable. In a vulnerable context, if the 'name' value is derived from untrusted user input without escaping in the template (e.g., <?=$name?>), it enables SSTI for RCE. Used in PHP web applications to dynamically generate content.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `/path/to/templates` | Path to the directory holding template files | `/var/www/templates` |
| `profile` | Template filename (sans extension) | `profile` |
| `['name' => 'Jonathan']` | Associative array of variables; 'name' key is injectable if user-controlled | `['name' => '<?php system("id"); ?>']` |

## Usage

Embed in a PHP script or web endpoint to render dynamic pages. For exploitation, replace the 'name' value with a PHP payload and submit via HTTP parameters. Requires the League\Plates library installed via Composer. Test in a lab by creating a simple vulnerable app.

## Detection

- Static analysis: Search for League\Plates\Engine and unchecked render calls with user input.
- Dynamic: Monitor for anomalous PHP execution in web logs (e.g., system() calls) or WAF alerts on PHP tags in inputs.
- Runtime: Enable PHP error logging to catch parse errors from injected code.

## Related

- [[procedures/Exploit-SSTI-in-Plates-PHP-Templating-Engine]]
- [[commands/php-render-plates-template]]
