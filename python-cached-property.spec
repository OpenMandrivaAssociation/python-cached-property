%global pypi_name cached-property

Name:		python-%{pypi_name}
Version:	1.5.1
Release:	3
Summary:	A decorator for caching properties in classes
Group:		Development/Python
License:	MIT
URL:		https://pypi.org/project/cached-property
Source0:	http://pypi.python.org/packages/source/c/%{pypi_name}/%{pypi_name}-%version.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python-setuptools

%description
A decorator for caching properties in classes.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python-%{pypi_name}
%doc README.rst AUTHORS.rst CONTRIBUTING.rst HISTORY.rst LICENSE
%{python_sitelib}/cached_property*
