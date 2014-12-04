# device is the android codename for the device (the bsp device)
# eg mako = Nexus 4
%define device i9305
# vendor is used in device/%vendor/%device/ (the vendor providing the bsp)
%define vendor samsung

# rpm_device is the name of the ported device
# %%define rpm_device bladerunner
# rpm_vendor is used in the rpm space (the vendor doing the port)
# %%define rpm_vendor nemo

# Manufacturer and device name to be shown in UI
%define vendor_pretty Samsung
%define device_pretty Galaxy SIII LTE

# android_config is the set of #defines needed by libhybris builds to
# be injected into android_config.h
# This could eventually be obtained by parsing the BoardConfig.mk
%define android_config \
#define EXYNOS4_ENHANCEMENTS 1\
%{nil}

%include rpm/dhd/droid-hal-device.inc
