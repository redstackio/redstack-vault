---
id: b45bab75-dc38-4313-b2b1-e04b7f9dd1e6
name: aws list ssh public keys for user
type: command
executor: bash
data: 'aws iam list-ssh-public-keys --user-name $AWS_IAM_USER

  '
output: null
created_at: '2020-07-31T04:25:28.973336+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# aws list ssh public keys for user

```bash
aws iam list-ssh-public-keys --user-name $AWS_IAM_USER

```
