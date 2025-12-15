%define module cached_property

Name:		python-cached-property
Version:	2.0.1
Release:	1
Summary:	A decorator for caching properties in classes
Group:		Development/Python
License:	BSD-2-Clause
URL:		https://pypi.org/project/cached-property
Source0:	https://files.pythonhosted.org/packages/source/c/%{module}/%{module}-%version.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildArch:		noarch

BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
A decorator for caching properties in classes.

%prep
%autosetup -n %{module}-%{version} -p1
# Remove bundled egg-info
rm -rf %{module}.egg-info

%build
%py_build

%install
%py_install

%files
%doc README.md
%license LICENSE
%{python_sitelib}/%{module}.py
%{python_sitelib}/%{module}-%{version}*.*-info
