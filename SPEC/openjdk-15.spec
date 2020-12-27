Name:           openjdk-15
%define build_timestamp %(date +"%Y%m%d_%H%M")
Version:        %{build_timestamp}
Release:        1
Summary:        OpenJDK

License:        GPL
URL:            https://java.net
%undefine _disable_source_fetch
Source0:        https://download.java.net/java/GA/jdk15.0.1/51f4f36ad4ef43e39d0dfdbaf6549e32/9/GPL/openjdk-15.0.1_linux-x64_bin.tar.gz

#BuildRequires:  
#Requires:       

%description
OpenJDK

%prep
mkdir -p %{_builddir}/openjdk-15
tar -zxvf %SOURCE0  -C %{_builddir}/openjdk-15


%build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/opt/openjdk-15
cp -ivr %{_builddir}/openjdk-15/*/* %{buildroot}/opt/openjdk-15

%files
/opt/openjdk-15/*
