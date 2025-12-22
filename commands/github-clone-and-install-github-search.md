---
id: new-uuid-for-clone-command
name: github-clone-and-install-github-search
type: command
executor: bash
data: >
  git clone https://github.com/gwen001/github-search.git && cd github-search &&
  pip3 install -r requirements.txt
output: null
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - installation
  - setup
verified: true
validated: true
---

# github-clone-and-install-github-search

## Command

```bash
git clone https://github.com/gwen001/github-search.git && cd github-search && pip3 install -r requirements.txt
```

## Description

This command clones the github-search repository from GitHub and installs its Python dependencies, preparing the environment to run scripts like github-subdomains.py for reconnaissance tasks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `https://github.com/gwen001/github-search.git` | Repository URL to clone | Yes |
| `pip3 install -r requirements.txt` | Installs dependencies like requests | Yes |

## Examples

### Basic Usage

```bash
git clone https://github.com/gwen001/github-search.git && cd github-search && pip3 install -r requirements.txt
```

### Advanced Usage

If behind a proxy: Add `git config --global http.proxy http://proxy:port` before cloning.

```bash
git config --global http.proxy http://proxy:port && git clone https://github.com/gwen001/github-search.git && cd github-search && pip3 install -r requirements.txt
```

## Expected Output

Cloning into 'github-search'...
remote: Enumerating objects: X, done.
...
Successfully installed requests-2.x.x beautifulsoup4-4.x.x

## Related

- [[procedures/Scrape-GitHub-Repositories-for-Subdomains]]
- [[tools/GitHub-Subdomains]]
