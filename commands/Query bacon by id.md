---
id: 7ebc1c64-43ab-4176-9daa-dfa3d6016f18
name: Query bacon by id
type: command
executor: bash
data: "{ \n    bacon(id: \"1'\") { \n        id, \n        type, \n        price\n\
  \    }\n}"
output: null
created_at: '2023-04-06T03:55:58.955674+00:00'
updated_at: '2023-04-10T20:22:21.494112+00:00'
---

# Query bacon by id

```bash
{ 
    bacon(id: "1'") { 
        id, 
        type, 
        price
    }
}
```


