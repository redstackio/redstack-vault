---
id: 0fd260be-f9ef-49da-a623-3e63b8faa401
name: Create a new storage bucket, change perms, export SQL DB
type: command
executor: bash
data: 'gsutil mb gs://<googlestoragename>

  gsutil acl ch -u <service account> gs://<googlestoragename>

  gcloud sql export sql <sql instance name> gs://<googlestoragename>/sqldump.gz --database=<database
  name>

  '
output: null
created_at: '2020-07-14T19:08:34.239922+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Create a new storage bucket, change perms, export SQL DB

```bash
gsutil mb gs://<googlestoragename>
gsutil acl ch -u <service account> gs://<googlestoragename>
gcloud sql export sql <sql instance name> gs://<googlestoragename>/sqldump.gz --database=<database name>

```


