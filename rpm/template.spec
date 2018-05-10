Name:           ros-kinetic-stereo-image-proc
Version:        1.12.23
Release:        0%{?dist}
Summary:        ROS stereo_image_proc package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/stereo_image_proc
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-cv-bridge
Requires:       ros-kinetic-dynamic-reconfigure
Requires:       ros-kinetic-image-geometry
Requires:       ros-kinetic-image-proc
Requires:       ros-kinetic-image-transport
Requires:       ros-kinetic-message-filters
Requires:       ros-kinetic-nodelet
Requires:       ros-kinetic-sensor-msgs
Requires:       ros-kinetic-stereo-msgs
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-cv-bridge
BuildRequires:  ros-kinetic-dynamic-reconfigure
BuildRequires:  ros-kinetic-image-geometry
BuildRequires:  ros-kinetic-image-proc
BuildRequires:  ros-kinetic-image-transport
BuildRequires:  ros-kinetic-message-filters
BuildRequires:  ros-kinetic-nodelet
BuildRequires:  ros-kinetic-rostest
BuildRequires:  ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-stereo-msgs

%description
Stereo and single image rectification and disparity processing.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Thu May 10 2018 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.12.23-0
- Autogenerated by Bloom

* Fri Dec 08 2017 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.12.22-0
- Autogenerated by Bloom

* Sun Nov 05 2017 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.12.21-0
- Autogenerated by Bloom

* Sun Apr 30 2017 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.12.20-0
- Autogenerated by Bloom

* Sun Jul 24 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.12.19-0
- Autogenerated by Bloom

* Tue Jul 12 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.12.18-0
- Autogenerated by Bloom

* Mon Jul 11 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.12.17-0
- Autogenerated by Bloom

* Thu Apr 07 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.12.16-0
- Autogenerated by Bloom

