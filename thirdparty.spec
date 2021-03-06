%global scl lsst-stack1

%{?scl:%global _scl_prefix /opt/lsst}
%{?scl:%scl_package thirdparty}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}thirdparty
Version:        1
Release:        4%{?dist}
Summary:        LSST Stack thirdparty dependencies
License:        MIT
Url:            https://confluence.lsstcorp.org/display/DM/DM+Third+Party+Software
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  %{?scl_prefix_python}python-devel >= 2.7
%{?scl:BuildRequires: %{scl_prefix}build %{scl_prefix}runtime}
%{?scl:Requires: %{scl_prefix}runtime}

# epel-6 provides activemq-cpp 3.8.2
Requires: activemq-cpp-devel >= 3.5.0
Requires: antlr >= 2.7.7
# el6 provides apr 1.3.9
Requires: apr-devel >= 1.3.3
# el6 provides apr-util 1.3.9
Requires: apr-util >= 1.3.4
# astrometry_net 0.50
# boost 1.51.0
# cfitsio 3360
Requires: %{?scl_prefix}doxygen >= 1.8.5
# epel-6 provides eigen3-devel 3.2.3
Requires: eigen3-devel >= 3.2.0
Requires: expat-devel >= 2.0.1
# fftw 3.3.3
# epel-6 provides freetds 0.91 XXX is this new enough?
Requires: freetds
# gsl 1.16
# healpy 1.7.4
# kazoo 2.0b1
# libevent 2.0.16
Requires: log4cxx-devel >= 0.10.0
Requires: lua-devel >= 5.1.4
Requires: lua-xmlrpc >= 1.2.1
# epel-6 provides lua-expat 1.3.0
Requires: lua-expat >= 1.1
# epel-6 provides lua-socket 3.0
Requires: lua-socket-devel >= 2.0.2
# epel6 provides root-minuit2 5.34.32
#Requires: root-minuit2 >= 5.28.00
# mpich2 XXX listed but does not appear to be in use
# el6 provides 5.1.73
Requires: mysql-devel >= 5.1.72
# epel-6 provides mysql-proxy 0.8.5
Requires: mysql-proxy-devel >= 0.8.2
Requires: python27-MySQL-python >= 1.2.3
# rhscl-python27-epel-6-x86_64 provides python27-numpy 1.7.1
# XXX eups pkg is 1.5.1; wiki says 1.8.0
Requires: python27-numpy >= 1.5.1
# oorb XXX listed by does not appear to be in use
# palpy 1.1
Requires: %{?scl_prefix}protobuf-devel >= 2.4.1
# pyephem 3.7.5.1
# pyfits 3.2.4
Requires: %{?scl_prefix}python-pykg-config >= 1.2.0
# pymssql 2.0.0
# scisql 0.3
Requires: python27-python-sqlalchemy
# sqlite3 3.8.2
# swig 1.3.40
# twisted 12.0.0
# epel-6 provides wcslib 4.3.1
Requires: wcslib-devel >= 4.1.4
# xpa 2.1.15
#Requires: xrootd-devel >= 4.0.3
# zope 3.8.0
# zookeeper 3.4.6

# not listed in wiki
# flask: 0.10.1+9 ok (1.5 sec).

%description
Pulls in thirdparty packages required for building the LSST Stack as
documented at https://confluence.lsstcorp.org/display/DM/DM+Third+Party+Software

%prep
%setup -c -T
%build
%install
%files

%changelog
* Fri Jul 24 2015 Joshua Hoblitt <josh@hoblitt.com> 1-4
- fix python-pykg-config version req (josh@hoblitt.com)

* Fri Jul 24 2015 Joshua Hoblitt <josh@hoblitt.com> 1-3
- fix python-pykg-config package name (josh@hoblitt.com)

* Fri Jul 24 2015 Joshua Hoblitt <josh@hoblitt.com> 1-2
- complete inspection of wiki listed packages (josh@hoblitt.com)

* Fri Jul 24 2015 Joshua Hoblitt <josh@hoblitt.com> 1-1
- new package built with tito

