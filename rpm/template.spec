Name:           ros-kinetic-roseus-smach
Version:        1.6.0
Release:        1%{?dist}
Summary:        ROS roseus_smach package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/roseus_smach
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-actionlib
Requires:       ros-kinetic-actionlib-tutorials
Requires:       ros-kinetic-euslisp
Requires:       ros-kinetic-message-runtime
Requires:       ros-kinetic-roseus
Requires:       ros-kinetic-rostest
Requires:       ros-kinetic-smach
Requires:       ros-kinetic-smach-msgs
Requires:       ros-kinetic-smach-ros
Requires:       ros-kinetic-std-msgs
BuildRequires:  ros-kinetic-actionlib
BuildRequires:  ros-kinetic-actionlib-tutorials
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-message-generation
BuildRequires:  ros-kinetic-roseus
BuildRequires:  ros-kinetic-rostest
BuildRequires:  ros-kinetic-smach
BuildRequires:  ros-kinetic-smach-msgs
BuildRequires:  ros-kinetic-smach-ros
BuildRequires:  ros-kinetic-std-msgs

%description
roseus_smach * Euslisp state machine class. it will be moved. * Message
publisher for visualizing current state by smach_viewer. * Simple pickle dump
script for debugging state machine. * Execute state machine as a action server.

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
* Sat Mar 11 2017 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.6.0-1
- Autogenerated by Bloom

* Fri Oct 21 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.6.0-0
- Autogenerated by Bloom

