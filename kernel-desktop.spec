#
# Spec file generated by kdist version v0.0.4-48-g9280
#
Name:          kernel-desktop
Summary:       The Linux Kernel for Mandriva systems
License:       GPLv2
Version:       3.1.0
Release:       %mkrel 1.1
URL:           http://www.kernel.org
Source:        kernel-desktop-3.1.0-1.tar.bz2
ExclusiveArch: %ix86 x86_64 
BuildRoot:     %{_tmppath}/%{name}-%{version}-root
AutoReqProv:   no

%global __debug_package 1
%define debug_package %{nil}
%define __check_files %{nil}

%ifarch %ix86 x86_64
%define asmarch x86
%define bzImage arch/x86/boot/bzImage
%define instkern_opts %{nil}
%endif

%ifarch %arm
%define asmarch arm
%define bzImage arch/arm/boot/zImage
%define instkern_opts -i -N
%endif

Summary:       The Linux Kernel for Mandriva systems
Provides:      kernel = 3.1.0.1.1
Provides:      kernel-desktop = 3.1.0.1.1
Group:         System/Kernel and hardware

%description
The Linux Kernel, the operating system core itself

%package devel
Summary:       The minimal Linux Kernel for building kernel modules
Provides:      kernel-devel = 3.1.0.1.1
Provides:      kernel-desktop-devel = 3.1.0.1.1
Group:         Development/Kernel
BuildRequires: rsync

%description -n kernel-desktop-devel
This package provides kernel headers, makefiles and a couple
of others files sufficient to build external kernel modules.

%package debuginfo
Summary:       The debug information for kernel-desktop
Provides:      kernel-debuginfo = 3.1.0.1.1
Provides:      kernel-desktop-debuginfo = 3.1.0.1.1
Group:         Development/Debug

%description -n kernel-desktop-debuginfo
This package provides the kernel's debug information required
by some binary object tools like kgdb, perf, etc...

%prep
%setup -q -n kernel-desktop-3.1.0-1

%build
make defconfig
make -s kernelrelease
test $(make -s kernelrelease) = 3.1.0-1.1-desktop
make %{?_smp_mflags}

%install
make -s INSTALL_MOD_PATH=%{buildroot} modules_install
find %{buildroot} -name \*.ko -exec chmod u+x {} \;

mkdir -p %{buildroot}/boot
cp %{bzImage} %{buildroot}/boot/vmlinuz-3.1.0-1.1-desktop
cp System.map %{buildroot}/boot/System.map-3.1.0-1.1-desktop
cp .config    %{buildroot}/boot/config-3.1.0-1.1-desktop
ln -snf /usr/src/devel/3.1.0-1.1-desktop %{buildroot}/lib/modules/3.1.0-1.1-desktop/build
ln -snf build %{buildroot}/lib/modules/3.1.0-1.1-desktop/source

mkdir -p %{buildroot}/usr/src/devel/3.1.0-1.1-desktop
cat develfiles-%asmarch.list >>develfiles.list
rsync -ar --files-from=develfiles.list . %{buildroot}/usr/src/devel/3.1.0-1.1-desktop

%post -n kernel-desktop
/sbin/installkernel %{instkern_opts} 3.1.0-1.1-desktop

%preun -n kernel-desktop
/sbin/installkernel -R 3.1.0-1.1-desktop

%postun -n kernel-desktop
/sbin/kernel_remove_initrd 3.1.0-1.1-desktop

%clean
rm -rf %{buildroot}

%files -n kernel-desktop
%defattr (-, root, root)
%dir /lib/modules
/lib/modules/3.1.0-1.1-desktop
/boot

%files -n kernel-desktop-devel
%defattr (-, root, root)
/usr/src/devel/3.1.0-1.1-desktop

%files -n kernel-desktop-debuginfo -f debugfiles.list
%defattr (-, root, root)

%changelog
* Wed Oct 26 2011 Franck Bui <franck.bui@mandriva.com> 3.1.0-1.1-desktop
  + Mandriva Release v3.1-1
  + usb: ehci: make HC see up-to-date qh/qtd descriptor ASAP
  + btrfs: btrfs_calc_avail_data_space cope with no read/write devices V2
  + gpu drm mach64 2.6.39 buildfix
  + vfs: introduce clone_private_mount()
  + vfs: export do_splice_direct() to modules
  + vfs: add i_op->open()
  + fb: avoid possible deadlock caused by fb_set_suspend
  + Mandriva Linux boot logo.
  + media video pwc no ads in dmesg
  + media video pwc lie in proc usb devices
  + usb storage unusual_devs add id 2.6.37 buildfix
  + Change to usb storage of unusual_dev.
  + Add blacklist of usb hid modules
  + bluetooth hci_usb disable isoc transfers
  + sound alsa hda ad1884a hp dc model
  + Support a Bluetooth SCO.
  + include kbuild export pci_ids
  + platform x86 add shuttle wmi driver
  + net netfilter psd 2.6.35 buildfix
  + ipt_psd: Mandriva changes
  + net netfilter psd
  + net netfilter IFWLOG 2.6.37 buildfix
  + net netfilter IFWLOG 2.6.35 buildfix
  + net netfilter IFWLOG mdv
  + net netfilter IFWLOG
  + net sis190 fix list usage
  + kbuild compress kernel modules on installation
  + gpu drm mach64 2.6.37 buildfix
  + gpu drm mach64 2.6.36 buildfix
  + gpu drm mach64 fix for changed drm_ioctl
  + gpu drm mach64 fix for changed drm_pci_alloc
  + Adapt mach64 to build with 2.6.31 series kernels
  + gpu drm mach64 fixes
  + gpu drm mach64
  + agp/intel: add new host bridge id for Q57 system
  + mpt scsi modules for VMWare's emulated
  + ide pci sis5513 965
  + ppscsi: build fix for 2.6.39
  + scsi megaraid new sysfs name
  + scsi ppscsi mdvbz45393
  + scsi ppscsi update for scsi_data_buffer
  + scsi ppscsi sg helper update
  + scsi ppscsi_fixes
  + scsi ppscsi-2.6.2
  + acpi video add blacklist to use vendor driver
  + acpi processor M720SR limit to C2
  + CLEVO M360S acpi irq workaround
  + acpi add proc event regs
  + acpi dsdt initrd v0.9c fixes
  + acpi dsdt initrd v0.9c 2.6.28
  + UBUNTU: SAUCE: isapnp_init: make isa PNP scans occur async
  + pnp pnpbios off by default
  + pci add ALI M5229 ide compatibility mode quirk
  + Card bus's PCI last bus
  + x86, cpufreq: set reasonable default for scaling_min_freq with p4-clockmod
  + x86 cpufreq speedstep dothan 3
  + default to "power_off" when SMP kernel is used on single processo
  + x86 boot video 80x25 if break
  + x86 pci toshiba equium a60 assign busses
  + kdist: make the config name part of the localversion
  + kdist: give a name to the config file
