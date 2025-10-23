---
id: 8bc11dee-50c9-4bb8-bebf-e29de3cf4fde
name: AWS metadata and credentials
type: command
executor: bash
data: 'Always here : /latest/meta-data/{hostname,public-ipv4,...}

  User data (startup script for auto-scaling) : /latest/user-data

  Temporary AWS credentials : /latest/meta-data/iam/security-credentials/'
output: null
created_at: '2023-04-06T03:56:38.153810+00:00'
updated_at: '2023-04-10T20:23:59.980820+00:00'
---

# AWS metadata and credentials

```bash
Always here : /latest/meta-data/{hostname,public-ipv4,...}
User data (startup script for auto-scaling) : /latest/user-data
Temporary AWS credentials : /latest/meta-data/iam/security-credentials/
```


