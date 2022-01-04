# edit ssh configuration file

file_line {'edit_line_sshh_config':
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => 'PasswordAuthentication no',
    match  => '^#\s{3,}PasswordAuthentication',
}

file_line {'edit_line_sshh_config2':
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => 'IdentityFile ~/.ssh/school',
    match  => '^#\s{3,}IdentityFile ~/.ssh/id_ed25519',
}
