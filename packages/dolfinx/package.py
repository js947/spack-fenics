# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Dolfinx(CMakePackage):
    """Next generation FEniCS problem solving environment"""

    homepage = "https://github.com/FEniCS/dolfinx"
    git      = "https://github.com/FEniCS/dolfinx.git"

    version('master', branch='master')
    version('masterish', commit='159476673')

    extends('python')

    variant('doc',  default=False, description='Builds the documentation')

    depends_on('mpi')
    depends_on('hdf5+hl+fortran')
    depends_on('petsc+mpi+shared+hypre+metis~superlu-dist@develop')
    depends_on('py-numpy')
    depends_on('py-sympy')
    depends_on('py-ffcx@master')
    depends_on('py-fiat@master')
    depends_on('py-dijitso@master')
    depends_on('py-ufl@master')
    depends_on('scotch+mpi~metis')
    depends_on('python@3.5:')
    depends_on('py-sphinx@1.0.1:', when='+doc', type='build')
    depends_on('eigen~fftw~metis~mpfr~scotch~suitesparse@3.2.0:')
    depends_on('metis')

    depends_on('swig@3.0.3:', type=('build', 'run'))
    depends_on('cmake@2.8.12:', type='build')

    root_cmakelists_dir = 'cpp'

    def cmake_is_on(self, option):
        return 'ON' if option in self.spec else 'OFF'
