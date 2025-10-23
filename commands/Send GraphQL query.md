---
id: 960b2007-b84b-4d1f-a859-87329cf26214
name: Send GraphQL query
type: command
executor: bash
data: "{\n  \"query\": \"query {\n    teams{\n      total_count,edges{\n        node{\n\
  \          id,_id,about,handle,state\n        }\n      }\n    }\n  }\"\n}"
output: null
created_at: '2023-04-06T03:55:58.816432+00:00'
updated_at: '2023-04-10T20:22:23.645696+00:00'
---

# Send GraphQL query

```bash
{
  "query": "query {
    teams{
      total_count,edges{
        node{
          id,_id,about,handle,state
        }
      }
    }
  }"
}
```


