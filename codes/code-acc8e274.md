---
id: acc8e274-6bb5-490c-913a-bfb302a72049
type: code
language: Python
verified: false
created_at: '2023-04-06T03:56:40.894446+00:00'
updated_at: '2023-04-06T03:56:40.905257+00:00'
---

# Code Snippet acc8e274

**Language**: Python

```python
# create valid .htaccess/xbm image

width = 50
height = 50
payload = '# .htaccess file'

with open('.htaccess', 'w') as htaccess:
    htaccess.write('#define test_width %d\n' % (width, ))
    htaccess.write('#define test_height %d\n' % (height, ))
    htaccess.write(payload)
```
