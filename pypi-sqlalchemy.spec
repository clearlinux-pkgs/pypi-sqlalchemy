#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x330239C1C4DAFEE1 (classic@zzzcomputing.com)
#
Name     : pypi-sqlalchemy
Version  : 1.4.32
Release  : 145
URL      : https://files.pythonhosted.org/packages/7a/9f/ace7376a3ab45adf0f7169a5d8d60707c04b171b72a18bb23d505f83f362/SQLAlchemy-1.4.32.tar.gz
Source0  : https://files.pythonhosted.org/packages/7a/9f/ace7376a3ab45adf0f7169a5d8d60707c04b171b72a18bb23d505f83f362/SQLAlchemy-1.4.32.tar.gz
Source1  : https://files.pythonhosted.org/packages/7a/9f/ace7376a3ab45adf0f7169a5d8d60707c04b171b72a18bb23d505f83f362/SQLAlchemy-1.4.32.tar.gz.asc
Summary  : Database Abstraction Library
Group    : Development/Tools
License  : MIT
Requires: pypi-sqlalchemy-license = %{version}-%{release}
Requires: pypi-sqlalchemy-python = %{version}-%{release}
Requires: pypi-sqlalchemy-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
=====================
SQLALCHEMY UNIT TESTS
=====================
Basic Test Running
==================

%package license
Summary: license components for the pypi-sqlalchemy package.
Group: Default

%description license
license components for the pypi-sqlalchemy package.


%package python
Summary: python components for the pypi-sqlalchemy package.
Group: Default
Requires: pypi-sqlalchemy-python3 = %{version}-%{release}

%description python
python components for the pypi-sqlalchemy package.


%package python3
Summary: python3 components for the pypi-sqlalchemy package.
Group: Default
Requires: python3-core
Provides: pypi(sqlalchemy)
Requires: pypi(greenlet)

%description python3
python3 components for the pypi-sqlalchemy package.


%prep
%setup -q -n SQLAlchemy-1.4.32
cd %{_builddir}/SQLAlchemy-1.4.32

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1646665360
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-sqlalchemy
cp %{_builddir}/SQLAlchemy-1.4.32/LICENSE %{buildroot}/usr/share/package-licenses/pypi-sqlalchemy/9425969aa233e93e4e8a48a106b23b1aaa529d83
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-sqlalchemy/9425969aa233e93e4e8a48a106b23b1aaa529d83

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
