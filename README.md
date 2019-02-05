Spack repo for the performance-test, dolfinx, ffcx, and other prerequisite
packages that make up FEniCS.

## Usage

After checking out the repo locally do:
```
spack repo add ./fenics-repo
```
to register the repo in spack. The performance test can then be installed with:
```
spack install fenics-performance-test
```

## Caveats

As dolfinx is under active development, the performance-test specifies a recent
but not quite up to date commit from the master branch.
