from conans import ConanFile, tools, os

class BoostMsmConan(ConanFile):
    name = "Boost.Msm"
    version = "1.64.0"
    short_paths = True
    url = "https://github.com/bincrafters/conan-boost-msm"
    description = "Please visit http://www.boost.org/doc/libs/1_64_0/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_names = ["msm"]
    requires =  "Boost.Any/1.64.0@bincrafters/testing", \
                      "Boost.Assert/1.64.0@bincrafters/testing", \
                      "Boost.Bind/1.64.0@bincrafters/testing", \
                      "Boost.Circular_Buffer/1.64.0@bincrafters/testing", \
                      "Boost.Config/1.64.0@bincrafters/testing", \
                      "Boost.Core/1.64.0@bincrafters/testing", \
                      "Boost.Function/1.64.0@bincrafters/testing", \
                      "Boost.Fusion/1.64.0@bincrafters/testing", \
                      "Boost.Mpl/1.64.0@bincrafters/testing", \
                      "Boost.Parameter/1.64.0@bincrafters/testing", \
                      "Boost.Phoenix/1.64.0@bincrafters/testing", \
                      "Boost.Preprocessor/1.64.0@bincrafters/testing", \
                      "Boost.Proto/1.64.0@bincrafters/testing", \
                      "Boost.Serialization/1.64.0@bincrafters/testing", \
                      "Boost.Tuple/1.64.0@bincrafters/testing", \
                      "Boost.Type_Traits/1.64.0@bincrafters/testing", \
                      "Boost.Typeof/1.64.0@bincrafters/testing"

                      #any6 assert1 bind3 circular_buffer8 config0 core2 function5 fusion5 mpl5 parameter10 phoenix9 preprocessor0 proto8 serialization11 tuple4 type_traits3 typeof5
                      
    def source(self):
        boostorg_github = "https://github.com/boostorg"
        archive_name = "boost-" + self.version  
        for lib_short_name in self.lib_short_names:
            tools.get("{0}/{1}/archive/{2}.tar.gz"
                .format(boostorg_github, lib_short_name, archive_name))
            os.rename(lib_short_name + "-" + archive_name, lib_short_name)

    def package(self):
        for lib_short_name in self.lib_short_names:
            include_dir = os.path.join(lib_short_name, "include")
            self.copy(pattern="*", dst="include", src=include_dir)		

    def package_id(self):
        self.info.header_only()