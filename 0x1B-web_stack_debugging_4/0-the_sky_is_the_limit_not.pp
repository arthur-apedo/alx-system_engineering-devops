# change the number of requests limit on nginx
exec { 'nginx-req-fix':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
}

exec { 'nginx-restart':
  command   => 'nginx restart',
  path      => '/usr/sbin:/sbin:/usr/bin:/bin',
  subscript => Exec['nginx-req-fix'],
}
