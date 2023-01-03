#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x330239C1C4DAFEE1 (classic@zzzcomputing.com)
#
Name     : pypi-sqlalchemy
Version  : 1.4.46
Release  : 163
URL      : https://files.pythonhosted.org/packages/af/ae/8d8e67f2691f0fdb845df90013d68c12a9127e009b4dedc34a3228f4e5ad/SQLAlchemy-1.4.46.tar.gz
Source0  : https://files.pythonhosted.org/packages/af/ae/8d8e67f2691f0fdb845df90013d68c12a9127e009b4dedc34a3228f4e5ad/SQLAlchemy-1.4.46.tar.gz
Source1  : https://files.pythonhosted.org/packages/af/ae/8d8e67f2691f0fdb845df90013d68c12a9127e009b4dedc34a3228f4e5ad/SQLAlchemy-1.4.46.tar.gz.asc
Summary  : Database Abstraction Library
Group    : Development/Tools
License  : MIT
Requires: pypi-sqlalchemy-filemap = %{version}-%{release}
Requires: pypi-sqlalchemy-lib = %{version}-%{release}
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

%package filemap
Summary: filemap components for the pypi-sqlalchemy package.
Group: Default

%description filemap
filemap components for the pypi-sqlalchemy package.


%package lib
Summary: lib components for the pypi-sqlalchemy package.
Group: Libraries
Requires: pypi-sqlalchemy-filemap = %{version}-%{release}

%description lib
lib components for the pypi-sqlalchemy package.


%package python
Summary: python components for the pypi-sqlalchemy package.
Group: Default
Requires: pypi-sqlalchemy-python3 = %{version}-%{release}

%description python
python components for the pypi-sqlalchemy package.


%package python3
Summary: python3 components for the pypi-sqlalchemy package.
Group: Default
Requires: pypi-sqlalchemy-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(sqlalchemy)
Requires: pypi(greenlet)

%description python3
python3 components for the pypi-sqlalchemy package.


%prep
%setup -q -n SQLAlchemy-1.4.46
cd %{_builddir}/SQLAlchemy-1.4.46
pushd ..
cp -a SQLAlchemy-1.4.46 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672785974
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-sqlalchemy

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
