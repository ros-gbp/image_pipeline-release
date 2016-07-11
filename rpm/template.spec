Name:           ros-indigo-image-rotate
Version:        1.12.17
Release:        0%{?dist}
Summary:        ROS image_rotate package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/image_rotate
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-cv-bridge
Requires:       ros-indigo-dynamic-reconfigure
Requires:       ros-indigo-image-transport
Requires:       ros-indigo-nodelet
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-tf2
Requires:       ros-indigo-tf2-geometry-msgs
Requires:       ros-indigo-tf2-ros
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cmake-modules
BuildRequires:  ros-indigo-cv-bridge
BuildRequires:  ros-indigo-dynamic-reconfigure
BuildRequires:  ros-indigo-eigen-conversions
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-image-transport
BuildRequires:  ros-indigo-nodelet
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-rostest
BuildRequires:  ros-indigo-tf2
BuildRequires:  ros-indigo-tf2-geometry-msgs
BuildRequires:  ros-indigo-tf2-ros

%description
Contains a node that rotates an image stream in a way that minimizes the angle
between a vector in some arbitrary frame and a vector in the camera frame. The
frame of the outgoing image is published by the node. This node is intended to
allow camera images to be visualized in an orientation that is more intuitive
than the hardware-constrained orientation of the physical camera. This is
particularly helpful, for example, to show images from the PR2's forearm cameras
with a consistent up direction, despite the fact that the forearms need to
rotate in arbitrary ways during manipulation. It is not recommended to use the
output from this node for further computation, as it interpolates the source
image, introduces black borders, and does not output a camera_info.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Jul 11 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.12.17-0
- Autogenerated by Bloom

* Sat Mar 19 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.12.16-0
- Autogenerated by Bloom

* Sun Jan 17 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.12.15-0
- Autogenerated by Bloom

* Wed Jul 22 2015 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.12.14-0
- Autogenerated by Bloom

* Mon Apr 06 2015 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.12.13-0
- Autogenerated by Bloom

* Wed Dec 31 2014 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.12.12-0
- Autogenerated by Bloom

