from conans import ConanFile, tools
import os

class StrawberryperlinstallerConan(ConanFile):
    name = "strawberryperl_installer"
    version = "0.1"
    license = "MIT"
    url = "https://github.com/KalleDK/conan-strawberryperl-installer"
    settings = {"os": ["Windows"]}

    def build(self):
        keychain = "%s_%s" % ("5.24", "x86_64")
        
        files = {"5.24_x86_64": "http://strawberryperl.com/download/5.24.1.1/strawberry-perl-5.24.1.1-64bit-portable.zip"}
        
        tools.download(files[keychain], "file.zip")
        tools.unzip("file.zip", "dist")

    def package(self):
        self.copy("*", dst="", src="dist")

    def package_info(self):
        self.env_info.path.append(os.path.join(self.package_folder, "c", "bin"))
        self.env_info.path.append(os.path.join(self.package_folder, "perl", "site", "bin"))
        self.env_info.path.append(os.path.join(self.package_folder, "perl", "bin"))
