---
data: >-
  @text.gsub(@pattern) do |markdown| file = find_file(@source_project,
  $~[:secret], $~[:file]) break markdown unless file.try(:exists?) klass =
  target_parent.is_a?(Namespace) ? NamespaceFileUploader : FileUploader moved =
  klass.copy_to(file, target_parent) ... def find_file(project, secret, file)
  uploader = FileUploader.new(project, secret: secret)
  uploader.retrieve_from_store!(file) uploader end
tags:
  - gitlab
  - vulnerability
type: command
executor: ruby
platforms:
  - Linux
id: 5ad647ea-fb80-4d25-b837-c724abf2d30d
created_at: '2025-12-11T03:47:59.040Z'
updated_at: '2025-12-11T03:47:59.040Z'
verified: false
validated: true
submitted: true
---
# uploads-rewriter-gsub

## Command

```ruby
@text.gsub(@pattern) do |markdown| file = find_file(@source_project, $~[:secret], $~[:file]) break markdown unless file.try(:exists?) klass = target_parent.is_a?(Namespace) ? NamespaceFileUploader : FileUploader moved = klass.copy_to(file, target_parent) ... def find_file(project, secret, file) uploader = FileUploader.new(project, secret: secret) uploader.retrieve_from_store!(file) uploader end
```

## Description

Code snippet from GitLab's UploadsRewriter that replaces upload references and copies files without path validation, enabling traversal.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `gsub` | Replaces matches | Yes |
| `find_file` | Retrieves file | Yes |

## Examples

### Basic Usage

Used internally during issue movement.

## Expected Output

Copied file in new project.

## Related

- [[commands/gitlab-markdown-traversal]]
- [[procedures/Move-Issue-to-Trigger-Arbitrary-File-Read]]
