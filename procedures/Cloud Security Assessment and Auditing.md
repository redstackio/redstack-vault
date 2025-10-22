---
id: c595e8c6-b062-4e3d-8749-d64447b6f88e
name: Cloud Security Assessment and Auditing
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:09.014046+00:00'
updated_at: '2023-04-10T20:20:58.720135+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Discovery|TA0007 - Discovery]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Cloud Service Dashboard|T1538 - Cloud Service Dashboard]]'
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
- '[[Data from Cloud Storage|T1530 - Data from Cloud Storage]]'
- '[[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]'
- '[[Internal Spearphishing|T1534 - Internal Spearphishing]]'
- '[[Steal Web Session Cookie|T1539 - Steal Web Session Cookie]]'
tags:
- '[[Cloud - AWS]]'
- '[[Tools]]'
commands:
- '[[Audit account]]'
- '[[Clone cloudmapper repository]]'
- '[[Clone Pacu Repository]]'
- '[[Clone prowler repository]]'
- '[[Clone s3_objects_check repository]]'
- '[[Clone ScoutSuite repository]]'
- '[[Clone SkyArk Repository]]'
- '[[Collect metadata]]'
- '[[Create and activate Python virtual environment]]'
- '[[Display help menu for s3-objects-check.py]]'
- '[[Download AWS IAM Configuration]]'
- '[[Download AWStealth PowerShell Script]]'
- '[[Download bucket_finder_1.1.tar.bz2]]'
- '[[Download buckets in my_words with region ie]]'
- '[[EC2 Describe Instances]]'
- '[[Find admin users and roles]]'
- '[[Generate HTML report]]'
- '[[Generate IAM HTML report]]'
- '[[Get help with AWS provider]]'
- '[[Import SkyArk PowerShell Module]]'
- '[[Install awscli, ansi2html and detect-secrets]]'
- '[[Install Cloudsplaining]]'
- '[[Install dependencies]]'
- '[[Install jq]]'
- '[[Install Pacu]]'
- '[[Install required packages]]'
- '[[Lambda Get Account Settings]]'
- '[[Lambda Get Function]]'
- '[[List Files]]'
- '[[List S3 Buckets]]'
- '[[Provide AWS credentials]]'
- '[[Provide Azure credentials]]'
- '[[Run Module in Specific Regions]]'
- '[[Run Module with Arguments]]'
- '[[Run Pacu]]'
- '[[Run prowler check42 and check43]]'
- '[[Run prowler custom-profile in us-east-1]]'
- '[[Run prowler with sts assume-role]]'
- '[[Run s3-objects-check.py with specified profiles]]'
- '[[Scan AWS Shadow Admins]]'
- '[[Scan IAM Configuration]]'
- '[[Search buckets in my_words with default region]]'
- '[[Search buckets in my_words with region ie]]'
- '[[Search buckets in my_words with region ie and log output to bucket.out]]'
- '[[Set Keys or Swap Keys]]'
- '[[Start AWS Stealth Scan]]'
---

# Cloud Security Assessment and Auditing

## Summary

The Cloud Security Assessment and Auditing procedure involves using various AWS tools to discover and assess the security posture of an organization's cloud environment. The procedure starts with discovering AWS shadow admins using SkyArk, followed by exploiting vulnerabilities with Pacu. The proce

## Description

# Description

The Cloud Security Assessment and Auditing procedure involves using various AWS tools to discover and assess the security posture of an organization's cloud environment. The procedure starts with discovering AWS shadow admins using SkyArk, followed by exploiting vulnerabilities with Pacu. The procedure then moves on to searching for public buckets and downloading files using Bucket Finder, and listing S3 buckets. Prowler is used to assess the security of the AWS environment against best practices, while Principal Mapper is used to map AWS IAM principals. ScoutSuite is used for multi-cloud security auditing, and S3 Object Permissions Checker is used to check S3 object permissions. Cloudsplaining is used to assess IAM security, and AWS Attack Library Commands are used to test the environment against known attack techniques. Finally, CloudMapper is used for AWS environment analysis.

