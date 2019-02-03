# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class FenicsPerformanceTest(CMakePackage):
    """performance tests for fenics"""

    homepage = "https://github.com/FEniCS/performance-test"
    git      = "https://github.com/FEniCS/performance-test.git"

    version('master', branch='master')

    extends('python')

    depends_on('py-ffcx@master')
    depends_on('dolfinx@masterish')
    depends_on('boost+program_options')

    @run_before('cmake')
    def compile_forms(self):
        ffc = which('ffc', path=self.spec['py-ffcx'].prefix.bin)
        with working_dir('src'):
            ffc('-l', 'dolfin', 'Elasticity.ufl')
            ffc('-l', 'dolfin', '-f', 'form_postfix', 'False', 'Poisson.ufl')

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install(join_path('spack-build', 'dolfin-scaling-test'), prefix.bin)

    root_cmakelists_dir = 'src'
