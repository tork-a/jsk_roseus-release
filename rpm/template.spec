Name:           ros-hydro-roseus-smach
Version:        1.2.7
Release:        0%{?dist}
Summary:        ROS roseus_smach package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/roseus_smach
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-euslisp
Requires:       ros-hydro-roseus
Requires:       ros-hydro-smach
Requires:       ros-hydro-smach-msgs
Requires:       ros-hydro-smach-ros
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-euslisp
BuildRequires:  ros-hydro-roseus
BuildRequires:  ros-hydro-smach
BuildRequires:  ros-hydro-smach-msgs
BuildRequires:  ros-hydro-smach-ros

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
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Sun Feb 22 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.7-0
- Autogenerated by Bloom

* Sat Feb 21 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.6-0
- Autogenerated by Bloom

* Fri Feb 13 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.5-0
- Autogenerated by Bloom

* Thu Feb 12 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.4-0
- Autogenerated by Bloom

* Mon Feb 02 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.3-0
- Autogenerated by Bloom

* Tue Jan 27 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.2-0
- Autogenerated by Bloom

* Tue Jan 27 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.1-0
- Autogenerated by Bloom

* Mon Jan 26 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.0-0
- Autogenerated by Bloom

* Mon Jan 26 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.33-0
- Autogenerated by Bloom

* Mon Jan 26 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.32-0
- Autogenerated by Bloom

* Fri Jan 23 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.31-0
- Autogenerated by Bloom

* Wed Jan 14 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.30-0
- Autogenerated by Bloom

* Sat Dec 27 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.29-0
- Autogenerated by Bloom

* Mon Nov 10 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.26-0
- Autogenerated by Bloom

* Sat Oct 11 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.25-0
- Autogenerated by Bloom

* Wed Sep 24 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.24-0
- Autogenerated by Bloom

* Fri Sep 05 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.22-0
- Autogenerated by Bloom

