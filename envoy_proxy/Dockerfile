FROM envoyproxy/envoy:v1.21-latest

COPY ./envoy.yaml /etc/envoy/envoy.yaml
COPY ./services.desc /etc/envoy/services.desc

CMD ["envoy", "-c", "/etc/envoy/envoy.yaml"]
