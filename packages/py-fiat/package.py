# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyFiat(PythonPackage):
    """The FInite element Automatic Tabulator FIAT supports generation of
    arbitrary order instances of the Lagrange elements on lines, triangles, and
    tetrahedra. It is also capable of generating arbitrary order instances of
    Jacobi-type quadrature rules on the same element shapes. Further, H(div)
    and H(curl) conforming finite element spaces such as the families of
    Raviart-Thomas, Brezzi-Douglas-Marini and Nedelec are supported on
    triangles and tetrahedra. Upcoming versions will also support Hermite and
    nonconforming elements"""

    homepage = "https://fenicsproject.org/"
    url = "https://github.com/FEniCS/ufl/archive/2019.1.0.tar.gz"
    git = "https://github.com/FEniCS/ufl.git"

    version("master", branch="master")
    version('2019.1.0',       sha256='46ac0df4e96327be10b9576d2b8fa8b2c4ca62d3c681d407f5718b162d3ca22d')
    version('2018.1.0',       sha256='b0d4c2f43f396fd5609317b70d55b53b89c649962fc8a593f4e0e21607da211d')
    version('2017.2.0.post0', sha256='111e77707cd6731584b1041f405c2fd3f1752a86c51fd9c430524bd396f293b0')
    version('2017.2.0',       sha256='0adff7a511185b20c38ddaccdeed6c1b2ecafe4b163c688bfd1316d5c3b1c00d')
    version('2017.1.0.post1', sha256='82c8170f44c2392c7e60aa86495df22cc209af50735af8115dc35aeda4b0ca96')

    depends_on('py-sympy')
