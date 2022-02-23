# debug php config file with puppet

exec { 'fix error 500':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => '/bin',
}
