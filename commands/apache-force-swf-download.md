---
id: cmd-swf-header
data: |-
  FilesMatch "\.(swf)$"
  Header set Content-Disposition attachment
  </FilesMatch>
tags:
  - mitigation
  - apache
  - flash
type: command
output: 'SWF files are downloaded rather than loaded/executed, mitigating direct access'
executor: apache
platforms:
  - Web
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:23:53.883Z'
verified: false
validated: true
submitted: true
---
# apache-force-swf-download

## Command

```apache
<FilesMatch "\.(swf)$">
Header set Content-Disposition attachment
</FilesMatch>
```

## Description

This Apache .htaccess configuration forces browsers to download SWF files as attachments instead of executing them, preventing direct loading of vulnerable Flash content like plupload.flash.swf.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| FilesMatch "\.(swf)$" | Matches all .swf files in the directory | Yes |
| Header set Content-Disposition attachment | Sets the header to prompt download | Yes |

## Examples

### Basic Usage

```apache
<FilesMatch "\.(swf)$">
Header set Content-Disposition attachment
</FilesMatch>
```

Place this in .htaccess in the WordPress root or wp-includes.

### Advanced Usage

```apache
<FilesMatch "plupload\.flash\.swf$">
Header set Content-Disposition attachment
Header unset Content-Type
</FilesMatch>
```

Targets specific file and removes MIME type.

## Expected Output

When accessing /wp-includes/js/plupload/plupload.flash.swf, the browser prompts to download instead of embedding/running the Flash.

## Related

- [[procedures/Open-SWF-Window-with-Crafted-Payload]]
