Spack repo for the performance-test, dolfinx, ffcx, and other prerequisite
packages that make up FEniCS.

See the rest of the [spack documentation](https://spack.rtfd.io).

## Usage

After checking out the repo locally do:
```
$ spack repo add ./spack-fenics
```
to register the repo in spack. The performance test can then be installed with:
```
$ spack install performance-test
```

This will make a module which can be loaded via spack:
```
$ spack load -r performance-test
$ which dolfin-scaling-test
/some/long/spack/prefix/bin/dolfin-scaling-test
```

