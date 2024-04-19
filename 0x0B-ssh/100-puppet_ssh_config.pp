#!/usr/bin/env bash
# connect to a server without typing a password


file { '/etc/ssh/ssh_config':
	ensure => present,
content => "
	#SSH config
	Host *
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
	",
}
