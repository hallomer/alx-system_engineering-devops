# Fixes all occurrences of 'phpp' to 'php' in wp-settings.php

exec { 'fix-wordpress':
  command => '/bin/sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  onlyif  => '/bin/grep "phpp" /var/www/html/wp-settings.php',
}
