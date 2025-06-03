A small python project attempting to define and calculate a metric for convexity of polygons. 

# Visualization dependency

This project includes some visualizations, but this requires a custom local Phanim main branch install of [phanim](https://github.com/quirijndubois/phanim). The [phanim](https://github.com/quirijndubois/phanim) pypi release is too old. Follow the install instructions [here](https://github.com/quirijndubois/phanim).

# usage

Before running one of the python files in the root dir, make sure the cython bindings are compiled. You can do this by running the following:

```bash
cd geometry
```

```bash
python setup.py build_ext --inplace
```

Now you can run any of the python files in the root directory