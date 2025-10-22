---
id: e1d94a0c-2501-4523-8aff-4b5f02dffc32
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:09.572338+00:00'
updated_at: '2023-04-10T20:19:44.887822+00:00'
---

# Code Snippet e1d94a0c

**Language**: Powershell

```powershell
# create a new image for the instance-id
$ aws ec2 create-image --instance-id i-0438b003d81cd7ec5 --name "AWS Audit" --description "Export AMI" --region eu-west-1  

# add key to AWS
$ aws ec2 import-key-pair --key-name "AWS Audit" --public-key-material file://~/.ssh/id_rsa.pub --region eu-west-1  

# create ec2 using the previously created AMI, use the same security group and subnet to connect easily.
$ aws ec2 run-instances --image-id ami-0b77e2d906b00202d --security-group-ids "sg-6d0d7f01" --subnet-id subnet-9eb001ea --count 1 --instance-type t2.micro --key-name "AWS Audit" --query "Instances[0].InstanceId" --region eu-west-1

# now you can check the instance 
aws ec2 describe-instances --instance-ids i-0546910a0c18725a1 

# If needed : edit groups
aws ec2 modify-instance-attribute --instance-id "i-0546910a0c18725a1" --groups "sg-6d0d7f01"  --region eu-west-1

# be a good guy, clean our instance to avoid any useless cost
aws ec2 stop-instances --instance-id "i-0546910a0c18725a1" --region eu-west-1 
aws ec2 terminate-instances --instance-id "i-0546910a0c18725a1" --region eu-west-1
```
