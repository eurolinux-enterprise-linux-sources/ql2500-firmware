Name:		ql2500-firmware
Summary: 	Firmware for qlogic 2500 devices
Version:	5.06.05
Release:	1%{?dist}
License:	Redistributable, no modification permitted
Group:		System Environment/Kernel
Source0:	ftp://ftp.qlogic.com/outgoing/linux/firmware/ql2500_fw.bin
Source1:	ftp://ftp.qlogic.com/outgoing/linux/firmware/LICENSE
URL:		ftp://ftp.qlogic.com/outgoing/linux/firmware/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

%description
Firmware for qlogic 2500 devices.

%prep
%setup -n %{name} -c -T
cp %{SOURCE0} .
cp %{SOURCE1} .

%build
# Firmware, do nothing.

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/lib/firmware/
install -m0644 ql2500_fw.bin %{buildroot}/lib/firmware/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE
/lib/firmware/ql2500_fw.bin

%changelog
* Thu Feb 16 2012 Tom Callaway <spot@fedoraproject.org> - 5.06.05-1
- update to 5.06.05

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.06.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 18 2011 Tom Callaway <spot@fedoraproject.org> - 5.06.02-1
- update to 5.06.02

* Wed Sep  7 2011 Tom Callaway <spot@fedoraproject.org> - 5.06.01-1
- update to 5.06.01

* Wed Aug  3 2011 Tom Callaway <spot@fedoraproject.org> - 5.06.00-1
- update to 5.06.00

* Mon Mar  7 2011 Tom Callaway <spot@fedoraproject.org> - 5.03.16-1
- update to 5.03.16

* Mon Mar  7 2011 Tom Callaway <spot@fedoraproject.org> - 5.03.15-1
- update to 5.03.15

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.03.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 23 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 5.03.13-1
- update to 5.03.13

* Mon Jun 28 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 5.03.07-1
- update to 5.03.07

* Tue Mar 23 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 5.03.02-1
- update to 5.03.02

* Fri Jan 29 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 5.03.01-1
- update to 5.03.01 (MID capable, mid firmware no longer needed/provided)

* Wed Aug 19 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 4.04.09-1
- update to 4.04.09

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.04.05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.04.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Nov 20 2008 Tom "spot" Callaway <tcallawa@redhat.com> 4.04.05-1
- update to 4.04.05

* Fri Aug 22 2008 Tom "spot" Callaway <tcallawa@redhat.com> 4.04.04-1
- Initial package for Fedora
