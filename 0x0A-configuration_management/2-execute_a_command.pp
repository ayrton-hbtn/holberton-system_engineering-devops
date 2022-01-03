# Kills a process called killmenow
exec { 'killmenow':
    path    => '/bin',
    onlyif  => 'pkill killmenow',
    command => 'killmenow',
}
