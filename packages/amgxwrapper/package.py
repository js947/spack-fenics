# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Amgxwrapper(CMakePackage):
    """An interface between PETSc and the NVIDIA AmgX library"""

    homepage = "https://github.com/barbagroup/AmgXWrapper"
    url      = "https://github.com/js947/AmgXWrapper/archive/v1.5.tar.gz"

    version('1.5', sha256='b3855bc9f5b18d3b55fd1f6ca3c31ece2924eb88bfe751c1988c55a793ce0c93')

    depends_on('amgx')
    depends_on('petsc')

    def cmake_args(self):
        return [
            'PETSC_DIR=%s' % self.spec['petsc'].prefix,
            'CUDA_DIR=%s' % sepf.spec['cuda'].prefix,
            'AMGX_DIR=%s' % sepf.spec['amgx'].prefix,
        ]
