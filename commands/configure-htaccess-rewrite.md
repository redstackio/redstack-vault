---
data: |-
  RewriteEngine on
  RewriteCond %{REQUEST_URI} !^/hack.js$
  RewriteRule .* /hack.js [L,R=302]
tags:
  - redirection
  - server-config
type: command
output: All non-/hack.js requests redirect to /hack.js
executor: apache
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:56:19.803Z'
id: cbbd3e1c-20b3-406d-adc9-52f722837e90
verified: false
validated: true
submitted: true
---
# configure-htaccess-rewrite

## Command

```apache
RewriteEngine on
RewriteCond %{REQUEST_URI} !^/hack.js$
RewriteRule .* /hack.js [L,R=302]
```

## Description

Configures Apache .htaccess to redirect all requests except /hack.js to the payload file, ensuring consistent JS delivery for multiple redirected asset paths in the XSS attack.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| REQUEST_URI | Incoming path condition | Yes |
| hack.js | Payload file path | Yes |
| R=302 | Redirect type (temporary) | No |

## Examples

### Basic Usage

Place in .htaccess root.

### Advanced Usage

Add MIME: AddType application/javascript .js

## Expected Output

Requests to /any/path return 302 to /hack.js, serving JS.

## Related

- [[commands/host-alert-payload]]
- [[procedures/Set-Up-Attacker-Web-Server-for-Script-Hosting]]
