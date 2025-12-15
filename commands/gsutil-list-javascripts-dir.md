---
id: c1b2c3d4-e5f6-7890-abcd-ef1234567892
data: 'gsutil ls gs://about.gitlab.com/javascripts/'
tags:
  - gcs
  - directory-listing
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:28.459Z'
verified: false
validated: true
submitted: true
---
# gsutil-list-javascripts-dir

## Command

```bash
gsutil ls gs://about.gitlab.com/javascripts/
```

## Description

Enumerates JavaScript and other files in the javascripts/ directory of the public GCS bucket, aiding in identification of additional sensitive assets.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| ls | List objects in directory | Yes |
| gs://about.gitlab.com/javascripts/ | Target directory path | Yes |

## Examples

### Basic Usage

```bash
gsutil ls gs://about.gitlab.com/javascripts/
```

### Advanced Usage

```bash
gsutil ls gs://about.gitlab.com/javascripts/*.js  # Filter JS files
```

## Expected Output

List of files in the directory, such as various .js files, confirming public access to web-related assets.

## Related

- [[commands/gsutil-list-main-bucket]]
- [[procedures/Download-Sensitive-Files-from-GCS-Bucket]]
