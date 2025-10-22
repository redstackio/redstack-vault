---
id: cd3cc7c8-dc23-426c-b4e2-fa4eb6637560
name: aws cloudfront invalidate file from distribution
type: command
executor: bash
data: 'aws cloudfront create-invalidation --distribution-id $DISTRIBUTION_ID  --paths
  $FILE_PATH $FILE_PATH_2

  '
output: aws cloudfront create-invalidation --distribution-id Z2W2LX9VBMAPRX --paths
  /index.html /error.html
created_at: '2020-07-31T04:25:30.278247+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# aws cloudfront invalidate file from distribution

```bash
aws cloudfront create-invalidation --distribution-id $DISTRIBUTION_ID  --paths $FILE_PATH $FILE_PATH_2

```

## Expected Output

```
aws cloudfront create-invalidation --distribution-id Z2W2LX9VBMAPRX --paths /index.html /error.html
```
