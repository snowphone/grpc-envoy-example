
# Doesn't work since storage is not synchronized yet.
curl -w '\n'  -H "authentication: Bearer secret-token" -X POST -d '{"key": "hello", "value": "world"}' localhost/v1/storage
curl -w '\n'  -H "authentication: Bearer secret-token" -X POST  'localhost/v1/storage?key=hi&value=bixby'
curl -w '\n'  -H "authentication: Bearer secret-token" localhost/v1/storage/hello

curl -w '\n'  -H "authentication: Bearer secret-token" localhost/v1/storage/hi

curl -w '\n' -i -H "authentication: Bearer secret-token" "localhost/v1/storage/I_presume_it_won't_exist"
