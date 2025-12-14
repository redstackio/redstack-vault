---
data: bundle exec rails s
tags:
  - server
  - rails
  - deploy
type: command
output: 'Server running on http://127.0.0.1:3000'
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:43.902Z'
id: 50498560-72f6-420a-becf-5eba95e618c9
verified: false
validated: true
submitted: true
---
# bundle-exec-rails-server

## Command

```bash
bundle exec rails s
```

## Description

Starts the Rails development server using Bundler to ensure dependencies are loaded, running on port 3000 for testing the PoC.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| s | Server alias | Yes |

## Examples

### Basic Usage

```bash
bundle exec rails s
```

### Advanced Usage

```bash
bundle exec rails s -p 3001
```

## Expected Output

=> Booting Puma
=> Rails 7.1.2 application starting in development
=> Run `bin/rails server --help` for more startup options
Puma starting in single mode...
* Puma version: 5.6.7
* Min threads: 5
* Max threads: 5
* Environment: development
* PID: 12345
* Listening on http://127.0.0.1:3000
Use Ctrl-C to stop

## Related

- [[commands/cd-rails-server]]
