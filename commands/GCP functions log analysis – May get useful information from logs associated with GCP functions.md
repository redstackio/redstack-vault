---
id: 31fbd66b-9ce4-4d2d-806d-c810eb82b1a1
name: GCP functions log analysis – May get useful information from logs associated
  with GCP functions
type: command
executor: bash
data: 'gcloud functions list

  gcloud functions describe <function name>

  gcloud functions logs read <function name> --limit <number of lines>

  '
output: null
created_at: '2020-07-14T19:08:34.241316+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# GCP functions log analysis – May get useful information from logs associated with GCP functions

```bash
gcloud functions list
gcloud functions describe <function name>
gcloud functions logs read <function name> --limit <number of lines>

```