## Requirements

1. Access to AWS environment

1. Credentials with appropriate permissions

1. Tools used in the procedure

## Defense

1. Regularly monitor AWS environment for shadow admins and unexpected changes in permissions

1. Implement least privilege access control to limit the impact of potential attacks

1. Implement multi-factor authentication to prevent unauthorized access to AWS environment

## Objectives

1. Discover AWS shadow admins

1. Exploit vulnerabilities

1. Assess security posture of AWS environment

1. Check S3 object permissions

1. Assess IAM security

1. Test environment against known attack techniques

1. Analyze AWS environment

# Instructions

1. To discover the AWS Shadow Admins, follow the below steps:
1. Clone the SkyArk repository from GitHub using the command: $ git clone https://github.com/cyberark/SkyArk
2. Open PowerShell and execute the command: $ powershell -ExecutionPolicy Bypass -NoProfile
3. Import the SkyArk module by executing the command: PS C> Import-Module .\SkyArk.ps1 -force
4. Start the AWS Stealth scan by executing the command: PS C> Start-AWStealth
5. Alternatively, execute the below command in the Cloud Console: PS C> IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/cyberark/SkyArk/master/AWStealth/AWStealth.ps1')
6. Finally, execute the command: PS C> Scan-AWShadowAdmins

**Code**: [[$ git clone https://github.com/cyberark/SkyArk
$ p]]

> This command is used to discover the most privileged users in the scanned AWS environment, including the AWS Shadow Admins. The command first clones the SkyArk repository from GitHub and imports the SkyArk module. Then, it starts the AWS Stealth scan to discover the AWS Shadow Admins. Alternatively, the command can be executed in the Cloud Console. Finally, it executes the Scan-AWShadowAdmins command to display the discovered AWS Shadow Admins.

**Command** ([[Clone SkyArk Repository]]):

```bash
$ git clone https://github.com/cyberark/SkyArk
```

**Command** ([[Import SkyArk PowerShell Module]]):

```powershell
PS C> Import-Module .\SkyArk.ps1 -force
```

**Command** ([[Start AWS Stealth Scan]]):

```powershell
PS C> Start-AWStealth
```

**Command** ([[Download AWStealth PowerShell Script]]):

```powershell
PS C> IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/cyberark/SkyArk/master/AWStealth/AWStealth.ps1')
```

**Command** ([[Scan AWS Shadow Admins]]):

```powershell
PS C> Scan-AWShadowAdmins
```

2. To use Pacu, first clone the repository using `git clone https://github.com/RhinoSecurityLabs/pacu`. Next, run `bash install.sh` to install the necessary dependencies. Finally, run `python3 pacu.py` to start the tool. Once inside the tool, use the `set_keys` or `swap_keys` commands to set or swap AWS access keys. Use the `ls` command to list available modules, and `run <module_name> [--keyword-arguments]` to run a module with optional keyword arguments. For example, `run ec2_enum --regions us-east-1,us-west-2` would run the `ec2_enum` module in the `us-east-1` and `us-west-2` regions.

