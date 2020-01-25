%define		pearname	Text_Diff
Summary:	%{pearname} - Engine for performing and rendering text diffs
Summary(pl.UTF-8):	%{pearname} - Silnik do przetwarzania i generowania różnic pomiędzy tekstami
Name:		php-pear-%{pearname}
Version:	1.2.2
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	2d66f40c8e0c8298281260d33e838b41
URL:		http://pear.php.net/package/Text_Diff/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(core) >= 4.2.0
Requires:	php-pear
Suggests:	php(xdiff)
Obsoletes:	php-pear-Text_Diff-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a text-based diff engine and renderers for
multiple diff output formats.

%description -l pl.UTF-8
Ten pakiet dostarcza silnik do przetwarzania różnic między tekstami
oraz funkcje generujące różnice w wielu formatach wyjściowych.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log
%doc optional-packages.txt
%doc docs/%{pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Text/*.php
%{php_pear_dir}/Text/Diff
