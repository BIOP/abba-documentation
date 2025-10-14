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

**Additional atlas information**

To get detailed information about the currently loaded atlas (including URLs and citations), use **Cite → About current atlas (web)** from the top menu.