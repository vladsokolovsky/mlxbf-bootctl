Name: mlxbf-bootctl
Version: 1.0
%{!?_release: %define _release 2}
Release: %{_release}%{?dist}
Summary: Mellanox BlueField boot partition management utility

License: GPLv2 or BSD
Url: https://mellanox.com
Source: %{name}-%{version}.tgz

BuildRequires: binutils
BuildRequires: gcc

%description
Access to all the boot partition management is via a program shipped
with the BlueField software called "mlxbf-bootctl".

%prep
%setup

%build
%make_build

%install
%make_install

%files
%defattr(-, root, root)
/sbin/*
%doc README.md COPYING
