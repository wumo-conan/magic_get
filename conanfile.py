from conans import CMake, ConanFile, tools
import os

class MagicGetConan(ConanFile):
    name = "magic_get"
    version = "2.0.1"
    url = "https://github.com/apolukhin/magic_get"
    description = "std::tuple like methods for user defined types without any macro or boilerplate code"
    
    settings = "os", "compiler", "build_type", "arch"
    
    no_copy_source = True
    
    def source(self):
        tools.get(f"{self.url}/archive/{self.version}.tar.gz")
    
    def package(self):
        include_folder = os.path.join(
            self.source_folder, f'{self.name}-{self.version}', 'include')
        self.copy(pattern='*.hpp', dst='include', src=include_folder)
    
    def package_id(self):
        self.info.header_only()
