---
id: 8a2a0dae-8bb1-4eca-8fb8-206c556e686c
name: docem.py - per_document xss
type: command
executor: bash
data: ./docem.py -s samples/xxe/sample_oxml_xxe_mod0/ -pm xss -pf payloads/xss_all.txt
  -pt per_document -kt -sx docx
output: null
created_at: '2023-04-06T03:56:43.974119+00:00'
updated_at: '2023-04-10T20:24:45.357412+00:00'
---

# docem.py - per_document xss

```bash
./docem.py -s samples/xxe/sample_oxml_xxe_mod0/ -pm xss -pf payloads/xss_all.txt -pt per_document -kt -sx docx
```


