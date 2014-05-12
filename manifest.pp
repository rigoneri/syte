class python {
    package { 'python':
        ensure => 'present',
    }

    package { 'python-pip':
        ensure => 'present',
    }

    exec { 'requirements':
        command => '/usr/local/bin/pip install -r /vagrant/requirements.txt',
    }

    Package['python'] -> Package['python-pip'] -> Exec['requirements']
}

include python