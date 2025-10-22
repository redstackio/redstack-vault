---
id: c8d6445b-f799-43d5-aea3-e595f04e5097
name: aws cloudfront invalidate files with wildcard from distribution
type: command
executor: bash
data: 'aws cloudfront create-invalidation --distribution-id $DISTRIBUTION_ID  --paths
  $FILE_PATH

  '
output: aws cloudfront create-invalidation --distribution-id Z2W2LX9VBMAPRX  --paths
  '/*'
created_at: '2020-07-31T04:25:30.278405+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# aws cloudfront invalidate files with wildcard from distribution

```bash
aws cloudfront create-invalidation --distribution-id $DISTRIBUTION_ID  --paths $FILE_PATH

```

## Expected Output

```
aws cloudfront create-invalidation --distribution-id Z2W2LX9VBMAPRX  --paths '/*'
```
