%global pypi_name cached-property

Name:           python-%{pypi_name}
Version:        1.5.1
Release:        %mkrel 1
Summary:        A decorator for caching properties in classes

License:        MIT
URL:            https://pypi.org/project/cached-property
Source0:        http://pypi.python.org/packages/source/c/%{pypi_name}/%{pypi_name}-%version.tar.gz
BuildArch:      noarch
Group:          Development/Python

BuildRequires:  pkgconfig(python3)
BuildRequires:  python-setuptools

%description
A decorator for caching properties in classes

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python-%{pypi_name}
%doc README.rst AUTHORS.rst CONTRIBUTING.rst HISTORY.rst LICENSE
%{python3_sitelib}/cached_property*
%{python3_sitelib}/cached_property-%{version}-py?.?.egg-info/*
%{python3_sitelib}/__pycache__/cached_property*
