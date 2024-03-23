# Terminates a process using pkill
exec { 'killmenow_process':
    command     => 'pkill killmenow',
    path        => ['/bin', '/usr/bin', '/sbin', '/usr/sbin'],
    refreshonly => true
}
