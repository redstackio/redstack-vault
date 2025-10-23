---
id: 2bc51d44-11a3-4617-96e5-a0da7fe97f3b
name: Request certificate using certi.py
type: command
executor: bash
data: certi.py req 'contoso.local/Anakin@dc01.contoso.local' contoso-DC01-CA -k -n
  --alt-name han --template UserSAN
output: null
created_at: '2023-04-06T03:56:05.732200+00:00'
updated_at: '2023-04-10T20:25:45.495574+00:00'
---

# Request certificate using certi.py

```bash
certi.py req 'contoso.local/Anakin@dc01.contoso.local' contoso-DC01-CA -k -n --alt-name han --template UserSAN
```


