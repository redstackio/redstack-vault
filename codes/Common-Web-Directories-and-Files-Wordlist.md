---
id: 3de152c2-962e-4461-8ed1-4516dcd7ee41
name: Common-Web-Directories-and-Files-Wordlist
type: code
language: text
verified: true
created_at: '2020-07-24T17:11:30.216278+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Web
tags:
  - wordlist
  - fuzzing
  - reconnaissance
validated: true
---

# Common-Web-Directories-and-Files-Wordlist

## Code

```text
/phpinfo.php
/info.php
/admin.php
/api/apidocs
/apidocs
/api
/api/v2
/api/v1
/v2
/package.json
/security.txt
/application.wadl
/api/apidocs
/swagger
/swagger-ui
/swagger-ui.html
/swagger/swagger-ui.html
/api/swagger-ui.html
/v1.x/swagger-ui.html
/swagger/index.html
/graphql
/graphiql
```

## Description

This is a static wordlist of common web directories, files, and endpoints frequently found in modern applications, particularly those exposing API documentation, admin interfaces, and configuration files. It is designed for use with fuzzing tools like Dirsearch to probe subdomains for hidden resources during reconnaissance. The list focuses on high-value targets like Swagger UI for APIs and security.txt for disclosure policies, helping prioritize discoveries that could lead to information leaks or further exploitation.

## Parameters

No variables; this is a static list. Save as a .txt file (e.g., paths.txt) for direct use in tools.

| Variable | Description | Example |
|----------|-------------|---------|
| N/A | Plain text file with one path per line | paths.txt |

## Usage

Load this wordlist into Dirsearch or similar tools for web brute-forcing: e.g., `-w paths.txt`. It is typically used after subdomain enumeration to map web structures. In the procedure [[procedures/Brute-Force-Directories-and-Files-on-Subdomains-Using-Dirsearch]], save this content to paths.txt before scanning.

## Detection

Wordlists like this are not executed directly, but their use can be detected via web server logs showing patterns of requests to these exact paths (e.g., bursts of /swagger-ui.html probes). WAFs may flag the sequence as scanning behavior.

## Related

- [[procedures/Brute-Force-Directories-and-Files-on-Subdomains-Using-Dirsearch]]
- [[tools/Dirsearch]]
