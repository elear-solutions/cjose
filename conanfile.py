from conans import ConanFile, CMake, tools

class CjoselibConan(ConanFile):
    name = "cjose"
    version = "0.1"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Elearcommonlib here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    requires="jansson/0.1@jenkins/master", "openssl/0.1@jenkins/master"
    options = {"shared": [True, False]}
    default_options = "shared=False", "openssl:no_asm=True"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        if (self.settings.os == "Android"):
            cmake.definitions[ "Platform" ] = "android"
        cmake.configure(source_folder=".")
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include/cjose", src="include/cjose")
        self.copy("*", dst="lib",src="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = [ "cjose" ]
        self.cpp_info.libs = [ "cjose_static" ]
