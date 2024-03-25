# puppet script to configure server
file_line { 'Turn off password auth':
    ensure => 'present',
    path   => '/etc/ssh/ssh_config',
    line   => 'PasswordAuthentication no',
}
file_line { 'identity file':
    ensure => 'present',
    path   => '/etc/ssh/ssh_config',
    line   => 'IdentityFile ~/.ssh/school',
}
