#!/usr/bin/env sh

set -o errexit
set -o nounset

cmd="$*"

# We need this line to make sure that this container is started
# after the one with MySQL:
while ! mysqladmin ping -h"$DJANGO_DATABASE_HOST" --silent; do
    sleep 1
done

# It is also possible to wait for other services as well: redis, elastic, mongo
>&2 echo 'MySQL is up - continuing...'

# Collect Static
echo "Apply Collectstatic"
python manage.py collectstatic --no-input

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Evaluating passed command (do not touch):
# shellcheck disable=SC2086
exec $cmd
