# syntax=docker/dockerfile:1.4

# build stage
FROM  --platform=$BUILDPLATFORM python:3.11 AS builder
ARG DEBIAN_FRONTEND=noninteractive

# Create a system group named "user" with the -r flag
RUN groupadd -r user

# Create a system user named "user" and add it to the "user" group with the -r and -g flags
RUN useradd -r -g user user

RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y
RUN apt-get install -y --no-install-recommends \
    git \
    nano \
    make \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory to /project
WORKDIR /project

# Change the ownership of the working directory to the non-root user "user"
RUN chown -R user:user /project

# Switch to the non-root user "user"
USER user

# install PDM
RUN pip install -U pip setuptools wheel
RUN pip install pdm

# copy files
COPY pyproject.toml pdm.lock README.md /project/
COPY src/ /project/src

# install dependencies and project into the local packages directory
WORKDIR /project
RUN --mount=type=cache,target=/root/.cache/pip \
    mkdir __pypackages__ && pdm sync --prod --no-editable


# dev container
FROM builder as dev-envs

RUN <<EOF
apk update
apk add git
EOF

RUN <<EOF
addgroup -S docker
adduser -S --shell /bin/bash --ingroup docker user vscode
EOF

# install Docker tools (cli, buildx, compose)
COPY --from=gloursdocker/docker / /

CMD ["python3", "-m", "project.app"]


# run stage
FROM python:3.11 AS runner

# retrieve packages from build stage
ENV PYTHONPATH=/project/pkgs
COPY --from=builder /project/__pypackages__/3.11/lib /project/pkgs

# retrieve executables
COPY --from=builder /project/__pypackages__/3.11/bin/* /bin/

# set command/entrypoint, adapt to fit your needs
CMD ["python3", "-m", "project.app"]
