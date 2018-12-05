FROM codeschool/projects-cli:${PROJECTS_CLI_BUILD_TAG:-latest} as projects-cli
FROM python:3.6-alpine

RUN apk add --no-cache libpng freetype libstdc++ python py-pip bash shadow nodejs git
RUN apk add --no-cache --virtual .build-deps \
        gcc \
        build-base \
        python-dev \
        libpng-dev \
        musl-dev \
        freetype-dev

SHELL ["/bin/bash", "-c"]
WORKDIR /opt/
COPY requirements.txt .

RUN ["pip", "install", "-r", "requirements.txt"]

# Create a psprojects user to default the running container to
RUN \
  useradd -b /opt -c "psprojects" -M psprojects && \
  chown -R psprojects:psprojects /opt && \
  mkdir -p /home/psprojects && \
  chown -R psprojects:psprojects /home/psprojects

ENV HOME=/home/psprojects

USER psprojects
RUN ["touch", "/home/psprojects/.bashrc"]

# copy the projects-cli from it's container image.
COPY --from=projects-cli /opt/projects-cli /opt/projects-cli

