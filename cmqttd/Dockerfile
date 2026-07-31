ARG BUILD_FROM
FROM ${BUILD_FROM}
RUN apt-get update && apt-get install -y python3 python3-yaml git ca-certificates && rm -rf /var/lib/apt/lists/*
CMD ["/bin/bash"]
