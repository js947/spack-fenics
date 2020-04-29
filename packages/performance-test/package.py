# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PerformanceTest(CMakePackage):
    """performance tests for fenics"""

    homepage = "https://github.com/FEniCS/performance-test"
    git = "https://github.com/FEniCS/performance-test.git"

    version("master", branch="master", default=True)
    version("amgx", branch="js947/amgx")

    depends_on("py-ffcx")
    depends_on("dolfinx")
    depends_on("boost+program_options")

    depends_on("amgxwrapper", when="@amgx")

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install(join_path(self.build_directory, "dolfinx-scaling-test"), prefix.bin)

    root_cmakelists_dir = "src"
