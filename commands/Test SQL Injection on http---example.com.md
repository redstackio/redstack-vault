---
id: e28bd604-c966-4623-ac53-024a674ee45d
name: Test SQL Injection on http://example.com
type: command
executor: bash
data: python sqlmap.py -u "http://example.com/?id=1"  -p id --suffix="-- "
output: null
created_at: '2023-04-06T03:56:36.476163+00:00'
updated_at: '2023-04-10T20:24:19.580819+00:00'
---

# Test SQL Injection on http://example.com

```bash
python sqlmap.py -u "http://example.com/?id=1"  -p id --suffix="-- "
```


