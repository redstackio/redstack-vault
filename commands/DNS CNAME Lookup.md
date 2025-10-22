---
id: 76825614-f47b-4d6a-90f0-cefe3a5c739e
name: DNS CNAME Lookup
type: command
executor: bash
data: '$ dig cname.example.com +noall +answer

  ; <<>> DiG 9.11.3-1ubuntu1.15-Ubuntu <<>> example.com +noall +answer

  ;; global options: +cmd

  cname.example.com.            381     IN      CNAME   target.local.'
output: null
created_at: '2023-04-06T03:55:57.625471+00:00'
updated_at: '2023-04-10T20:22:11.443582+00:00'
---

# DNS CNAME Lookup

```bash
$ dig cname.example.com +noall +answer
; <<>> DiG 9.11.3-1ubuntu1.15-Ubuntu <<>> example.com +noall +answer
;; global options: +cmd
cname.example.com.            381     IN      CNAME   target.local.
```
