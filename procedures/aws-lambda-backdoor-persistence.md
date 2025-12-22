---
type: procedure
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
techniques:
  - >-
    [[techniques/Application Access Token|T1528 - Steal Application Access
    Token]]
  - '[[techniques/Phishing|T1566 - Phishing]]'
sub_techniques: []
tags:
  - aws
  - cloud
  - persistence
  - lambda
  - backdoor
commands:
  - '[[commands/update-aws-lambda-function-code]]'
tools:
  - '[[tools/aws-cli]]'
platforms:
  - AWS
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# aws-lambda-backdoor-persistence

## Summary

This procedure demonstrates how to achieve persistence in an AWS environment by uploading malicious code to an existing Lambda function using stolen or compromised AWS credentials. The backdoor code can execute arbitrary commands, exfiltrate data, or maintain a foothold, allowing attackers to evade detection and regain access even after initial compromises are remediated.

## Description

AWS Lambda enables serverless execution of code in response to events, making it an attractive vector for persistence without managing infrastructure. Once an attacker obtains valid AWS credentials (e.g., via phishing or token theft), they can modify an existing Lambda function's code to include a backdoor. This backdoor might trigger on common events like API Gateway requests or S3 uploads, performing actions such as data exfiltration to an attacker-controlled server or executing system commands. The technique leverages the trust in Lambda functions, which often run with elevated permissions, and is hard to detect without code reviews. It applies to environments where Lambda functions are deployed for automation, APIs, or event-driven workflows, assuming the attacker knows or enumerates function names.

## Requirements

1. Valid AWS credentials with permissions to update Lambda functions (e.g., lambda:UpdateFunctionCode policy).
2. AWS CLI installed and configured with the compromised credentials.
3. Access to an existing Lambda function name (discoverable via AWS console or CLI enumeration).
4. A ZIP file containing the backdoor code, prepared for Lambda deployment (Python runtime assumed).
5. Network access to upload the ZIP file (local file path).

## Defense

- Monitor AWS CloudTrail logs for unauthorized lambda:UpdateFunctionCode API calls and alert on changes from unknown IPs or unusual user agents.
- Implement least-privilege IAM policies, restricting Lambda code updates to approved roles and requiring MFA for sensitive actions.
- Regularly audit Lambda function code using tools like AWS Config or third-party scanners for malicious payloads, and enable code signing for functions.
- Use AWS Organizations SCPs to deny Lambda updates in production environments without approval workflows.

## Objectives

1. Establish long-term persistence in the AWS account by modifying a Lambda function to include backdoor logic.
2. Evade detection by blending malicious code with legitimate function behavior, maintaining access post-compromise.
3. Enable further actions like data exfiltration or lateral movement upon function invocation.

## Instructions

### Step 1: Prepare the Backdoor Code

**Context**: Create a malicious Lambda handler that exfiltrates event data to an attacker-controlled endpoint upon invocation. This step ensures the code is ready for packaging and explains why a simple HTTP request is used—to avoid dependencies and trigger on any event.

Save the backdoor code as `lambda_function.py` using the [[codes/lambda-python-backdoor-exfil]] snippet, substituting parameters as needed.

**Expected Output**: A Python file ready for zipping.

### Step 2: Package the Backdoor into a ZIP File

**Context**: Lambda requires code to be uploaded as a ZIP archive. This step packages the malicious handler, ensuring it's deployable without altering the function's configuration.

Create a directory `backdoor_lambda`, place `lambda_function.py` inside, and zip it:

```bash
mkdir backdoor_lambda
# Place lambda_function.py here
zip -r deployment.zip backdoor_lambda/
```

**Expected Output**: A `deployment.zip` file containing the backdoor code.

**Success Indicators**:
- ZIP file created without errors.
- Unzipping shows the Python handler intact.

### Step 3: Update the Lambda Function Code

**Context**: Use AWS CLI to replace the existing function code with the backdoor ZIP. This overwrites the original handler, achieving persistence; the function will execute the backdoor on next invocation.

**Command** ([[commands/update-aws-lambda-function-code]]):

```bash
aws lambda update-function-code --function-name $_FUNCTION_NAME --zip-file fileb://$_ZIP_FILE
```

> This command uploads the ZIP and updates the function. The `fileb://` prefix is required for local file uploads. Replace placeholders with actual values (e.g., function name from enumeration, ZIP path).

**Expected Output**: JSON response confirming the update, including FunctionName, LastModified, and CodeSize.

**Success Indicators**:
- No permission errors; response shows "FunctionArn" and updated CodeSha256.
- Verify via AWS console or `aws lambda get-function --function-name $_FUNCTION_NAME` showing new LastModified timestamp.
