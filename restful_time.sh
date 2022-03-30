
seq 10 | parallel --max-args 0 -j20 curl -H '"authentication: Bearer secret-token"' -w '\\n' -sS localhost/v1/time/now
