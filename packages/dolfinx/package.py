# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Dolfinx(CMakePackage):
    """Next generation FEniCS problem solving environment"""

    homepage = "https://github.com/FEniCS/dolfinx"
    url = "https://github.com/FEniCS/dolfinx"
    git = "https://github.com/FEniCS/dolfinx.git"

    submodules = True

    version("master", branch="master")
    #extends("python")

    variant("doc", default=False, description="Builds the documentation")

    depends_on("mpi")
    depends_on("hdf5+hl+fortran")
    depends_on("boost")
    depends_on("eigen")
    depends_on("petsc+mpi+shared+hypre+metis~superlu-dist")
    depends_on("scotch+mpi~metis")
    depends_on("py-ufl")
    depends_on("py-ffcx")
    depends_on("py-sphinx@1.0.1:", when="+doc", type="build")

    #depends_on("python@3.5:")

    depends_on("cmake@3.9:", type="build")

    root_cmakelists_dir = "cpp"

    def cmake_args(self):
        mpi = self.spec["mpi"]
        return [
            "-DDOLFIN_SKIP_BUILD_TESTS=True",
            "-DMPI_C_COMPILER=%s" % mpi.mpicc,
            "-DMPI_CXX_COMPILER=%s" % mpi.mpicxx,
        ]
