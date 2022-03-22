
# Doesn't work since storage is not synchronized yet.
#curl -i -X POST 'localhost/v1/storage?key=hello&value=world'
#curl -i 'localhost/v1/storage/hello'
#curl -i "localhost/v1/storage/I_presume_it_won't_exist"

seq 1000 | parallel --max-args 0 -j20 curl -w '\\n' -sS localhost/v1/time
