---
id: c5ee48f4-755a-4eab-b08a-476389fa9ad9
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:09.491654+00:00'
updated_at: '2023-04-10T20:19:51.413422+00:00'
---

# Code Snippet c5ee48f4

**Language**: Powershell

```powershell
git clone git@github.com:andresriancho/enumerate-iam.git
pip install -r requirements.txt
./enumerate-iam.py --access-key AKIA... --secret-key StF0q...
2019-05-10 15:57:58,447 - 21345 - [INFO] Starting permission enumeration for access-key-id "AKIA..."
2019-05-10 15:58:01,532 - 21345 - [INFO] Run for the hills, get_account_authorization_details worked!
2019-05-10 15:58:01,537 - 21345 - [INFO] -- {
    "RoleDetailList": [
        {
            "Tags": [],
            "AssumeRolePolicyDocument": {
                "Version": "2008-10-17",
                "Statement": [
                    {
...
2019-05-10 15:58:26,709 - 21345 - [INFO] -- gamelift.list_builds() worked!
2019-05-10 15:58:26,850 - 21345 - [INFO] -- cloudformation.list_stack_sets() worked!
2019-05-10 15:58:26,982 - 21345 - [INFO] -- directconnect.describe_locations() worked!
2019-05-10 15:58:27,021 - 21345 - [INFO] -- gamelift.describe_matchmaking_rule_sets() worked!
2019-05-10 15:58:27,311 - 21345 - [INFO] -- sqs.list_queues() worked!
```
