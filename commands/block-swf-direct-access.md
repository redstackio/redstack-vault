---
id: cmd-uuid-2
data: |-
  <FilesMatch "\.(swf)$">
  Header set Content-Disposition attachment
  </FilesMatch>
tags:
  - mitigation
  - apache
  - htaccess
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:55.615Z'
verified: false
validated: true
submitted: true
---
# block-swf-direct-access

## Command

```bash
<FilesMatch "\.(swf)$">
Header set Content-Disposition attachment
</FilesMatch>
```

## Description

Apache .htaccess directive to force SWF files to download as attachments rather than execute in the browser, mitigating direct access exploits like Flash XSS. Add to .htaccess in WordPress directories.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| FilesMatch | Regex for .swf files | Yes |
| Header set | Sets Content-Disposition to attachment | Yes |

## Examples

### Basic Usage

Add to .htaccess:

```bash
<FilesMatch "\.(swf)$">
Header set Content-Disposition attachment
</FilesMatch>
```

### Advanced Usage

Combine with deny:

```bash
<FilesMatch "\.(swf)$">
Order allow,deny
Deny from all
Header set Content-Disposition attachment
</FilesMatch>
```

## Expected Output

Browser prompts download of SWF instead of embedding/running it, preventing execution.

## Related

- [[commands/curl-flash-xss-poc]]
- [[procedures/Execute-Flash-XSS-PoC-in-WordPress]]
