Spack repo for the performance-test, dolfinx, ffcx, and other prerequisite
packages that make up FEniCS.

See the rest of the [spack documentation](https://spack.rtfd.io).

## Usage

After checking out the repo locally do:
```
$ spack repo add ./fenics-repo
```
to register the repo in spack. The performance test can then be installed with:
```
$ spack install fenics-performance-test
```

This will make a module which can be loaded via spack:
```
$ spack load -r fenics-performance-test
$ which dolfin-scaling-test
/some/long/spack/prefix/bin/dolfin-scaling-test
```

## Caveats

As dolfinx is under active development, the performance-test specifies a recent
but not quite up to date commit from the master branch.

The fenics-performance-test package currently only contains the binary for
`dolfin-scaling-test`.
