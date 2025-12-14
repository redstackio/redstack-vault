---
id: cmd-git-clone-001
data: 'git clone #{ content_tag(:span, default_url_to_repo, class: ''js-clone'') }'
tags:
  - git
  - clone
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:06.918Z'
verified: false
validated: true
submitted: true
---
# git-clone

## Command

```bash
git clone #{ content_tag(:span, default_url_to_repo, class: 'js-clone') }
```

## Description

Clones a Git repository from a URL. In GitLab's vulnerable setup display, the URL is wrapped in HAML content_tag, but adjacent injections from branch names can pollute the execution context with JS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `url` | The repository URL to clone | Yes |
| `#{ content_tag(:span, default_url_to_repo, class: 'js-clone') }` | HAML interpolation for URL with class; potential vector if combined with XSS | Yes |

## Examples

### Basic Usage

```bash
git clone https://gitlab.com/user/repo.git
```

### Advanced Usage

```bash
git clone #{ content_tag(:span, default_url_to_repo, class: 'js-clone') }  # As in GitLab template
```

## Expected Output

Clones repo into a new directory; progress shown.

## Related

- [[commands/cd-project-path]]
- [[procedures/Create-Blank-Project-to-Host-XSS-Payload]]