**Code**: [[$ git clone https://github.com/RhinoSecurityLabs/p]]

> Pacu is an AWS exploitation tool developed by Rhino Security Labs. It allows users to identify and exploit configuration flaws within an AWS environment using an extensible collection of modules with a diverse feature-set. The tool can be used to perform a variety of tasks, such as enumerating EC2 instances, dumping S3 buckets, and more. To use the tool, users must first clone the repository, install the necessary dependencies, and set or swap AWS access keys. Once inside the tool, users can list available modules and run them with optional keyword arguments. More information on available modules can be found in the tool's documentation.

**Command** ([[Clone Pacu Repository]]):

```bash
$ git clone https://github.com/RhinoSecurityLabs/pacu
```

**Command** ([[Install Pacu]]):

```bash
$ bash install.sh
```

**Command** ([[Run Pacu]]):

```bash
$ python3 pacu.py
```

**Command** ([[Set Keys or Swap Keys]]):

```bash
set_keys/swap_keys
```

**Command** ([[List Files]]):

```bash
ls
```

**Command** ([[Run Module with Arguments]]):

```bash
run <module_name> [--keyword-arguments]
```

**Command** ([[Run Module in Specific Regions]]):

```bash
run <module_name> --regions eu-west-1,us-west-1
```

3. To use this command, follow the steps below:
1. Download the bucket_finder_1.1.tar.bz2 file using the command 'wget https://digi.ninja/files/bucket_finder_1.1.tar.bz2 -O bucket_finder_1.1.tar.bz2'
2. Run the command './bucket_finder.rb my_words' to search for public buckets
3. Run the command './bucket_finder.rb --region ie my_words' to search for public buckets in a specific region
4. Run the command './bucket_finder.rb --download --region ie my_words' to download all files in a public bucket in a specific region
5. Run the command './bucket_finder.rb --log-file bucket.out my_words' to log the output of the command to a file named 'bucket.out'

**Code**: [[wget https://digi.ninja/files/bucket_finder_1.1.ta]]

> The 'wget' command is used to download the bucket_finder_1.1.tar.bz2 file from the specified URL and save it as 'bucket_finder_1.1.tar.bz2'. The './bucket_finder.rb my_words' command is used to search for public buckets using a wordlist named 'my_words'. The './bucket_finder.rb --region ie my_words' command is used to search for public buckets in a specific region (in this case, Ireland) using a wordlist named 'my_words'. The './bucket_finder.rb --download --region ie my_words' command is used to download all files in a public bucket in a specific region (in this case, Ireland) using a wordlist named 'my_words'. The './bucket_finder.rb --log-file bucket.out my_words' command is used to log the output of the command to a file named 'bucket.out' while searching for public buckets using a wordlist named 'my_words'.

**Command** ([[Download bucket_finder_1.1.tar.bz2]]):

```bash
wget https://digi.ninja/files/bucket_finder_1.1.tar.bz2 -O bucket_finder_1.1.tar.bz2
```

**Command** ([[Search buckets in my_words with default region]]):

```bash
./bucket_finder.rb my_words
```

**Command** ([[Search buckets in my_words with region ie]]):

```bash
./bucket_finder.rb --region ie my_words
```

**Command** ([[Download buckets in my_words with region ie]]):

```bash
./bucket_finder.rb --download --region ie my_words
```

**Command** ([[Search buckets in my_words with region ie and log output to bucket.out]]):

```bash
./bucket_finder.rb --log-file bucket.out my_words
```

4. This command lists all S3 buckets in the specified region.

**Code**: [[import boto3

# Create an S3 client
s3 = boto3.cli]]

> Arguments:
None

This command uses the `boto3` library to create an S3 client and then calls the `list_buckets` method to retrieve a list of all S3 buckets in the specified region. If successful, the list of buckets is returned. If an error occurs, the error message is printed.

**Command** ([[List S3 Buckets]]):

```bash
import boto3

# Create an S3 client
s3 = boto3.client('s3', aws_access_key_id='AKIAJQDP3RKREDACTED', aws_secret_access_key='igH8yFmmpMbnkcUaCqXJIRIozKVaREDACTED', region_name='us-west-1')

try:
    # List all S3 buckets
    result = s3.list_buckets()
    print(result)
except Exception as e:
    print(e)
```

5. To perform AWS security best practices assessment using Prowler, follow these steps:
1. Install awscli, ansi2html, and detect-secrets using pip.
2. Clone the Prowler repository from GitHub.
3. Install jq using sudo apt install jq.
4. Run Prowler with the desired checks using the following commands:
- ./prowler -E check42,check43
- ./prowler -p custom-profile -r us-east-1 -c check11
- ./prowler -A 123456789012 -R ProwlerRole  # sts assume-role
Note: Replace the profile, region, account ID, and role name with your own values.

**Code**: [[$ pip install awscli ansi2html detect-secrets
$ gi]]

> Prowler is a tool for performing AWS security best practices assessments, audits, incident response, continuous monitoring, hardening and forensics readiness. It is a command-line tool that checks for security vulnerabilities in AWS services and resources. The commands provided in the data field are used to install Prowler and its dependencies, and to run Prowler with different checks. The -E option is used to exclude certain checks, the -p option is used to specify a custom profile, the -r option is used to specify the region, the -c option is used to specify a specific check, and the -A and -R options are used to assume a role before running Prowler. The instruction field provides step-by-step instructions for using Prowler, and the explain field provides an overview of what Prowler is and what it does.

**Command** ([[Install awscli, ansi2html and detect-secrets]]):

```bash
$ pip install awscli ansi2html detect-secrets
```

**Command** ([[Clone prowler repository]]):

```bash
$ git clone https://github.com/toniblyx/prowler
```

**Command** ([[Install jq]]):

```bash
$ sudo apt install jq
```

**Command** ([[Run prowler check42 and check43]]):

```bash
$ ./prowler -E check42,check43
```

**Command** ([[Run prowler custom-profile in us-east-1]]):

```bash
$ ./prowler -p custom-profile -r us-east-1 -c check11
```

**Command** ([[Run prowler with sts assume-role]]):

```bash
$ ./prowler -A 123456789012 -R ProwlerRole  # sts assume-role
```

6. To use Principal Mapper, install it using pip and run the following commands:

- `pmapper graph --create` to create a graph of the IAM permissions in your AWS environment.
- `pmapper visualize --filetype png` to visualize the graph in PNG format.
- `pmapper analysis --output-type text` to analyze the permissions and output the results in text format.

You can also use the following commands to determine if a PowerUser can escalate privileges or to find all principals that can access or be accessed by a PowerUser:

- `pmapper query "preset privesc user/PowerUser"`
- `pmapper argquery --principal user/PowerUser --preset privesc`
- `pmapper query "preset privesc *"`
- `pmapper argquery --principal '*' --preset privesc`
- `pmapper query "preset connected user/PowerUser *"`
- `pmapper argquery --principal user/PowerUser --resource '*' --preset connected`
- `pmapper query "preset connected * user/PowerUser"`
- `pmapper argquery --principal '*' --resource user/PowerUser --preset connected`

**Code**: [[https://github.com/nccgroup/PMapper
pip install pr]]

> Principal Mapper is a tool that helps evaluate IAM permissions in AWS. It provides various commands to create a graph of IAM permissions, visualize the graph, and analyze the permissions. Additionally, it provides commands to determine if a PowerUser can escalate privileges and to find all principals that can access or be accessed by a PowerUser.

7. To use ScoutSuite, first clone the repository using the following command:

$ git clone https://github.com/nccgroup/ScoutSuite

Once cloned, navigate to the ScoutSuite directory and run the following command to see available commands and arguments for a specific cloud provider:

$ python scout.py PROVIDER --help

To audit the security of an AWS account, use the following command with the appropriate access key ID, secret access key, and session token (if applicable):

$ python scout.py aws --access-keys --access-key-id <ACCESS_KEY_ID> --secret-access-key <SECRET_ACCESS_KEY> --session-token <SESSION_TOKEN>

To audit the security of an Azure account, use the following command with the Azure CLI installed:

$ python scout.py azure --cli

**Code**: [[$ git clone https://github.com/nccgroup/ScoutSuite]]

> ScoutSuite is a multi-cloud security auditing tool that can be used to audit the security of AWS and Azure accounts. To use ScoutSuite, first clone the repository using the provided command. Once cloned, navigate to the ScoutSuite directory and run the provided command to see available commands and arguments for a specific cloud provider. To audit the security of an AWS account, use the provided command with the appropriate access key ID, secret access key, and session token (if applicable). To audit the security of an Azure account, use the provided command with the Azure CLI installed.

**Command** ([[Clone ScoutSuite repository]]):

```bash
$ git clone https://github.com/nccgroup/ScoutSuite

```

**Command** ([[Get help with AWS provider]]):

```bash
$ python scout.py PROVIDER --help

```

**Command** ([[Provide AWS credentials]]):

```bash
$ python scout.py aws --access-keys --access-key-id <AKIAIOSFODNN7EXAMPLE> --secret-access-key <wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY> --session-token <token>

```

**Command** ([[Provide Azure credentials]]):

```bash
$ python scout.py azure --cli
```

8. To use this tool, first clone the repository using the command `git clone https://github.com/nccgroup/s3_objects_check`. Then, navigate to the cloned directory and create a virtual environment using `python3 -m venv env && source env/bin/activate`. Next, install the required dependencies using `pip install -r requirements.txt`. Finally, run the tool using `python s3-objects-check.py -p whitebox-profile -e blackbox-profile`, where `whitebox-profile` is the name of the profile containing your AWS access key and secret access key, and `blackbox-profile` is the name of the profile containing the access keys for the target account you wish to test.

**Code**: [[$ git clone https://github.com/nccgroup/s3_objects]]

> This tool is used to evaluate the effective permissions of objects stored in an S3 bucket. It does this by performing a whitebox analysis of the bucket, using the AWS SDK to determine which objects are publicly accessible. The tool requires two AWS profiles to be set up - a 'whitebox' profile containing your own AWS access key and secret access key, and a 'blackbox' profile containing the access keys for the target account you wish to test. The tool will then use the AWS SDK to query the target account and determine which objects are publicly accessible. The results of the analysis are output to the console.

**Command** ([[Clone s3_objects_check repository]]):

```bash
$ git clone https://github.com/nccgroup/s3_objects_check
```

**Command** ([[Create and activate Python virtual environment]]):

```bash
$ python3 -m venv env && source env/bin/activate
```

**Command** ([[Install required packages]]):

```bash
$ pip install -r requirements.txt
```

**Command** ([[Display help menu for s3-objects-check.py]]):

```bash
$ python s3-objects-check.py -h
```

**Command** ([[Run s3-objects-check.py with specified profiles]]):

```bash
$ python s3-objects-check.py -p whitebox-profile -e blackbox-profile
```

9. To use cloudsplaining, first install it using the pip3 command. Then, download your AWS IAM policies using the cloudsplaining download command. Finally, run the cloudsplaining scan command to identify any violations of least privilege and generate a report.

**Code**: [[$ pip3 install --user cloudsplaining
$ cloudsplain]]

> The `cloudsplaining` tool is used to assess the security of AWS IAM policies. It identifies any violations of the principle of least privilege, which states that each user should only have the minimum permissions necessary to perform their job. The `download` command is used to download the IAM policies of the AWS account specified in the `--profile` argument. The `scan` command is used to scan the downloaded policies and generate a report that prioritizes the risks identified. The `--input-file` argument specifies the path to the downloaded policies in JSON format.

**Command** ([[Install Cloudsplaining]]):

```bash
$ pip3 install --user cloudsplaining
```

**Command** ([[Download AWS IAM Configuration]]):

```bash
$ cloudsplaining download --profile myawsprofile
```

**Command** ([[Scan IAM Configuration]]):

```bash
$ cloudsplaining scan --input-file default.json
```

10. To use the AWS Attack Library, run the following commands:

**Code**: [[python3 weirdAAL.py -m ec2_describe_instances -t d]]

> The AWS Attack Library provides a set of commands to perform attacks and security assessments against Amazon Web Services (AWS) environments. The commands included in this JSON object are just a few examples of what can be done with the library.

- `ec2_describe_instances`: This command will retrieve information about all EC2 instances in the specified AWS account and region. The `-t` flag specifies the target profile to use.

- `lambda_get_account_settings`: This command will retrieve account settings for AWS Lambda in the specified AWS account and region. The `-t` flag specifies the target profile to use.

- `lambda_get_function`: This command will retrieve information about the specified AWS Lambda function in the specified AWS account and region. The `-a` flag specifies the function name and region, and the `-t` flag specifies the target profile to use.

**Command** ([[EC2 Describe Instances]]):

```bash
python3 weirdAAL.py -m ec2_describe_instances -t demo
```

**Command** ([[Lambda Get Account Settings]]):

```bash
python3 weirdAAL.py -m lambda_get_account_settings -t demo
```

**Command** ([[Lambda Get Function]]):

```bash
python3 weirdAAL.py -m lambda_get_function -a 'MY_LAMBDA_FUNCTION','us-west-2' -t yolo
```

11. To use CloudMapper, clone the repository and install the required dependencies. Then, run one of the available commands to generate an HTML report, audit your AWS environment, collect metadata, or find admin users and roles.

**Code**: [[git clone https://github.com/duo-labs/cloudmapper.]]

> CloudMapper is a tool that helps you analyze your Amazon Web Services (AWS) environments. It provides several commands that can be used to generate reports, audit your environment, collect metadata, and identify admin users and roles. To use CloudMapper, you need to clone the repository and install the required dependencies. Once you have done that, you can run one of the available commands to perform the desired action. The available commands are:

- report: Generates an HTML report that includes a summary of the accounts and audit findings.
- iam_report: Generates an HTML report for the IAM information of an account.
- audit: Checks for potential misconfigurations.
- collect: Collects metadata about an account.
- find_admins: Looks at IAM policies to identify admin users and roles, or principals with specific privileges.

**Command** ([[Clone cloudmapper repository]]):

```bash
git clone https://github.com/duo-labs/cloudmapper.git
```

**Command** ([[Install dependencies]]):

```bash
sudo yum install autoconf automake libtool python3-devel.x86_64 python3-tkinter python-pip jq awscli
# You may additionally need "build-essential"
sudo apt-get install autoconf automake libtool python3.7-dev python3-tk jq awscli
pipenv install --skip-lock
pipenv shell
```

**Command** ([[Generate HTML report]]):

```bash
pipenv run python cloudmapper.py report
```

**Command** ([[Generate IAM HTML report]]):

```bash
pipenv run python cloudmapper.py iam_report
```

**Command** ([[Audit account]]):

```bash
pipenv run python cloudmapper.py audit
```

**Command** ([[Collect metadata]]):

```bash
pipenv run python cloudmapper.py collect
```

**Command** ([[Find admin users and roles]]):

```bash
pipenv run python cloudmapper.py find_admins
```

## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]
- [[Credential Access|TA0006 - Credential Access]]
- [[Discovery|TA0007 - Discovery]]
- [[Execution|TA0002 - Execution]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Cloud Service Dashboard|T1538 - Cloud Service Dashboard]]
- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]
- [[Data from Cloud Storage|T1530 - Data from Cloud Storage]]
- [[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]
- [[Internal Spearphishing|T1534 - Internal Spearphishing]]
- [[Steal Web Session Cookie|T1539 - Steal Web Session Cookie]]

## Commands Used

- [[Audit account]]
- [[Clone cloudmapper repository]]
- [[Clone Pacu Repository]]
- [[Clone prowler repository]]
- [[Clone s3_objects_check repository]]
- [[Clone ScoutSuite repository]]
- [[Clone SkyArk Repository]]
- [[Collect metadata]]
- [[Create and activate Python virtual environment]]
- [[Display help menu for s3-objects-check.py]]
- [[Download AWS IAM Configuration]]
- [[Download AWStealth PowerShell Script]]
- [[Download bucket_finder_1.1.tar.bz2]]
- [[Download buckets in my_words with region ie]]
- [[EC2 Describe Instances]]
- [[Find admin users and roles]]
- [[Generate HTML report]]
- [[Generate IAM HTML report]]
- [[Get help with AWS provider]]
- [[Import SkyArk PowerShell Module]]
- *...and 26 more*

## Tags

- [[Cloud - AWS]]
- [[Tools]]
