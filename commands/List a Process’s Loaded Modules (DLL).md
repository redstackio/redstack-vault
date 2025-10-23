---
id: c916f1b3-582a-49e6-b962-d957e0921c56
name: List a Process’s Loaded Modules (DLL)
type: command
executor: bash
data: 'get-process -id 1234|select -expand modules

  '
output: null
created_at: '2020-07-14T18:21:10.825093+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# List a Process’s Loaded Modules (DLL)

```bash
get-process -id 1234|select -expand modules

```


