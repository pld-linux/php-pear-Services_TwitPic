%include	/usr/lib/rpm/macros.php
%define		_class		Services
%define		_subclass	TwitPic
%define		_status		alpha
%define		_pearname	Services_TwitPic
Summary:	%{_pearname} - PHP Interface to TwitPics API
Summary(pl.UTF-8):	%{_pearname} - interfejs PHP do API TwitPics
Name:		php-pear-%{_pearname}
Version:	0.1.0
Release:	1
License:	BSD Style
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	7c872e6139fca86f1aaa417c32194e46
URL:		http://pear.php.net/package/Services_TwitPic/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-HTTP_Request >= 1.4.3
Requires:	php-pear-PEAR >= 1.4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An interface for uploading pictures to TwitPic and optionally posting
them (along with status messages) to Twitter as well.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Interfejs do wgrywania zdjęć do serwisu TwitPic oraz opcjonalnie
wysyłanie ich (wraz z komunikatem) do serwisu Twitter.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
AutoReq:	no
Requires:	%{name} = %{version}-%{release}
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/Services_TwitPic/docs/example.php
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Services/TwitPic.php
%{php_pear_dir}/Services/TwitPic

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/Services_TwitPic
