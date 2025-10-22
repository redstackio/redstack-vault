---
id: b5c6e11c-bb56-4d61-a3d7-4b37b427cff9
type: code
language: ini
verified: false
created_at: '2023-04-06T03:56:40.941670+00:00'
updated_at: '2023-04-06T03:56:40.945323+00:00'
---

# Code Snippet b5c6e11c

**Language**: ini

```ini
[uwsgi]
; read from a symbol
foo = @(sym://uwsgi_funny_function)
; read from binary appended data
bar = @(data://[REDACTED])
; read from http
test = @(http://[REDACTED])
; read from a file descriptor
content = @(fd://[REDACTED])
; read from a process stdout
body = @(exec://whoami)
; call a function returning a char *
characters = @(call://uwsgi_func)
```
