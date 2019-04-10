pipeline {
    agent any
    options {
        disableConcurrentBuilds()
    }

    stages {

        stage("Build Images") {
            // Builds images that are required for tests
            steps {
                dir("__riptide_lib") {
                    git url: 'https://github.com/Parakoopa/riptide-lib.git'
                    sh "docker build -t riptide_docker_tox test_assets/riptide-docker-tox"
                }
            }
        }

        stage("Tests") {
            steps {
                sh '''#!/bin/bash
                    docker run \
                        -v /var/run/docker.sock:/var/run/docker.sock \
                        -e USER=$(id -u) \
                        -e DOCKER_GROUP=$(cut -d: -f3 < <(getent group docker)) \
                        -v "/tmp:/tmp" \
                        -v "$(pwd):$(pwd)" \
                        --network host \
                        --workdir $(pwd) \
                        riptide_docker_tox \
                        tox
                '''
            }
        }

    }

}