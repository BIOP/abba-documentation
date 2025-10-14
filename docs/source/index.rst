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

Do not forget to include third party tools. The methods writing assistant is handy for that.

Methods writing assistant
=========================

ABBA includes a built-in tool to help you write the methods section for your publication. This feature automatically generates a draft methods paragraph based on your actual registration workflow.

.. admonition:: How to use the methods generator
   :class: tip

   1. Complete your registration workflow with all slices
   2. Select the slices you want to include in your methods
   3. Navigate to **Cite → Generate methods prompt** in the top menu
   4. Copy the generated prompt and paste it into your preferred LLM (Mistral, ChatGPT, Claude, etc.)
   5. Review and edit the generated methods text carefully before including it in your publication

.. admonition:: What information is included
   :class: note

   The generated prompt includes:

   * Atlas information and configuration (name, DOI, rotation adjustments)
   * List of registered slices with their positions
   * Registration methods used (DeepSlice, Elastix affine/spline, BigWarp manual)
   * Channel mappings for multi-channel registrations
   * Inter-slice spacing information
   * Relevant citations for all tools used

.. admonition:: Example
   :class: hint

   Want to see what the output looks like? Check out this `example conversation with Mistral AI <https://chat.mistral.ai/chat/45d5595c-0f86-4000-b517-cc29ddad91b6>`_ showing both the generated prompt and the resulting methods section.

.. admonition:: Important
   :class: warning

   * The generated methods section is a **draft** - always review and verify the content
   * Add missing experimental details (image acquisition, staining protocols, equipment)
   * Fill in any placeholders marked in the generated text
   * Verify that atlas orientation (coronal/sagittal/horizontal) is correctly specified
   * For manual BigWarp registrations, add the number of control points used


Citing third-party tools
========================

Here's a list of common third party tools that may be used with or within ABBA. They should automatically be included (if relevant) with the writing assistant.

**Atlas datasets**

Please cite the relevant publication for the atlas dataset you are using. To get detailed information about the currently loaded atlas (including URLs and citations), use **Cite → About current atlas (web)** from the top menu.
This should automatically included in the methods assistant.

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
