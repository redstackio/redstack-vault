---
id: fa59fc5e-36d5-44e6-ae8f-b44a3f2472a1
name: Display All Authors
type: command
executor: bash
data: "<?php\n\nrequire_once('config.php');\n\n$sql = 'SELECT * FROM authors';\n$result\
  \ = $conn->query($sql);\n\nif ($result->num_rows > 0) {\n    // output data of each\
  \ row\n    while($row = $result->fetch_assoc()) {\n        echo 'Name: ' . $row['name']\
  \ . ' - Email: ' . $row['email'] . '<br>';\n    }\n} else {\n    echo '0 results';\n\
  }\n\n$conn->close();\n?>"
output: null
created_at: '2023-04-06T03:56:40.435655+00:00'
updated_at: '2023-04-10T20:23:38.202907+00:00'
---

# Display All Authors

```bash
<?php

require_once('config.php');

$sql = 'SELECT * FROM authors';
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo 'Name: ' . $row['name'] . ' - Email: ' . $row['email'] . '<br>';
    }
} else {
    echo '0 results';
}

$conn->close();
?>
```
