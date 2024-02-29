# MT-Ranker
This is the repository for the ICLR'24 Spotlight paper [MT-Ranker: Reference-free machine translation evaluation by inter-system ranking](https://openreview.net/forum?id=Rry1SeSOQL).

# Background

# Our Work

# Spaces
Here is the [link](https://huggingface.co/spaces/ibraheemmoosa/mt-ranker) to a huggingface space hosting our model.

# Models
Our models are available on huggingface hub.
1. [MT-Ranker-Base](https://huggingface.co/ibraheemmoosa/mt-ranker-base)
2. [MT-Ranker-Large](https://huggingface.co/ibraheemmoosa/mt-ranker-large)
3. [MT-Ranker-XXL](https://huggingface.co/ibraheemmoosa/mt-ranker-xxl)

# Usage
Use the `load_model_from_huggingface_hub.py` to load the models. The models take in a source sentence and pair of translations in the following format.

`Source: Le chat est sur la tapis. Translation 0: The cat is on the bed. Translation 1: The cat is on the carpet.`

The model performs a binary classification and returns probability logits for the two translations.

# TODO
- [x] Upload models to Huggingface Hub.
- [x] Add model loading code to GitHub.
- [ ] Add training code to GitHub
- [ ] Streamline model loading.
- [x] Add link to Huggingface Spaces.

# Citation
Please cite our work if you find it helpful.

```
@inproceedings{
Moosa2024MTRankerRM,
title={MT-Ranker: Reference-free machine translation evaluation by inter-system ranking},
author={Ibraheem Muhammad Moosa and Rui Zhang and Wenpeng Yin},
booktitle={The Twelfth International Conference on Learning Representations},
year={2024},
url={https://openreview.net/forum?id=Rry1SeSOQL}
}
```
