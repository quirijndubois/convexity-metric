A small python project attempting to define and calcualte some metric for convexity of polygons. Includes visualization demos, using phanim library. 

*Phanim main branch is required. The Phanim pypi release is too old.*

# usage

Before running one of the python files in the root dir, make sure the cython bindings are compiled. You can do this by running the following:

```bash
cd geometry
```

```bash
python setup.py build_ext --inplace
```
