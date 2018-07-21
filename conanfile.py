from conans import ConanFile, tools


class RaxConan(ConanFile):
    name = "rax"
    version = "master"
    license = "BSD-2-Clause"
    url = "https://github.com/elshize/conan-rax"
    code_url = "https://github.com/antirez/rax"
    description = "A radix tree implementation in ANSI C"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/antirez/rax.git")

    def build(self):
        with tools.chdir("rax"):
            self.run("cc -c -fPIC -std=c99 rax.c -o librax.a")

    def package(self):
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("rax/rax.h", dst="include", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["rax"]

    def configure(self):
        del self.settings.compiler.libcxx
