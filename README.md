Docker-Cloud API "cron" service. Configure cron-like job specifications for Docker-Cloud API events. — Edit

# Usage

Construct cron-like job specifications based on [Docker Cloud Events][], in this form:

    Type Action State User Command

E.g.

    stack update Success root jq .
    service update Success root echo "${@}"
    node,nodecluser create,update root jq -r .datetime


The command is piped the JSON event body on STDIN, also each field passed as $1.. positional parameters in this order:

1. Type
2. Action
3. Resource URI
4. State
5. UUID
6. Datetime
7. ... Parents

E.g.

    service update Success root echo Type=$1 Action=$2 Resource URI=$3 State=$4 UUID=$5 Datetime=$6 Parents=\(${@:7}\)

A `*` wild-card matches any value.

    * * Success root echo Type=$1 Action=$2 Resource URI=$3 State=$4 UUID=$5 Datetime=$6 Parents=\(${@:7}\)

[Docker Cloud Events]: https://docs.docker.com/apidocs/docker-cloud/?python#docker-cloud-event
