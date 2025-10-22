---
id: 464d14ea-991d-4394-b52e-0d67c1b7e183
name: List Command Invocations
type: command
executor: bash
data: $ aws ssm list-command-invocations --command-id "COMMAND-ID-HERE" --details
  --query "CommandInvocations[].CommandPlugins[].{Status:Status,Output:Output}" --profile
  stolencreds
output: null
created_at: '2023-04-06T03:56:09.691524+00:00'
updated_at: '2023-04-10T20:20:49.939502+00:00'
---

# List Command Invocations

```bash
$ aws ssm list-command-invocations --command-id "COMMAND-ID-HERE" --details --query "CommandInvocations[].CommandPlugins[].{Status:Status,Output:Output}" --profile stolencreds
```
