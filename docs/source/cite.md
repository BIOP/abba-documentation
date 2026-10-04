# Cite ABBA

## How to cite ABBA

If you use ABBA in your work, please cite the paper below:

:::{admonition} Reference
Chiaruttini, N.; Castoldi, C.; Requie L. et al. **ABBA+BraiAn, an integrated suite for whole-brain mapping, reveals brain-wide differences in immediate-early genes induction upon learning**, *Cell Reports* (2025).
<https://doi.org/10.1016/j.celrep.2025.115876>
:::

Do not forget to cite the third-party tools you used as well: the methods writing assistant below lists them for you.

(methods-writing-assistant)=
## Methods writing assistant

ABBA can draft the methods section of your publication from your actual registration workflow. It writes a prompt describing what was done to the slices, which you paste into the large language model of your choice.

:::{admonition} How to use the methods generator
:class: tip

1. Complete your registration workflow with all slices.
2. Select the slices you want to include in your methods.
3. In the ABBA window, click {menuselection}`Cite --> Generate Methods Prompt` (see [the menu reference](#menu-cite-generate-methods-prompt)).
4. Copy the generated prompt and paste it into your preferred LLM (Mistral, ChatGPT, Claude, etc.).
5. Review and edit the generated methods text carefully before including it in your publication.
:::

:::{admonition} What information is included
:class: note

The generated prompt includes:

* atlas information and configuration (name, DOI, slicing angles);
* the list of registered slices with their positions;
* the registration methods used (DeepSlice, Elastix affine and spline, manual affine, BigWarp);
* the channels used by each registration;
* the spacing between slices;
* relevant citations for all the tools used.
:::

:::{admonition} Example
:class: hint

Want to see what the output looks like? Check out this [example conversation with Mistral AI](https://chat.mistral.ai/chat/45d5595c-0f86-4000-b517-cc29ddad91b6) showing both the generated prompt and the resulting methods section.
:::

:::{admonition} Important
:class: warning

* The generated methods section is a **draft**: always review and verify its content.
* Add the missing experimental details (image acquisition, staining protocols, equipment).
* Fill in any placeholder of the generated text.
* Check that the atlas orientation (coronal, sagittal or horizontal) is correct.
* For manual registrations (BigWarp, manual affine), describe how the landmarks or the transformation were set.
:::

## Citing third-party tools

Here is a list of third-party tools commonly used with or within ABBA. The methods writing assistant includes them automatically when they were used.

**Atlas datasets**

Please cite the publication of the atlas you are using. To get detailed information about the atlas of the session, including its URL and how to cite it, click {menuselection}`Cite --> About Current Atlas (Web)` in the ABBA window.

**BrainGlobe**

If you use BrainGlobe atlases through ABBA, please cite:

> Claudi, F., Petrucco, L., Tyson, A. L. et al. **BrainGlobe Atlas API: a common interface for neuroanatomical atlases**. *Journal of Open Source Software* 5(54), 2668 (2020).
> <https://doi.org/10.21105/joss.02668>

**DeepSlice**

If you use DeepSlice for automated registration, please cite:

> Carey, H., Pegios, M., Martin, L. et al. **DeepSlice: rapid fully automatic registration of mouse brain imaging to a volumetric atlas**. *Nat Commun* 14, 5884 (2023).
> <https://doi.org/10.1038/s41467-023-41645-4>

**Elastix**

If you use the automated affine or spline registrations, please cite:

> Klein, S., Staring, M., Murphy, K., Viergever, M. A., Pluim, J. P. W. **elastix: a toolbox for intensity-based medical image registration**. *IEEE Transactions on Medical Imaging* 29(1), 196-205 (2010).
> <https://doi.org/10.1109/TMI.2009.2035616>

**QuPath**

If you use QuPath for image analysis, please cite:

> Bankhead, P. et al. **QuPath: Open source software for digital pathology image analysis**. *Scientific Reports* 7, 17204 (2017).
> <https://doi.org/10.1038/s41598-017-17204-5>
