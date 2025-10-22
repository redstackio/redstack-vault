---
id: 9df71556-f8d4-45ae-b6d2-928a6908253f
name: Send SSH public key
type: command
executor: bash
data: $ aws ec2-instance-connect send-ssh-public-key --region us-east-1 --instance-id
  INSTANCE --availability-zone us-east-1d --instance-os-user ubuntu --ssh-public-key
  file://shortkey.pub --profile uploadcreds
output: null
created_at: '2023-04-06T03:56:09.629928+00:00'
updated_at: '2023-04-10T20:19:45.231882+00:00'
---

# Send SSH public key

```bash
$ aws ec2-instance-connect send-ssh-public-key --region us-east-1 --instance-id INSTANCE --availability-zone us-east-1d --instance-os-user ubuntu --ssh-public-key file://shortkey.pub --profile uploadcreds
```
