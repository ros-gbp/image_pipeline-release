%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-camera-calibration
Version:        1.15.3
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS camera_calibration package

License:        BSD
URL:            http://www.ros.org/wiki/camera_calibration
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-noetic-cv-bridge
Requires:       ros-noetic-image-geometry
Requires:       ros-noetic-message-filters
Requires:       ros-noetic-rospy
Requires:       ros-noetic-sensor-msgs
Requires:       ros-noetic-std-srvs
BuildRequires:  ros-noetic-catkin >= 0.5.68
BuildRequires:  ros-noetic-rostest
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
camera_calibration allows easy calibration of monocular or stereo cameras using
a checkerboard calibration target.

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Fri Dec 11 2020 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.15.3-1
- Autogenerated by Bloom

* Tue May 19 2020 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.15.2-1
- Autogenerated by Bloom

* Mon May 18 2020 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.15.1-1
- Autogenerated by Bloom

* Thu May 14 2020 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.15.0-1
- Autogenerated by Bloom

