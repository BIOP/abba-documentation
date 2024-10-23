ABBA - Aligning Big Brains & Atlases
====================================

ABBA is a set of software component which allows to register images of thin serial biological tissue sections, cut in any orientation (coronal, sagittal or horizontal) to atlases, usually brain atlases. It has been developed by the `BioImaging & Optics Platform <https://www.epfl.ch/research/facilities/ptbiop/>`_ at EPFL

ABBA consists of a `Fiji <https://fiji.sc/>`_ plugin for the registration part, which is best used in conjunction with `QuPath <https://qupath.github.io>`_. Typically, a set of serial sections is defined as a QuPath project, that is registered within Fiji. The registration results are imported back into QuPath for downstream processing (cell detection and classification, cell counting per region, etc.).

Available atlases are the `3D mouse Allen Brain atlas <http://atlas.brain-map.org/atlas?atlas=602630314)>`_, and the `Waxholm Space Atlas of the Sprague Dawley Rat Brain <https://www.nitrc.org/projects/whs-sd-atlas>`_. Depending on the way you install ABBA, you may also use all `BrainGlobe atlases <https://brainglobe.info/documentation/brainglobe-atlasapi/usage/atlas-details.html>`_.

Once your dataset is registered, you can use `BraiAn <https://silvalab.codeberg.page/BraiAn/>`_ to streamline the analysis.

How to cite ABBA
================

If you use ABBA in your work, please cite the paper below, currently in pre-print:

.. admonition:: Reference

    Chiaruttini, N., Castoldi, C. et al. ABBA, a novel tool for whole-brain mapping, reveals brain-wide differences in immediate early genes induction following learning. bioRxiv (2024).
    https://doi.org/10.1101/2024.09.06.611625

.. raw:: html

    <video autoplay loop muted style="width: 100%;">
      <source src="https://user-images.githubusercontent.com/20223054/149301605-07b27dd0-4010-4ca4-b415-f5a9acc8963d.mp4" type="video/mp4">
      Your browser does not support the video tag.
    </video>


If you want to check a short presentation of who the biop is and what are ABBA's goals, you can check `this presentation  <https://docs.google.com/presentation/d/1LWlmE8iHpaJhV4bZr8hC3H2cjUDvGUA1s21OdNTCUCg/edit#slide=id.g1259e64410f_0_91>`_:

.. raw:: html

    <iframe src="https://docs.google.com/presentation/d/e/2PACX-1vSPCf8GXPFr8STRMw7zyeIjI2WQzBuY2oHBpG8qZjwzWYQzUTOB4IO5yJN90uWGqIb-OFI5ErWr3YZA/embed?start=false&loop=false&delayms=60000" frameborder="0" width="100%" height="560" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>



