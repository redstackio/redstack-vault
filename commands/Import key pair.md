---
id: d057d498-02a8-4caf-94b9-5cae38758c7a
name: Import key pair
type: command
executor: bash
data: $ aws ec2 import-key-pair --key-name "AWS Audit" --public-key-material file://~/.ssh/id_rsa.pub
  --region eu-west-1
output: null
created_at: '2023-04-06T03:56:09.572488+00:00'
updated_at: '2023-04-10T20:19:44.887186+00:00'
---

# Import key pair

```bash
$ aws ec2 import-key-pair --key-name "AWS Audit" --public-key-material file://~/.ssh/id_rsa.pub --region eu-west-1
```


