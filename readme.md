A small python project attempting to define and calcualte some metric for convexity of polygons. Includes visualization demos, using phanim library. 

*Custom local Phanim main branch install is required. The Phanim pypi release is too old. See [phanim](https://github.com/quirijndubois/phanim)*

# usage

Before running one of the python files in the root dir, make sure the cython bindings are compiled. You can do this by running the following:

```bash
cd geometry
```

```bash
python setup.py build_ext --inplace
```

Now you can run any of the python files in the root directory