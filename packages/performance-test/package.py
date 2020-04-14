# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PerformanceTest(CMakePackage):
    """performance tests for fenics"""

    homepage = "https://github.com/FEniCS/performance-test"
    git = "https://github.com/FEniCS/performance-test.git"

    version("master", branch="master")

    depends_on("py-ffcx")
    depends_on("dolfinx")
    depends_on("boost+program_options")

    @run_before("cmake")
    def compile_forms(self):
        ffc = which("ffc", path=self.spec["py-ffcx"].prefix.bin)
        with working_dir("src"):
            ffc("Elasticity.ufl")
            ffc("Poisson.ufl")

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install(join_path("..", "spack-build", "dolfin-scaling-test"), prefix.bin)

    root_cmakelists_dir = "src"

    def cmake_args(self):
        mpi = self.spec["mpi"]
        return ["-DMPI_C_COMPILER=%s" % mpi.mpicc, "-DMPI_CXX_COMPILER=%s" % mpi.mpicxx]
