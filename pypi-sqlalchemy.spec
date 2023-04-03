#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
# Source0 file verified with key 0x330239C1C4DAFEE1 (classic@zzzcomputing.com)
#
Name     : pypi-sqlalchemy
Version  : 2.0.8
Release  : 173
URL      : https://files.pythonhosted.org/packages/0f/73/b76a2c8dbe035791e54da29cefaa22c166f875b24da844dc0f16b66e47bb/SQLAlchemy-2.0.8.tar.gz
Source0  : https://files.pythonhosted.org/packages/0f/73/b76a2c8dbe035791e54da29cefaa22c166f875b24da844dc0f16b66e47bb/SQLAlchemy-2.0.8.tar.gz
Source1  : https://files.pythonhosted.org/packages/0f/73/b76a2c8dbe035791e54da29cefaa22c166f875b24da844dc0f16b66e47bb/SQLAlchemy-2.0.8.tar.gz.asc
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
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
Requires: pypi(typing_extensions)

%description python3
python3 components for the pypi-sqlalchemy package.


%prep
%setup -q -n SQLAlchemy-2.0.8
cd %{_builddir}/SQLAlchemy-2.0.8
pushd ..
cp -a SQLAlchemy-2.0.8 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1680533672
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-sqlalchemy
cp %{_builddir}/SQLAlchemy-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-sqlalchemy/5ed1f856b86ff607825ad84842cc48b6ad3a2b7f || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-sqlalchemy/5ed1f856b86ff607825ad84842cc48b6ad3a2b7f

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
