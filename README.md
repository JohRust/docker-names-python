# docker-names-python
Create random names identical to default docker container names. 

This is a python port of the name generator from the Moby project that is used to create the well-known naming schemes of docker containers:
https://github.com/moby/moby/blob/master/pkg/namesgenerator/names-generator.go

Note that there are no guarantees to avoid naming collisions. Generating very high numbers of random names will lead to dublicates.
Use the retries param to appent

# Installation
Just copy the docker names folder into your project and import it as a module.

# Usage
    >>> import docker_names
    >>> docker_names.get_random_name(retry=0)
    'practical_banach'
    >>> docker_names.get_random_name(retry=1)
    'kind_fermi1'
