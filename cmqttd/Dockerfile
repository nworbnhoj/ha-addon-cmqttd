ARG BUILD_FROM
FROM ${BUILD_FROM}

ARG CMQTTD_COMMIT=cc0bdf3

SHELL ["/bin/bash","-o","pipefail","-c"]

RUN apt-get update &&     apt-get install -y --no-install-recommends       git build-essential cmake pkg-config       python3 python3-pip python3-venv       libssl-dev libmosquitto-dev libyaml-cpp-dev       ca-certificates &&     rm -rf /var/lib/apt/lists/*

WORKDIR /opt

RUN curl -L \
    https://github.com/micolous/cbus/archive/${CMQTTD_COMMIT}.tar.gz \
    | tar -xz

# Phase 4 builds and installs cmqttd.

COPY rootfs/ /

CMD ["/bin/bash"]
