---
id: f76b0cc2-75fe-4f32-901c-215d2eb8eaea
name: Login to Google Container Registry
type: command
executor: bash
data: docker login -e <service_account_email> -u oauth2accesstoken -p "<service_account_token>"
  https://gcr.io
output: null
created_at: '2023-04-06T03:56:17.031770+00:00'
updated_at: '2023-04-10T20:33:50.751327+00:00'
---

# Login to Google Container Registry

```bash
docker login -e <service_account_email> -u oauth2accesstoken -p "<service_account_token>" https://gcr.io
```
