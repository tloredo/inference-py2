# Inference package for Python-2.7

The **`inference`** package is a collection of Python modules implementing a variety of methods targeting the statistical inference problems—and the statistical modeling *style*—of the physical sciences. Our own discipline is astronomy, and our choice of problems and methods most directly targets the needs of astronomers, but tools here may be of use to other physical scientists.

We adopt a narrow view of *statistical inference* for this package: we strive to provide tools that not only provide a "best" estimate or choice in a problem, but that also *quantify uncertainties*. For many scientific purposes, merely knowing what's "best" is not enough; we also need to know the range of possibilities that are "nearly as good." That's the kind of science the `inference` package aims to address.

The modules comprising the **inference** package fall into two categories:

- **Library modules:** These modules implement tools that are largely self-contained. They fall into three categories:
  - *Statistical tools:* These modules implement statistical methods targeting specific, focused problems, such as estimating rates from Poisson-distributed event counts, or fitting a line to data with errors in both abscissa and ordinate.
  - *Utilities:* These modules implement computational algorithms that are useful for statistical computation, but which may be useful in other settings; examples include multi-dimensional numerical integration and Monte Carlo algorithms.
  - *Signal models:* These modules implement functions and classes for calculating predictions from selected widely-used models in astronomy and physics, such as Keplerian models for orbital motion, or cosmological models for the distribution of luminous sources in space-time.
- **Parametric Inference Engine (PIE):** These modules comprise a framework facilitating exploring the parameter spaces of statistical models for data, for three different general modeling approaches: *chi-squared* (or nonlinear weighted least squares), *maximum likelihood*, and *Bayesian*.

This repo archives the last version of `inference` as it was maintained for Python-2.7. API docs (and some initial higher-level documentation) are accessible in the collection of [Selected open-source projects by Tom Loredo](https://tloredo.github.io/). To install `inference`:

* Prepare a Python-2.7 environment that includes NumPy, SciPy, and `matplotlib`.
* Clone this repo.
* Within the `packages` folder, excectute: `python setup.py install --install-platlib DESTINATION`, where `DESTINATION` is any folder included in your Python's `sys.path` (we use the `PYTHONPATH` shell environment variable to point to a local folder holding regularly-used modules and packages).

Revision and refactoring to make `inference`  compatible with Python-3 is ongoing (the revised version is `pip`-installable). All pure-Python modules have been ported, but `inference` includes a number of C and Fortran extension modules that require more extensive revision (due to major changes in the Python-3 and NumPy C APIs). Funding to support this work is being sought; in the meantime, the revision is being undertaken as driven by ongoing research projects.
