---
id: 9315418d-fb3f-45b8-a5c9-7cb7fb1ee5f7
name: Look at environment variables set for secrets and analyze code
type: command
executor: bash
data: 'aws lambda get-function --function-name <lambda function>

  '
output: null
created_at: '2020-07-14T19:06:15.100394+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Look at environment variables set for secrets and analyze code

```bash
aws lambda get-function --function-name <lambda function>

```
