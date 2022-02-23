# modify nginx config file to accept more user requests

exec { 'user limit':
  ensure   => file,
  command  => 'sed -i "5s/[0-9]\+/$( ulimit -n )/" /etc/default/nginx; service nginx restart',
}
