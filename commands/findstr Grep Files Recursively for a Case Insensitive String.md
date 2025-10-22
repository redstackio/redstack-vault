---
id: d67c1db3-908c-4e94-b40f-c4a5eb0cd1fa
name: findstr Grep Files Recursively for a Case Insensitive String
type: command
executor: command_prompt
data: findstr /si $_STRING *.*
output: 'C:\Users>findstr /s "OPENSSH" *.*

  Bob\mykey:-----BEGIN OPENSSH PRIVATE KEY-----

  Bobo\mykey:-----END OPENSSH PRIVATE KEY-----'
created_at: '2019-11-26T16:37:00.745610+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# findstr Grep Files Recursively for a Case Insensitive String

```command_prompt
findstr /si $_STRING *.*
```

## Expected Output

```
C:\Users>findstr /s "OPENSSH" *.*
Bob\mykey:-----BEGIN OPENSSH PRIVATE KEY-----
Bobo\mykey:-----END OPENSSH PRIVATE KEY-----
```
