---
id: 85a0e055-ff41-4101-a6cb-b9688e720f33
name: google-dorks-search-admin-login-urls
type: command
executor: browser
data: 'site:domain.com inurl:login,register,upload,logout,redirect,redir,goto,admin'
output: null
created_at: '2023-04-06T03:56:25.426036+00:00'
updated_at: '2023-04-10T20:25:37.761328+00:00'
platforms:
  - Web
tags:
  - reconnaissance
  - auth-discovery
verified: true
validated: true
---

# google-dorks-search-admin-login-urls

## Command

Enter this query directly into the Google search bar:

```text
site:domain.com inurl:login,register,upload,logout,redirect,redir,goto,admin
```

## Description

This Google Dork locates authentication and administrative URLs by searching for common paths like 'login' or 'admin', helping identify potential entry points for credential attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| domain.com | The target domain | Yes |
| inurl:login,register,... | Comma-separated paths to search | Yes |

## Examples

### Basic Usage

```text
site:example.com inurl:login,admin
```

Finds login and admin pages.

### Advanced Usage

Exclude false positives:

```text
site:example.com inurl:admin -inurl:blog
```

Avoids non-admin results.

## Expected Output

Results like:

- admin.example.com/login
- example.com/user/register

Test for weaknesses.

## Related

- [[procedures/Subdomain-Enumeration-with-Google-Dorks]]
- [[commands/google-dorks-search-urls-with-ampersand]]
