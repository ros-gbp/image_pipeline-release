Name:           ros-lunar-image-rotate
Version:        1.12.20
Release:        0%{?dist}
Summary:        ROS image_rotate package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/image_rotate
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-lunar-cv-bridge
Requires:       ros-lunar-dynamic-reconfigure
Requires:       ros-lunar-image-transport
Requires:       ros-lunar-nodelet
Requires:       ros-lunar-roscpp
Requires:       ros-lunar-tf2
Requires:       ros-lunar-tf2-geometry-msgs
Requires:       ros-lunar-tf2-ros
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-cmake-modules
BuildRequires:  ros-lunar-cv-bridge
BuildRequires:  ros-lunar-dynamic-reconfigure
BuildRequires:  ros-lunar-geometry-msgs
BuildRequires:  ros-lunar-image-transport
BuildRequires:  ros-lunar-nodelet
BuildRequires:  ros-lunar-roscpp
BuildRequires:  ros-lunar-rostest
BuildRequires:  ros-lunar-tf2
BuildRequires:  ros-lunar-tf2-geometry-msgs
BuildRequires:  ros-lunar-tf2-ros

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
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Sun Apr 30 2017 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.12.20-0
- Autogenerated by Bloom

* Fri Apr 21 2017 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.12.19-0
- Autogenerated by Bloom

