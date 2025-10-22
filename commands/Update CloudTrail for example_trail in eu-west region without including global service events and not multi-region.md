---
id: ca793cc6-0027-47ed-8feb-65657f53e5ad
name: Update CloudTrail for example_trail in eu-west region without including global
  service events and not multi-region
type: command
executor: bash
data: aws cloudtrail update-trail --name example_trail --no-include-global-service-event
  --no-is-multi-region --region=eu-west
output: null
created_at: '2023-04-06T03:56:14.180227+00:00'
updated_at: '2023-04-10T20:20:22.191166+00:00'
---

# Update CloudTrail for example_trail in eu-west region without including global service events and not multi-region

```bash
aws cloudtrail update-trail --name example_trail --no-include-global-service-event --no-is-multi-region --region=eu-west
```
