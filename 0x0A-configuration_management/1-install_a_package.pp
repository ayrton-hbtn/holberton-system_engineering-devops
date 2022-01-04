# install puppet-lint
exec { 'puppet-lint -v 2.5.0':
    command => '/bin/gem install puppet-lint -v 2.5.0',
}
