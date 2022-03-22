FROM envoyproxy/envoy:v1.21-latest

COPY ./envoy.yaml /etc/envoy/envoy.yaml
COPY ./storage.desc /etc/envoy/storage.desc

CMD ["envoy", "-c", "/etc/envoy/envoy.yaml"]
