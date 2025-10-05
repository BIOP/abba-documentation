ABBA - Aligning Big Brains & Atlases
====================================

.. raw:: html

    <video autoplay loop muted style="width: 100%;">
      <source src="https://user-images.githubusercontent.com/20223054/149301605-07b27dd0-4010-4ca4-b415-f5a9acc8963d.mp4" type="video/mp4">
      Your browser does not support the video tag.
    </video>

ABBA is a set of software components which allows to register images of thin serial biological tissue sections, cut in any orientation (coronal, sagittal or horizontal) to atlases, usually brain atlases. It has been developed by the `BioImaging & Optics Platform <https://www.epfl.ch/research/facilities/ptbiop/>`_ at EPFL.

ABBA consists of a `Fiji <https://fiji.sc/>`_ plugin for the registration part, which is best used in conjunction with `QuPath <https://qupath.github.io>`_. Typically, a set of serial sections is defined as a QuPath project, that is registered within Fiji. The registration results are imported back into QuPath for downstream processing (cell detection and classification, cell counting per region, etc.).

Available atlases include the `3D mouse Allen Brain atlas <http://atlas.brain-map.org/atlas?atlas=602630314)>`_ and the `Waxholm Space Atlas of the Sprague Dawley Rat Brain <https://www.nitrc.org/projects/whs-sd-atlas>`_. Depending on your installation method, you may also access all `BrainGlobe atlases <https://brainglobe.info/documentation/brainglobe-atlasapi/usage/atlas-details.html>`_.

Once your dataset is registered, you can use `BraiAn <https://silvalab.codeberg.page/BraiAn/>`_ to streamline the analysis.

How to cite ABBA
================

If you use ABBA in your work, please cite the paper below:

.. admonition:: Reference

    Chiaruttini, N.; Castoldi, C.; Requie L. et al. **ABBA+BraiAn, an integrated suite for whole-brain mapping, reveals brain-wide differences in immediate-early genes induction upon learning**, *Cell Reports* (2025).
    https://doi.org/10.1016/j.celrep.2025.115876

Citing third-party tools
========================

ABBA integrates several third-party tools and resources. If you use them in your workflow, please cite their respective publications:

**Atlas datasets**

Please cite the relevant publication for the atlas dataset you are using.

**BrainGlobe**

If you use BrainGlobe atlases through ABBA, please cite:

    Claudi, F., Petrucco, L., Tyson, A. L. et al. **BrainGlobe Atlas API: a common interface for neuroanatomical atlases**. *Journal of Open Source Software* 5(54), 2668 (2020).
    https://doi.org/10.21105/joss.02668

**DeepSlice**

If you use DeepSlice for automated registration, please cite:

    Carey, H., Pegios, M., Martin, L. et al. **DeepSlice: rapid fully automatic registration of mouse brain imaging to a volumetric atlas**. *Nat Commun* 14, 5884 (2023).
    https://doi.org/10.1038/s41467-023-41645-4

**QuPath**

If you use QuPath for image analysis, please cite:

    Bankhead, P. et al. **QuPath: Open source software for digital pathology image analysis**. *Scientific Reports* 7, 17204 (2017).
    https://doi.org/10.1038/s41598-017-17204-5


Learn more
==========

For a short presentation about the BioImaging & Optics Platform and ABBA's goals, check out `this presentation <https://docs.google.com/presentation/d/1LWlmE8iHpaJhV4bZr8hC3H2cjUDvGUA1s21OdNTCUCg/edit#slide=id.g1259e64410f_0_91>`_:

.. raw:: html

    <iframe src="https://docs.google.com/presentation/d/e/2PACX-1vSPCf8GXPFr8STRMw7zyeIjI2WQzBuY2oHBpG8qZjwzWYQzUTOB4IO5yJN90uWGqIb-OFI5ErWr3YZA/embed?start=false&loop=false&delayms=60000" frameborder="0" width="100%" height="560" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
