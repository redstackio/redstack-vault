---
id: 9cab5425-dc81-4b46-8ea3-8fd496b73d86
name: Upload image from URL
type: command
executor: bash
data: 'document.querySelector(''input[type=url]'').value = ''https://example.com/image.jpg'';

  document.querySelector(''input[type=url]'').dispatchEvent(new Event(''change''));'
output: null
created_at: '2023-04-06T03:56:37.687052+00:00'
updated_at: '2023-04-10T20:24:06.140012+00:00'
---

# Upload image from URL

```bash
document.querySelector('input[type=url]').value = 'https://example.com/image.jpg';
document.querySelector('input[type=url]').dispatchEvent(new Event('change'));
```


