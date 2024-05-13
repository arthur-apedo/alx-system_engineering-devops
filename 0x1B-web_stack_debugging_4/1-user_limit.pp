# fixing the number of allowed files in holberton user
exec { 'fix-file-limit':
  command => 'sed -i"/holberton hard/s/5/10000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/:/sbin/'
}
exec { 'soft-file-limit':
  command => 'sed -i"/holberton soft/s/4/20000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/:/sbin/'
}
