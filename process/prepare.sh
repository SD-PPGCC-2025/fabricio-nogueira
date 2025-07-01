#!/bin/bash

function generate_env() {
  # Reads docker-compose service definitions. Loads all env declarations and
  # by the sample, creates the respective .env file.
  cat docker-compose.yaml | grep env_file | while read -r line ; do
      envfile=$(echo $line | sed -e 's/env_file: //g')

      if [ ! -f $envfile ]; then
        cp "$envfile.sample" $envfile
      fi
  done
}

# Executions
generate_env