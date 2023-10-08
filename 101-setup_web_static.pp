# by itry mo9atil
# Setup the web servers for the deployment of web_static
class web_static_setup {
  $directories = ['/data', '/data/web_static', '/data/web_static/releases', '/data/web_static/releases/test', '/data/web_static/shared']
  $nginx_package_name = 'nginx'
  $fake_html_content = '<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>'

  exec { '/usr/bin/env apt -y update' : }
  -> package { $nginx_package_name: ensure => installed, }

  file { $directories:
    ensure => directory,
    owner  => 'ubuntu',
    group  => 'ubuntu',
    mode   => '0755',
    recurse => true,
  }

  file { '/data/web_static/releases/test/index.html':
    ensure  => file,
    content => $fake_html_content,
    require => File[$directories],
  }

  file { '/data/web_static/current':
    ensure => link,
    target => '/data/web_static/releases/test',
    force  => true,
    require => File['/data/web_static/releases/test/index.html'],
  }

  exec { 'chown -R ubuntu:ubuntu /data/':
    path => '/usr/bin/:/usr/local/bin/:/bin/',
    require => File['/data/web_static/current'],
  }

  file_line { 'nginx_config':
    path   => '/etc/nginx/sites-available/default',
    line   => '        location /hbnb_static {\n            alias /data/web_static/current/;\n        }',
    match  => '^        location /hbnb_static',
    after  => '^    server {',
    require => Package[$nginx_package_name],
    notify  => Service[$nginx_package_name],
  }

  service { $nginx_package_name:
    ensure     => running,
    enable     => true,
    hasrestart => true,
    hasstatus  => true,
    subscribe  => File_line['nginx_config'],
  }
}
