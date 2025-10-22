---
id: 084daad2-801a-4ba4-8a5f-d44fcac9d317
name: docem.py - per_file xss
type: command
executor: bash
data: ./docem.py -s samples/xxe/sample_oxml_xxe_mod0/ -pm xss -pf payloads/xss_all.txt
  -pt per_file -kt -sx docx
output: null
created_at: '2023-04-06T03:56:43.974322+00:00'
updated_at: '2023-04-10T20:24:45.357412+00:00'
---

# docem.py - per_file xss

```bash
./docem.py -s samples/xxe/sample_oxml_xxe_mod0/ -pm xss -pf payloads/xss_all.txt -pt per_file -kt -sx docx
```
