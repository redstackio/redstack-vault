---
id: 5882c137-07ff-4593-9dbc-a5ae2b95cfc3
name: Get Cookie Value
type: command
executor: bash
data: window.cookieStore.get('COOKIE NAME').then((cookieValue)=>{alert(cookieValue.value);});
output: null
created_at: '2023-04-06T03:56:42.691581+00:00'
updated_at: '2023-04-10T20:21:40.922757+00:00'
---

# Get Cookie Value

```bash
window.cookieStore.get('COOKIE NAME').then((cookieValue)=>{alert(cookieValue.value);});
```
