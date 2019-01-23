#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/testing")

class BoostMsmConan(base.BoostBaseConan):
    name = "boost_msm"
    version = "1.67.0"
    url = "https://github.com/bincrafters/conan-boost_msm"
    lib_short_names = ["msm"]
    header_only_libs = ["msm"]
    b2_requires = [
        "boost_any",
        "boost_assert",
        "boost_bind",
        "boost_circular_buffer",
        "boost_config",
        "boost_core",
        "boost_function",
        "boost_fusion",
        "boost_mpl",
        "boost_parameter",
        "boost_phoenix",
        "boost_preprocessor",
        "boost_proto",
        "boost_serialization",
        "boost_tuple",
        "boost_type_traits",
        "boost_typeof"
    ]


