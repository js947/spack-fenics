# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Amgxwrapper(CMakePackage):
    """An interface between PETSc and the NVIDIA AmgX library"""

    homepage = "https://github.com/barbagroup/AmgXWrapper"
    url      = "https://github.com/barbagroup/AmgXWrapper/archive/v1.5.tar.gz"
    git      = "https://github.com/barbagroup/AmgXWrapper.git"

    version('master', branch='master')
    version('1.5', sha256='b3855bc9f5b18d3b55fd1f6ca3c31ece2924eb88bfe751c1988c55a793ce0c93')

    version('js947', branch='js947', git='https://github.com/js947/AmgXWrapper.git')

    depends_on('amgx')
    depends_on('petsc')

    def cmake_args(self):
        return [
            '-DPETSC_DIR=%s' % self.spec['petsc'].prefix,
            '-DCUDA_DIR=%s' % self.spec['cuda'].prefix,
            '-DAMGX_DIR=%s' % self.spec['amgx'].prefix,
        ]
