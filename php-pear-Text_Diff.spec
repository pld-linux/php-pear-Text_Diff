%include	/usr/lib/rpm/macros.php
%define         _class          Text
%define         _subclass       Diff
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - Engine for performing and rendering text diffs
Summary(pl):	%{_pearname} - Silnik do przetwarzania i generowania ró¿nic pomiêdzy tekstami
Name:		php-pear-%{_pearname}
Version:	0.0.3
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	e621bff6b173f68c22f66b3871d42ae5
URL:		http://pear.php.net/package/Class_Subclass/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a text-based diff engine and renderers for
multiple diff output formats. 

This class has in PEAR status: %{_status}.

%description -l pl
Ten pakiet dostarcza silnik do przetwarzania ró¿nic miêdzy tekstami
oraz funkcje generuj±ce ró¿nice w wielu formatach wyj¶ciowych.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Renderer

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}
install %{_pearname}-%{version}/%{_subclass}/Renderer/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Renderer

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{docs/*,tests/}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
