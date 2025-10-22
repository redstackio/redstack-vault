---
id: d2ca4d8c-71bb-4753-a509-5c4b6105ef0e
name: Google Cloud Platform CLI Tool Cheatsheet
type: cheatsheet
verified: false
created_at: '2020-07-14T19:08:35.247198+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# Google Cloud Platform CLI Tool Cheatsheet

# Authentication

Authentication with gcloud

**Command** ([[user identity login]]):

```bash
gcloud auth login

```

**Command** ([[service account login]]):

```bash
gcloud auth activate-service-account --key-file creds.json

```

**Command** ([[List accounts available to gcloud]]):

```bash
gcloud auth list

```

# Account Information

**Command** ([[Get account information]]):

```bash
gcloud config list

```

**Command** ([[List organizations]]):

```bash
gcloud organizations list

```

**Command** ([[Enumerate IAM policies set ORG-wide]]):

```bash
gcloud organizations get-iam-policy <org ID>

```

**Command** ([[Enumerate IAM policies set per project]]):

```bash
gcloud projects get-iam-policy <project ID>

```

**Command** ([[List projects]]):

```bash
gcloud projects list

```

**Command** ([[Set a different project]]):

```bash
gcloud config set project <project name> 

```

**Command** ([[Gives a list of all APIs that are enabled in project]]):

```bash
gcloud services list

```

**Command** ([[Get source code repos available to user]]):

```bash
gcloud source repos list

```

**Command** ([[Clone repo to home dir]]):

```bash
gcloud source repos clone <repo_name>

```

# Virtual Machines

**Command** ([[List compute instances]]):

```bash
gcloud compute instances list

```

**Command** ([[Get shell access to instance]]):

```bash
gcloud beta compute ssh --zone "<region>" "<instance name>" --project "<project name>"

```

**Command** ([[Puts public ssh key onto metadata service for project]]):

```bash
gcloud compute ssh <local host>

```

**Command** ([[Get access scopes if on an instance]]):

```bash
curl http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/scopes -H &#39;Metadata-Flavor:Google’

```

**Command** ([[Use Google keyring to decrypt encrypted data]]):

```bash
gcloud kms decrypt --ciphertext-file=encrypted-file.enc --plaintext-file=out.txt --key <crypto-key> --keyring <crypto-keyring> --location global

```

# Storage Buckets

**Command** ([[List Google Storage buckets]]):

```bash
gsutil ls

```

**Command** ([[List Google Storage buckets recursively]]):

```bash
gsutil ls -r gs://<bucket name>

```

**Command** ([[Copy item from bucket]]):

```bash
gsutil cp gs://bucketid/item ~/

```

# Webapps & SQL

**Command** ([[List WebApps]]):

```bash
gcloud app instances list

```

**Command** ([[List SQL instances]]):

```bash
gcloud sql instances list

```

**Command** ([[List SQL databases]]):

```bash
gcloud sql databases list --instance <instance ID>

```

# Export SQL databases and buckets

**Command** ([[First copy buckets to local directory]]):

```bash
gsutil cp gs://bucket-name/folder/ .

```

**Command** ([[Create a new storage bucket, change perms, export SQL DB]]):

```bash
gsutil mb gs://<googlestoragename>
gsutil acl ch -u <service account> gs://<googlestoragename>
gcloud sql export sql <sql instance name> gs://<googlestoragename>/sqldump.gz --database=<database name>

```

# Networking

**Command** ([[List subnets]]):

```bash
gcloud compute networks subnets list

```

**Command** ([[List Interconnects (VPN)]]):

```bash
gcloud compute interconnects list

```

**Command** ([[List Containers]]):

```bash
gcloud container clusters list

```

**Command** ([[GCP Kubernetes config file ~/.kube/config gets generated when you are authenticated with gcloud and run:]]):

```bash
gcloud container clusters get-credentials <cluster name> --region <region>

```

**Command** ([[If successful and the user has the correct permission the Kubernetes command below can be used to get cluster info:]]):

```bash
kubectl cluster-info

```

# Serverless

**Command** ([[GCP functions log analysis – May get useful information from logs associated with GCP functions]]):

```bash
gcloud functions list
gcloud functions describe <function name>
gcloud functions logs read <function name> --limit <number of lines>

```

Gcloud stores creds in ~/.config/gcloud/credentials.db

**Command** ([[Search home directories]]):

```bash
sudo find /home -name "credentials.db

```

**Command** ([[Copy gcloud dir to your own home directory to auth as the compromised user]]):

```bash
sudo cp -r /home/username/.config/gcloud ~/.config
sudo chown -R currentuser:currentuser ~/.config/gcloud
gcloud auth list

```

**Command** ([[Metadata Service URL]]):

```bash
curl "http://metadata.google.internal/computeMetadata/v1/?recursive=true&alt=text" -H "Metadata-Flavor: Google"

```
