---
id: aead8875-3fa1-435b-9562-a762a0e85012
name: Obfuscate-AWS-CloudTrail-and-GuardDuty-Logs
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:09.790674+00:00'
updated_at: '2023-04-10T20:19:56.104956+00:00'
tactics:
  - '[[tactics/Defense-Evasion|TA0005 - Defense Evasion]]'
techniques:
  - >-
    [[techniques/Impair-Defenses-Disable-or-Modify-Tools|T1562.001 - Disable or
    Modify Tools]]
  - '[[techniques/Indicator-Removal-on-Host|T1070 - Indicator Removal on Host]]'
sub_techniques: []
tags:
  - Cloud-AWS
  - Cover-Tracks-Obfuscate-CloudTrail-GuardDuty
commands: []
platforms:
  - AWS
  - Cloud
tools:
  - '[[tools/AWS-CLI]]'
  - '[[tools/Boto3]]'
validated: true
---

# Obfuscate-AWS-CloudTrail-and-GuardDuty-Logs

## Summary

This procedure demonstrates how to modify the user-agent string in AWS CLI requests using the Boto3 library to evade detection by AWS GuardDuty. By altering the user-agent to remove indicators of offensive Linux distributions like Kali, Parrot, or Pentoo, attackers can obfuscate their API calls in CloudTrail logs, making it harder for security teams to identify suspicious activity originating from security testing environments.

## Description

AWS CloudTrail logs all API activity, and GuardDuty analyzes these logs for threats, including API calls from known security tools or distributions like Kali Linux. The default user-agent in Boto3 sessions includes OS details that can trigger GuardDuty findings. This procedure involves integrating a Python snippet into scripts that use Boto3 to dynamically detect and modify the user-agent before making API calls. This technique falls under defense evasion by impairing logging mechanisms without disabling them outright. It is particularly useful in post-compromise scenarios where persistent access to AWS resources is needed without alerting monitoring services. The target environment is any AWS account with CloudTrail and GuardDuty enabled, assuming the attacker has valid credentials.

## Requirements

1. Valid AWS credentials (access key and secret key) with permissions to make API calls.
2. AWS CLI installed on the attacker's machine (version 2.x recommended).
3. Python 3.x with the Boto3 library installed (pip install boto3).
4. Running on a Linux distribution like Kali, Parrot, or Pentoo where the default user-agent needs obfuscation.

## Defense

- Enable and monitor GuardDuty for unusual API call patterns, including custom threat detection rules for user-agent anomalies.
- Implement AWS CloudTrail log integrity validation and forward logs to a central SIEM for correlation with other indicators.
- Use AWS IAM policies to restrict API calls from untrusted user-agents or IP ranges, and enable MFA for all privileged accounts.
- Regularly audit Boto3 usage in custom scripts and monitor for modifications to user-agent strings in application logs.

## Objectives

1. Modify the Boto3 session user-agent to remove identifiable OS indicators and evade GuardDuty findings.
2. Ensure API calls to AWS services are logged in CloudTrail without triggering automated alerts.
3. Maintain stealthy access to AWS resources for further operations like data exfiltration or lateral movement.

## Instructions

### Step 1: Verify Boto3 Installation and AWS Credentials

**Context**: Before modifying the user-agent, confirm that Boto3 is available and AWS credentials are configured to avoid authentication errors during testing.

Run the following Python command to test Boto3 session creation:

```python
python3 -c "import boto3; session = boto3.session.Session(); print('Boto3 session created successfully')"
```

> This verifies the library is installed and can create a session. If credentials are not set, configure them via AWS CLI: `aws configure`.

**Expected Output**: "Boto3 session created successfully" with no import or authentication errors.

### Step 2: Integrate User-Agent Modification Snippet

**Context**: Embed the user-agent modification code into your Boto3-based scripts. This snippet checks the current user-agent and alters it if it contains indicators of Kali, Parrot, or Pentoo Linux, preventing GuardDuty from flagging the OS.

Use the code snippet [[codes/Boto3-User-Agent-Modification-for-Evasion]] by inserting it at the beginning of your Python script before any API calls:

```python
boto3_session = boto3.session.Session()
ua = boto3_session._session.user_agent()
if 'kali' in ua.lower() or 'parrot' in ua.lower() or 'pentoo' in ua.lower():  # If the local OS is Kali/Parrot/Pentoo Linux
    # GuardDuty triggers a finding around API calls made from Kali Linux, so let's avoid that...
    self.print('Detected environment as one of Kali/Parrot/Pentoo Linux. Modifying user agent to hide that from GuardDuty...')
```

> Place this in a class or function where `self` is available (e.g., in a custom AWS client class). The code dynamically modifies the user-agent to a neutral string, such as a generic browser or application identifier. Test by printing the modified ua.

**Expected Output**: Console message indicating detection and modification, e.g., "Detected environment as one of Kali/Parrot/Pentoo Linux. Modifying user agent to hide that from GuardDuty...". Subsequent API calls should show a sanitized user-agent when inspected.

### Step 3: Test Obfuscated API Call

**Context**: Execute a benign API call (e.g., list S3 buckets) using the modified session to verify logs in CloudTrail do not trigger GuardDuty alerts.

Create a test script incorporating the snippet and run:

```python
python3 test_aws_call.py
```

Where test_aws_call.py includes the modification and a call like `s3 = boto3.client('s3'); print(s3.list_buckets())`.

> Monitor CloudTrail events in the AWS console or via CLI (`aws logs get-log-events`) for the API call. The user-agent in the log should lack Kali/Parrot/Pentoo indicators.

**Expected Output**: Successful API response (e.g., list of buckets) without immediate GuardDuty findings. CloudTrail logs show the request with obfuscated user-agent.

### Step 4: Validate Evasion in GuardDuty

**Context**: After running API calls, check GuardDuty for any new findings related to unusual user-agents or reconnaissance.

Use AWS CLI to query GuardDuty findings:

```bash
aws guardduty list-findings --detector-id <DETECTOR_ID>
```

> Replace <DETECTOR_ID> with your GuardDuty detector ID (find via `aws guardduty list-detectors`). If no findings appear for the test calls, the obfuscation succeeded.

**Expected Output**: Empty or unrelated findings list, confirming no triggers from the modified user-agent.

**Success Indicators**:
- No GuardDuty alerts for API calls from the testing environment.
- CloudTrail logs show API activity with neutral user-agent.
