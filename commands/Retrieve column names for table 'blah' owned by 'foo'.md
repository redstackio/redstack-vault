---
id: f169ab5d-84c4-4a00-a745-4a6463c0cbbf
name: Retrieve column names for table 'blah' owned by 'foo'
type: command
executor: bash
data: SELECT column_name FROM all_tab_columns WHERE table_name = 'blah' and owner
  = 'foo';
output: null
created_at: '2023-04-06T03:56:35.199899+00:00'
updated_at: '2023-04-10T20:23:10.722085+00:00'
---

# Retrieve column names for table 'blah' owned by 'foo'

```bash
SELECT column_name FROM all_tab_columns WHERE table_name = 'blah' and owner = 'foo';
```


