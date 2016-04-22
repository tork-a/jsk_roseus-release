Name:           ros-indigo-roseus-tutorials
Version:        1.5.1
Release:        0%{?dist}
Summary:        ROS roseus_tutorials package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/roseus_tutorials
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-ar-track-alvar
Requires:       ros-indigo-checkerboard-detector
Requires:       ros-indigo-image-proc
Requires:       ros-indigo-image-view2
Requires:       ros-indigo-opencv-apps
Requires:       ros-indigo-posedetection-msgs
Requires:       ros-indigo-pr2eus
Requires:       ros-indigo-uvc-camera
Requires:       ros-indigo-visualization-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-roseus

%description
roseus_tutorials

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
* Fri Apr 22 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.5.1-0
- Autogenerated by Bloom

* Mon Mar 21 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.5.0-0
- Autogenerated by Bloom

* Wed Nov 25 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.4.1-0
- Autogenerated by Bloom

* Tue Nov 03 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.4.0-0
- Autogenerated by Bloom

* Tue Sep 15 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.3.9-0
- Autogenerated by Bloom

* Sat Sep 12 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.3.8-0
- Autogenerated by Bloom

* Tue Aug 18 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.3.7-0
- Autogenerated by Bloom

* Fri Jun 19 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.3.6-0
- Autogenerated by Bloom

* Fri May 15 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.3.5-0
- Autogenerated by Bloom

* Sun May 03 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.3.4-0
- Autogenerated by Bloom

* Wed Apr 29 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.3.3-0
- Autogenerated by Bloom

* Tue Apr 28 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.3.2-0
- Autogenerated by Bloom

* Sun Apr 26 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.3.1-0
- Autogenerated by Bloom

* Fri Apr 24 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.3.0-0
- Autogenerated by Bloom

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

* Mon Jan 26 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.32-0
- Autogenerated by Bloom

* Fri Jan 23 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.31-0
- Autogenerated by Bloom

