---
id: cmd-echo-htaccess
data: 'echo -e "RewriteEngine On\nRewriteRule ^(.*)$ /nonexistent [L]" > .htaccess'
tags:
  - file-creation
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:06.546Z'
verified: false
validated: true
submitted: true
---
# echo-create-file

## Command

```bash
echo -e "RewriteEngine On\nRewriteRule ^(.*)$ /nonexistent [L]" > .htaccess
```

## Description

This command creates a .htaccess file with Apache rewrite directives designed to cause processing errors when accessed.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-e` | Enables interpretation of backslash escapes | Yes |
| `> .htaccess` | Redirects output to file | Yes |

## Examples

### Basic Usage

```bash
echo -e "RewriteEngine On\nRewriteRule ^ /bad [L]" > .htaccess
```

### Advanced Usage

```bash
echo -e "<RequireAll>\nRequire all denied\n</RequireAll>" > .htaccess
```

## Expected Output

No output; file .htaccess is created with the specified content.

## Related

- [[Related Procedure|procedures/Upload-htaccess-File-to-Nextcloud]]
