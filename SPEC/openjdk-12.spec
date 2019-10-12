Name:           openjdk-12
Version:        12
%define build_timestamp %(date +"%Y%m%d_%H%M")
Release:        %{build_timestamp}
Summary:        OpenJDK

License:        GPL
URL:            https://java.net
%undefine _disable_source_fetch
Source0:        https://download.java.net/java/GA/jdk12/33/GPL/openjdk-12_linux-x64_bin.tar.gz

#BuildRequires:  
#Requires:       

%description
OpenJDK

%prep
mkdir -p %{_builddir}/openjdk-12
tar -zxvf %SOURCE0  -C %{_builddir}/openjdk-12


%build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/opt/openjdk-12
cp -ivr %{_builddir}/openjdk-12/*/* %{buildroot}/opt/openjdk-12

%files
/opt/openjdk-12/*

