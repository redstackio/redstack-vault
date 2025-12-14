---
data: >-
  git clone https://github.com/organization/repo-name.git && cd repo-name &&
  grep -r -i "token\|key\|secret" .
tags:
  - git
  - discovery
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 4e004a35-5bca-4bbf-bb65-5f8fe379f2c7
created_at: '2025-12-14T17:32:10.804Z'
updated_at: '2025-12-14T17:32:10.804Z'
verified: false
validated: true
submitted: true
---
# git-clone-repo

## Command

```bash
git clone https://github.com/organization/repo-name.git && cd repo-name && grep -r -i "token\|key\|secret" .
```

## Description

Clones a public GitHub repository and searches its contents for keywords indicative of exposed secrets like tokens or keys, useful for local inspection of information disclosures.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `git clone URL` | Clones the repository from the given URL | Yes |
| `cd repo-name` | Changes into the cloned directory | Yes |
| `grep -r -i "pattern" .` | Recursively searches files case-insensitively for patterns | Yes |

## Examples

### Basic Usage

```bash
git clone https://github.com/reverb/experimental.git
cd experimental
grep -r "token" .
```

### Advanced Usage

```bash
git clone https://github.com/org/repo.git && cd repo && grep -r -E "(api_|access_)token" --include="*.js" .
```

## Expected Output

File paths and matching lines, e.g.,:

```bash
./config.js: export const API_TOKEN = 'abc123...';
```

## Related

- [[commands/github-search-tokens]]
- [[procedures/Discover-Exposed-Tokens-in-Public-GitHub-Repositories]]
