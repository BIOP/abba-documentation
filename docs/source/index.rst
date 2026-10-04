ABBA - Aligning Big Brains & Atlases
====================================

.. raw:: html

    <video autoplay loop muted style="width: 100%;">
      <source src="https://user-images.githubusercontent.com/20223054/149301605-07b27dd0-4010-4ca4-b415-f5a9acc8963d.mp4" type="video/mp4">
      Your browser does not support the video tag.
    </video>

ABBA is a set of software components which allows to register images of thin serial biological tissue sections, cut in any orientation (coronal, sagittal or horizontal) to atlases, usually brain atlases. It has been developed by the `BioImaging & Optics Platform <https://www.epfl.ch/research/facilities/ptbiop/>`_ at EPFL.

ABBA consists of a `Fiji <https://fiji.sc/>`_ plugin for the registration part, which is best used in conjunction with `QuPath <https://qupath.github.io>`_. Typically, a set of serial sections is defined as a QuPath project, that is registered within Fiji. The registration results are imported back into QuPath for downstream processing (cell detection and classification, cell counting per region, etc.).

Available atlases include the `3D mouse Allen Brain atlas <http://atlas.brain-map.org/atlas?atlas=602630314>`_ and the `Waxholm Space Atlas of the Sprague Dawley Rat Brain <https://www.nitrc.org/projects/whs-sd-atlas>`_, built into ABBA, as well as all `BrainGlobe atlases <https://brainglobe.info/documentation/brainglobe-atlasapi/usage/atlas-details.html>`_, downloaded on demand.

Once your dataset is registered, you can use `BraiAn <https://silvalab.codeberg.page/BraiAn/>`_ to streamline the analysis.

This documentation describes ABBA |release|. The documentation of the previous version, ABBA 0.11, `remains available <https://abba-documentation.readthedocs.io/en/v0.11.0/>`_.

How this documentation is organized
===================================

* **Getting started** walks you through a first registration on demo slices, from start to finish.
* The **User guide** explains each step of the workflow in detail: preparing a dataset, importing it, orienting, positioning and registering the slices, saving your work and exporting the results.
* The **Reference** lists every menu entry of ABBA with its dialog and parameters, the keyboard and mouse shortcuts, and the file formats.

How to cite ABBA
================

If you use ABBA in your work, please cite the paper below:

.. admonition:: Reference

    Chiaruttini, N.; Castoldi, C.; Requie L. et al. **ABBA+BraiAn, an integrated suite for whole-brain mapping, reveals brain-wide differences in immediate-early genes induction upon learning**, *Cell Reports* (2025).
    https://doi.org/10.1016/j.celrep.2025.115876

Do not forget to cite the third-party tools you used: ABBA can draft the methods section of your publication for you, citations included. See :doc:`cite`.
